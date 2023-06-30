
python
from flask import Flask, render_template, request
from our_parser import parse_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse():
    url = request.form.get('url')
    data = parse_data(url)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
