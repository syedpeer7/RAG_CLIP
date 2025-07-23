from PIL import Image
from io import BytesIO
import requests

def download_images(image_urls):
    images = []
    for url in image_urls:
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content)).convert("RGB")
            images.append((url, img))
        except:
            continue
    return images
