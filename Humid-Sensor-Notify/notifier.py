import os
import line_notify as lin  
from dotenv import load_dotenv

load_dotenv()

client = lin.LineNotify(token = os.getenv('LINE_TOKEN'))

def send_text_notification(args: str):
    client.notify(args)

def send_image_notification(path: str):
    client.notify(imgs = path)

if __name__ == '__main__':
    client.notify('Hello, world!')
    client.notify(imgs ='./assets/1649057854.jpeg')