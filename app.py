from flask import Flask, jsonify,render_template
from forms import CurrencyRate
import logging
import requests
import config

app = Flask(__name__)

app.debug = config.DEBUG
API_KEY = config.API_KEY
app.secret_key = "development-key"
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def index():
  form=CurrencyRate()
  return render_template("index.html",form=form)


@app.route('/rate/<currency1>/<currency2>')
def get_currency_rate(currency1, currency2):
    data = call_exchange_rate(currency1, currency2)
    if data['result'] == 'success':

        return jsonify({'from': data['from'], 'to': data['to'],
                       'rate': data['rate']})
    else:
        return jsonify(data)


@app.route('/convert/<currency1>/<float:amount>/<currency2>')
def convert_currency(currency1, currency2, amount):

    data = call_exchange_rate(currency1, currency2)
    if data['result'] == 'success':
        converted_amount = amount * data['rate']

        return jsonify({
            'from': data['from'],
            'from_amount': amount,
            'converted_amount': '{0:.2f}'.format(converted_amount),
            'to': data['to'],
            })
    else:
        return jsonify(data)


def call_exchange_rate(currency1, currency2):
    try:

        # Exchange rate api url

        url = 'https://v3.exchangerate-api.com/pair/' + API_KEY + '/' \
            + currency1 + '/' + currency2
        logger.info('Exchange rate API url' + url)

        # Making our request

        response = requests.get(url)
        logger.info('Response status from API'
                    + str(response.status_code))
        data = response.json()

        return data
    except requests.exceptions.RequestException, e:
        raise default_error_handler(e)


@app.errorhandler
def default_error_handler(error):
    '''Default error handler'''

    return ({'message': str(error)}, getattr(error, 'code', 500))

if __name__ == '__main__':
    app.run(debug=True)

			