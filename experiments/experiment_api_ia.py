import os
from openai import AzureOpenAI

endpoint = "https://testetcc2025.openai.azure.com/"
model_name = "gpt-35-turbo"
deployment = "AI_PROTOTIPO_TCC"

subscription_key = "1UsI8dFVR3bZNz1LooLBwFiaT9q8g5sG4xnncXuYmSE7vdoCE8u6JQQJ99BDACZoyfiXJ3w3AAABACOGLXBE"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)

print(response.choices[0].message.content)