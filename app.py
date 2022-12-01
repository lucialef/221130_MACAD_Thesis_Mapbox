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
def process_post():
  data_in = request.form
  sel_month = data_in['sel_month']

  print(sel_month)
  return "yeahh"

@app.route('/no', methods=['POST'])
def xx():
  data_in = request.form
  coord_start = data_in['coord_start']
  coord_end = data_in['coord_end']
  sel_month = data_in['sel_month']
  data_fin = seasonal.getRoutes(coord_start, coord_end, sel_month)
  print(data_fin)
  
  return data_fin


if __name__ == '__main__':
  app.run(debug=True, threaded=True)