import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT
from call_functions import available_functions, call_function

def main():
    
    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('Usage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    prompt_text = ' '.join(args)
    messages = [types.Content(parts=[types.Part(text=prompt_text)], role="user")]

    if verbose:
         print(f"User prompt: {prompt_text}")

    for _ in range(0, 20):
        try:
            response = generate_response(client, messages, verbose)
            if response:
                print(f"{response}")
                break
        except Exception as e:
            print(f"{e}")
    

def generate_response(client, messages, verbose):
    
    response = client.models.generate_content(model="gemini-2.0-flash-001", 
                                              contents=messages, 
                                              config=types.GenerateContentConfig(tools=[available_functions], system_instruction=SYSTEM_PROMPT)
                                              )
    
    agent_messages = response.candidates
    for agent_message in agent_messages:
        messages.append(agent_message.content)

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    function_calls = response.function_calls

    if not function_calls:
        return f"Response:\n{response.text}"
        
    for function in function_calls:
            func_call_response = call_function(function, verbose)
            func_response = func_call_response.parts[0].function_response.response
            if not func_response:
                raise Exception(f"Error: no response from {function.name}.")
            if verbose:
                print(f"-> {func_response['result']}")
            
            user_message = types.Content(parts=[types.Part(text=func_response['result'])], role="user")
            messages.append(user_message)
            

if __name__ == "__main__":
    main()