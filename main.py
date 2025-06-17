import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

#arg[0] is the script name
#arg[1] is the first expected arg
list_len = len(sys.argv)
show_more = False
if list_len == 1:
    # print("Arguments passed:")
    # for arg in sys.argv[1:]:
    #     print(arg)
    print("Error No arguments provided.")
    sys.exit(1)
elif list_len >= 2:
    user_prompt = sys.argv[1]
if list_len >= 3:    
    if sys.argv[2] == "--verbose":
        show_more = True            

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file relative to the working directory.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)
schema_run_python_file = types.FunctionDeclaration(
    name="run_command",
    description="Executes a shell command in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "command": types.Schema(
                type=types.Type.STRING,
                description="The shell command to execute.",
            ),
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to execute the command in, relative to the working directory. If not provided, executes in the working directory itself.",
            ),
        },
    ),
)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
# response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages,
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file ,
    ],
    temperature=0.2,
    max_output_tokens=1024,
    top_p=0.95,
    top_k=40,
)
print(response.text)
if show_more:
    meta = response.usage_metadata
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {meta.prompt_token_count}")
    print(f"Response tokens: {meta.candidates_token_count}")