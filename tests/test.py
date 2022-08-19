import requests

headers = {
    "accept": "application/json",
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

files = {
    "data": open("images/noita.jpg", "rb"),
}

response = requests.post("http://127.0.0.1:8000/image/", headers=headers, files=files)
print(response.text)
