import requests

def get_kitty():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url, 'api_key = 3c8bfe29-9507-476a-8e55-a9b8be5b578d')
    pic = response.json()[0]["url"]
    print(response)
    return (pic)
