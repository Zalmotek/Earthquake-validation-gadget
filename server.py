__author__ = 'cristi'
from datetime import datetime

import twitter
from flask import Flask



CONSUMER_KEY = '7vkkFq3i6F63zwPTpxeMnt1zq'
CONSUMER_SECRET = 'VuODKr2LzEEzsMG5La10CNpYYMb2m9oUIS3Ffl3ea5BN0W2Sk9'
ACCESS_TOKEN = '862241031940603904-UK9htq79xVWYwMtn89vNw6UHAgbQVcI'
ACCESS_TOKEN_SECRET = 'AQrAqWAp4MTnPJtb7JqEG94xMfnCRViPX8vWbnmJmPgGo'


def detect_earthquake():
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET)
    today = datetime.now()
    query = "q=cutremur%20&result_type=recent&since={}-{}-{}&count=100&geocode=44.413731,26.158461,150km&lang=ro".format(
        today.year, today.month, today.day)
    results = api.GetSearch(raw_query=query)
    return results


app = Flask(__name__)

@app.route("/")
def hello():
    return str(len(detect_earthquake()))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8013)