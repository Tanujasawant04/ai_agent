import os
from dotenv import load_dotenv
from google import genai
from google.genai import types



load_dotenv()
# we loaded API key 

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
# created a instnace for Clinet -> connect to genai (Google studio(geminiai))

# Create the chat session
chat = client.chats.create(model="gemini-2.5-flash") 

print("Chat starts here! (Type 'end chat' to stop)")
user_input = ""

while user_input.lower() != "end chat":
    user_input = input("User: ")
    #user_input = "end chat"
    
    if user_input.lower() == "end chat":
        break
        
    # Send message through the chat session object
    response = chat.send_message(user_input)
    
    print(f"Chatbot: {response.text}")


print("\n--- Full Chat History ---")
for message in chat.get_history():
    role = message.role  # 'user' or 'model'
    text = message.parts[0].text
    print(f"[{role.upper()}]: {text}")    