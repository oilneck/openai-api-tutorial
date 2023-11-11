from openai import OpenAI

def chat(prompt:str, system_msg:str="You are a helpful assistant."):
    client = OpenAI()
    try:
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ],
        )
        result = response.choices[0].message.content
        return result
    except AttributeError as e:
        result = f"Error: {e}"
        return result