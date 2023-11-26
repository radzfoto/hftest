from huggingface_hub import InferenceClient
from PIL import Image

client = InferenceClient()
image = client.text_to_image("A photorealistic image of a woman swimming in a lake")
image.save("images/woman_swimming.png")
