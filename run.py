import pandas as pd
import json
from StringIO import StringIO 
import matplotlib.pyplot as plt
import numpy as np

from flask import Flask, render_template, jsonify
from flask.ext.cors import CORS


app = Flask("rapido")
app.config["DEBUG"] = True
cors = CORS(app, resources={r"/*": {"origins": "*"}})



def JsonParser(data):
	try:
		return json.loads(data)
	except: 
		return
# 
def latlongs(data):
	alllats = []
	# alljson = []
	# alljson["data"] =[]
	for i in data:
		alllats = alllats + [ [l["latitude"],  l["longitude"], l["time"] ]   for l in i]
		# alljson + i
		# Implementation for Grouping by time on the given json
	# pd.read_json(json.loads(dict(alljson)))
	# print alljson[["time"]].groupby(pd.TimerGroup(freq='20min'))
	print len(alllats)
	return alllats


def readingCsv():
	all_data = pd.read_csv("2.csv",sep=',',header= None, names= '0 1'.split(), usecols=['0','1'] , nrows=13,converters={'1':JsonParser}, dtype=unicode)
	jso =  all_data['1']
	cols = ['lats', 'long']
	latslogns = latlongs(all_data['1'])	
	return latslogns


@app.route('/')
def show():
	df = readingCsv()
	return render_template('index.html', data=df)


@app.route('/return')
def get():
	df = readingCsv()
	return jsonify({"data": df})

app.run()