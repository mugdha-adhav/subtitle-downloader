import os
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from src import provision
import constants
import json

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

class SubsRequest:
   def __init__(self, opensubshash, subsdbhash, filesize):
      self.opensubshash = opensubshash
      self.subsdbhash = subsdbhash
      self.filesize = filesize

@app.route('/subtitle',methods = ['POST', 'GET'])
@cross_origin(origin='http://www.subsworld.site',headers=['Content-Type'])
def welcome_user():
   if request.method == 'POST':
      subrequest = SubsRequest(request.json['opensubsHash'], request.json['subsdbHash'], request.json['fileSize'])
      subs=provision(subrequest, constants.LANGUAGE)
      if not subs:
         return json.dumps({'status': 400,'data':None})
      return json.dumps({'status': 200,'data':""+subs+""})
   else:
      return render_template("index.html")

if __name__ == '__main__':
   app.run()