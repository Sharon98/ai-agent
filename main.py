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


messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
)
print(response.text)
if show_more:
    meta = response.usage_metadata
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {meta.prompt_token_count}")
    print(f"Response tokens: {meta.candidates_token_count}")