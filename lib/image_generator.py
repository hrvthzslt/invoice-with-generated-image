import openai


class ImageGenrator:
    def __init__(self, key: str):
        openai.api_key = key

    @staticmethod
    def generate(prompt: str) -> str:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="256x256"
        )
        return response['data'][0]['url']
