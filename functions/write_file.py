#Allows the agent to create or write a file

import os
from google.genai import types


def write_file(working_directory, file_path, content):
    #make sure the requested access is inside the permitted directory
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'    
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)    
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing file "{file_path}": {e}'

#Explain functionality to the agent
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