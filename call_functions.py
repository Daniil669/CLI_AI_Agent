from google.genai import types
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.write_file import write_file, schema_write_file
from functions.run_python import run_python_file, schema_run_python_file
from functions.get_file_content import get_file_content, schema_get_file_content

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_write_file,
        schema_run_python_file,
        schema_get_file_content
    ]
)

def call_function(function_call_part, verbose=False):

    func_name = function_call_part.name
    func_args = function_call_part.args
    func_args['working_directory'] = './calculator'

    if verbose:
        print(f"Calling function: {func_name}({func_args})")
    
    print(f" - Calling function: {func_name}")
    print(f" - {func_name} args: {func_args}")

    match(function_call_part.name):
        case "get_files_info":
            result = get_files_info(**func_args)
            return types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=func_name,
                            response={"result": result},
                        )
                    ],
                )
        case "get_file_content":
            result = get_file_content(**func_args)
            return types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=func_name,
                            response={"result": result},
                        )
                    ],
                )
        case "write_file":
            result = write_file(**func_args)
            return types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=func_name,
                            response={"result": result},
                        )
                    ],
                )
        case "run_python_file":
            result = run_python_file(**func_args)
            return types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=func_name,
                            response={"result": result},
                        )
                    ],
                )
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=func_name,
                        response={"error": f"Unknown function: {func_name}"},
                    )
                ],
            )