from random import shuffle
from base64 import b64encode


imgs = ["Хорошая работа!", "Молодец", "Круто", "Великолепно!", "Высший пилотаж"]
shuffle(imgs)


def get_image():
    with open(f"ipfs/{imgs[0]}.png", "rb") as image_file:
        encoded_string = b64encode(image_file.read())
    return {"base64": encoded_string, "NFTName": imgs[0]}

