
from flask import *
 
app = Flask(__name__)

items = []
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
    return render_template('form.html', items=items)

@app.route('/add_todo')
def add_todo():
    item = request.args.get("item")
    print(item)
    items.append(item)
    return redirect("http://localhost:5000/", code = 302)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')