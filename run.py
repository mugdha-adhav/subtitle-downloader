import os
from flask import Flask, render_template, request
from src import provision
import constants
app = Flask(__name__)

@app.route('/subtitle',methods = ['POST', 'GET'])
def welcome_user():
   if request.method == 'POST':
      opensubsHash=request.json['opensubsHash']
      subsdbHash=request.json['subsdbHash']
      movieSize=request.json['movieSize']
      subs=provision(subsdbHash, constants.LANGUAGE)
      if not subs:
         return "bad_request"
      return subs
   else:
      return render_template("index.html")

if __name__ == '__main__':
   app.run()