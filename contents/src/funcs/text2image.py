import requests
from openai import OpenAI



def download_image(url:str, file_path:str):

    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                for chunk in response:
                    file.write(chunk)
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False



def text2image(prompt:str, filename:str='./image.jpg'):
    client = OpenAI()

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1, # You must provide n=1 for dalle-e-3 model
    )

    return download_image(response.data[0].url, filename)
