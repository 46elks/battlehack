from flask import Flask
import apini

app = Flask(__name__)

@app.route('/')
def index():
    return apini.random_url()

@app.route('/incomingsms', methods=['POST'])
def incomingsms():
    return ''

@app.route('/pay', methods=['POST'])
def post_handler(payid):
    return ''

@app.route('/pay/<payid>')
def pay(payid):
    return ''

if __name__ == '__main__':
    print('Starting server...')
    app.run(debug=True)

