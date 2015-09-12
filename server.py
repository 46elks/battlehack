from flask import Flask, request, render_template
from urllib.parse import parse_qs
import braintree
import apini
import elks
import re

app = Flask(__name__)
baseurl = 'https://apini.theusr.org/pay/%s'

@app.route('/')
def index():
    return apini.random_url()

@app.route('/incomingsms', methods=['POST'])
def incomingsms():
    rawmessage = request.form['message'].strip()
    rawmessage = rawmessage.split()
    rawmessage = list(map(lambda x: x.strip(), rawmessage))
    sender = request.form['from']
    if re.match("\+[0-9]*", rawmessage[0]):
        recipient = rawmessage[0]
        amount = rawmessage[2]
    else:
        recipient = sender
        amount = rawmessage[1]
    url = apini.insert_transaction(int(amount), sender, recipient)
    if recipient == sender:
        return baseurl % url
    else:
        elks.send_url(url, amount, recipient)
    return ''

@app.route('/pay', methods=['POST'])
def post_handler(payid):
    return ''

@app.route('/pay/<payid>')
def pay(payid):
    braintree.Configuration.configure(braintree.Environment.Sandbox,
        merchant_id="dfxyx8mq4y7m4zrw",
        public_key="xx9zvf5nf4wvgryz",
        private_key="51570311b8ece6b2c49a63c31080518a")
    token = braintree.ClientToken.generate()
    amount = apini.get_amount(payid)
    return render_template('payform.html',
                           amount=amount,
                           token=token,
                           uri=payid)
    

if __name__ == '__main__':
    print('Starting server...')
    app.run(debug=True)

