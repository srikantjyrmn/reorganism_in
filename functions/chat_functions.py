import os
from dotenv import load_dotenv
load_dotenv()
import requests
from flask import jsonify
from prompts import self_rag_agent
from openai import OpenAI
import json

def chat_with_openai(message, system_prompt = self_rag_agent):
    """Chat with the OpenAI API
    """
    # Get the API key from environment variable
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("OPENAI_API_KEY not found in environment variables")
        return "OPENAI_API_KEY not found in environment variables"

    print(f"API Key found: {api_key[:5]}...") # Print first 5 characters for verification

    # Set the OpenAI API key
    #openai.api_key = api_key

    try:
        print("Sending request to OpenAI API...")
        response = OpenAI(api_key = api_key).chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            max_tokens=1000,
            temperature=0.5
        )
        print("Successfully received response from OpenAI API")
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in OpenAI API request: {e}")
        return f"Error in OpenAI API request: {e}"

from flask import Response

def chat_with_pi(message):
    if not message:
        return jsonify({'error': 'Missing ngrok_url or text'}), 400

    try:
        response = requests.post(
            f'https://knowing-sincerely-hyena.ngrok-free.app/chat',
            json={'text': message},
            timeout=30
        )
        
        return json.loads(response.content)#['result']
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500