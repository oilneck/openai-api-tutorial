import base64
from openai import OpenAI

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def image2text(impaths:list, prompt:str, max_tokens:int=300):

    if isinstance(impaths, str):
        impaths = [impaths]


    encimgs = [encode_image(path) for path in impaths]

    image_url_list = [
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64, {imurl}"
            }
        } for imurl in encimgs
    ]


    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    *image_url_list
                ],
            }
        ],
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content
