#!/usr/bin/python3
# -*- coding: utf-8 -*-

### General imports ###
from __future__ import division
import numpy as np
import pandas as pd
import time
import os

### Flask imports
from flask import Flask, render_template, session, request, redirect, flash, Response

# Flask config
app = Flask(__name__)
app.secret_key = b'(\xee\x00\xd4\xce"\xcf\xe8@\r\xde\xfc\xbdJ\x08W'

################################################################################
################################## INDEX #######################################
################################################################################

# Home page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Communal roads
@app.route('/com', methods=['GET','POST'])
def index_com():
    return render_template('com.html')

# Departmental roads
@app.route('/dep', methods=['GET','POST'])
def index_dep():
    return render_template('dep.html')

# National roads
@app.route('/nat', methods=['GET','POST'])
def index_nat():
    return render_template('nat.html')

# HighWay
@app.route('/aut', methods=['GET','POST'])
def index_aut():
    return render_template('aut.html')

# Exploration
@app.route('/all', methods=['GET','POST'])
def index_all():
    return render_template('all.html')
    
if __name__ == '__main__':
    app.run(debug=True)
