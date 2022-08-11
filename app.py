from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



import requests

response_API = requests.get('https://www.askpython.com/')
print(response_API)

languages = ['en', 'es', 'hu']

for language in languages:
    if language == 'en':
        print('English is prodominently spoken in England, America, Australia.')
    elif language == 'hu':
        print('Hungarian is prodominently spoken in Hungary.')
    elif language == 'es':
        print('Spanish is prodominently spoken in Spain and South America.')

