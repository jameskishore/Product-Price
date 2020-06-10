from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/html-table.html')
# def html_table():
#     return render_template('html-table.html')