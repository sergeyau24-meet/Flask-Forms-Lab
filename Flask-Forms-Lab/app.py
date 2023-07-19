from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
  if request.method == 'GET':
  	return render_template('login.html')
  else:
  	UnIn = request.form['username']
  	PsIn = request.form['password']

  	if UnIn == username and PsIn == password:
  		return redirect(url_for('home'))
  	else:
  		return render_template('login.html')
@app.route('/home')
def home():
 return render_template('home.html',list = facebook_friends)

enemy= "Vadim"
@app.route('/friends_exists/<string:eName>')
def friends(eName):
	return render_template('friend_exists.html', st = eName in facebook_friends)



  
  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)