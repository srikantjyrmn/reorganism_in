# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
from chat_functions import chat_with_openai
import os
initialize_app()

@https_fn.on_call()
def chat_fn(req: https_fn.CallableRequest) -> dict:
    try:
        data = req.data
        message = data.get('message', '')
        
        # First, create the "Yes, I heard" response
        heard_response = f"Yes, I heard: {message}"
        
        # Try to get a response from Claude
        try:
            # Use Firebase config in production, fallback to environment variable
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                raise ValueError("OPENAI_API_KEY not found")
            
            os.environ['OPENAI_API_KEY'] = api_key  # Ensure the API key is in the environment
            claude_response = chat_with_openai(message)
            if claude_response:
                full_response = f"{claude_response}"
            else:
                full_response = f"{heard_response}\n\nClaude did not provide a response."
        except Exception as claude_error:
            print(f"Error calling Claude API: {str(claude_error)}")
            full_response = f"{heard_response}\n\nUnable to get a response from Claude at this time."
        
        return {"result": full_response}
    except Exception as e:
        print(f"Error in chat function: {str(e)}")
        return {"error": str(e)}