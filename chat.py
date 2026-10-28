from openai import OpenAI

client = OpenAI(api_key="API_key")

prompt = input("Enter your prompt: ")

response = client.chat.completions.create(
    messages=[
        {"role": "user", "content": prompt}
    ],
    model="gpt-5"
)

print(response.choices[0].message.content)