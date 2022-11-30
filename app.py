from flask import Flask, render_template, request

import seasonal
import json


app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/info', methods=['POST'])
def process_post();
  data_in = request.form
  start = data_in['start']
  end = data_in['end']
  month = data_in['month']
  data_fin = seasonal.getRoutes(start, end, month)
  return data_fin


if __name__ == '__main__':
    app.run(port=port_no)