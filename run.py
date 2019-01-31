import os
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/subtitle',methods = ['POST', 'GET'])
def welcome_user():
   if request.method == 'POST':
      hash=request.json['hash']
      return "working"
   else:
      return render_template("index.html")

if __name__ == '__main__':
   app.run()