from .flickr import FlackrImage
import requests
from PIL import Image
from io import BytesIO
import os
import io


class ImageWatermark(object):
    def __init__(self):
        self.img = FlackrImage()

    def get_img(self):
        url = self.img.get_random_image('industrial')['url_l']
        img = requests.get(url, stream=True)
        return img.content

    def watermark(self):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'watermark')
        watermark = Image.open(f'{path}/Logo-1-01.png').convert('RGBA')
        watermark = watermark.resize((120, 42), Image.ANTIALIAS)
        random_image = Image.open(BytesIO(self.get_img()))
        thumb = Image.new(mode='RGBA', size=(random_image.size[0], 60), color=(255, 255, 255, 100))
        thumb.paste(watermark, (int(random_image.size[0]/2-watermark.size[0]/2), 5), watermark)
        random_image = random_image.convert('RGBA')
        random_image.paste(thumb, (0, 0), thumb)
        byte_arr = io.BytesIO()
        random_image.save(byte_arr, format="png")
        byte_arr = byte_arr.getvalue()
        return byte_arr


