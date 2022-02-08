from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def call():
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    randombeer=(r.json())
    '''print(randombeer[0]['name'])
    print(randombeer[0]['abv'])
    print(randombeer[0]['description'])
    print(randombeer[0]['food_pairing'][0])'''

    beer = {
       'name': randombeer[0]['name'],
       'abv': randombeer[0]['abv'],
       'desc': randombeer[0]['description'],
       'first' :randombeer[0]['first_brewed'],
       'food': randombeer[0]['food_pairing'][0]
       
  }

    print(beer)

    return render_template('index.html', beer=beer)
if __name__ == "__main__":
     app.run(debug=True, host='0.0.0.0')