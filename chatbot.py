from dotenv import load_dotenv
from openai import OpenAI

import os
import json


# Load .env file
load_dotenv()

# Load API key
api_key = os.getenv("open_router_api")


# OpenRouter client setup
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


# Function to load disease database
def load_disease_data():

    with open("disease_data.json", "r") as file:
        return json.load(file)


# Function for local database response
def get_local_response(user_query):

    diseases = load_disease_data()

    query = user_query.lower()

    for disease in diseases:

        # Match disease name in query
        if disease.lower() in query:

            data = diseases[disease]

            symptoms = "\n- ".join(
                data["symptoms"]
            )

            prevention = "\n- ".join(
                data["prevention"]
            )

            return f"""
Disease: {disease}

Symptoms:
- {symptoms}

Prevention:
- {prevention}

Treatment:
{data['treatment']}

Vaccination:
{data['vaccination']}
"""

    return None


# Function for AI response
def get_ai_response(user_query):

    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[

            {
                "role": "system",
                "content": """
You are an AI Healthcare Chatbot.

Your responsibilities:

1. Explain diseases.
2. Explain symptoms.
3. Suggest prevention methods.
4. Promote vaccination awareness.
5. Promote healthy lifestyle practices.
6. Never provide medical diagnosis.
7. Always recommend consulting healthcare professionals.

Keep responses simple and educational.
"""
            },

            {
                "role": "user",
                "content": user_query
            }

        ]
    )

    return response.choices[0].message.content


# Main response function
def get_response(user_query):

    # First check local database
    local_answer = get_local_response(
        user_query
    )

    if local_answer:
        return local_answer

    # Otherwise use AI
    try:

        return get_ai_response(
            user_query
        )

    except Exception as e:

        return f"""
Error Occurred:
{str(e)}
"""