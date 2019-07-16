
from flask import Flask, render_template
 
app = Flask(__name__)
''' 
@app.route('/greetings')
def index():
    return 'Hello world'

@app.route('/whereiam')
def where_i_am():
    return 'ghana'
'''

@app.route('/')
def tee():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')