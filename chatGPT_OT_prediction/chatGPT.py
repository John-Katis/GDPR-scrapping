import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def predict_ot_words(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    # Extract the message content from the response
    return response["choices"][0]["message"]["content"]
