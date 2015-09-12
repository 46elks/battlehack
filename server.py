from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Apini Battlehack Submission!\nNot much too see here :)'

@app.route('/incomingsms')
def incomingsms():
    return ''

@app.route('/p')
def paylanding():
    return ''

@app.route('/p/<payid>')
def pay(payid):
    return ''

if __name__ == '__main__':
    print('Starting server...')
    app.run()

