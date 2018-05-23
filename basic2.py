__author__ = 'gavin'


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('test.html')

@app.route('/hello', methods=['POST'])
def hello():
    fullname = request.form['full_name']
    usphone = request.form['usphone']
    email = request.form['email']
    addy1 = request.form['add_one']
    addy2 = request.form['add_two']
    zip = request.form['zip']
    card = request.form['card_number']
    cvv = request.form['cvv_number'] 
    exp = request.form['exp_date']
    return'Profile Created: {}'.format(fullname)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)



