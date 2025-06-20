#Allows the agent to run a Python script

import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    #Is it in the work area?
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    #is it a python script?
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:     
        result = subprocess.run(["python3", file_path], timeout=30,  text=True, capture_output=True, cwd=working_directory)                
        
        if result.returncode != 0:
            return f'Process exited with code {result.returncode}'
        elif len(result.stderr) > 0:
            return f'STDERR: {result.stderr}'    
        if len(result.stdout) == 0:
            return 'No output produced.'        
        else:
            return f'STDOUT: {result.stdout}'
                    
    except subprocess.TimeoutExpired as e:
        return f"Error: executing Python file: {e}"
    except subprocess.CalledProcessError as e:
        return f"STDERR: {e.stderr}"

#Explain functionality to the agent
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)