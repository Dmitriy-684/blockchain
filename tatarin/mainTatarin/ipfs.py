import ipfsapi
from genImg import get_image


def ipfs_load_json(wallet, level):
    try:
        if level not in ["1", "3", "5", "7", "10"]: return "NoReward"
        ip, port = "127.0.0.1", 5001
        api = ipfsapi.Client(ip, port)
        image = get_image()
        json = str({"base64": image["base64"],
                    "Wallet": wallet,
                    "NFTName": image["NFTName"]})
        json_hash = api.add_json(json)
        return json_hash
    except AttributeError:
        return "None"


def ipfs_get_json(hash):
    try:
        ip, port = "127.0.0.1", 5001
        api = ipfsapi.Client(ip, port)
        json = api.get_json(hash)
        return json
    except AttributeError:
        return "None"