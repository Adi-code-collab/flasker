from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')

#def index():
#	return "<h1>Hello wprld!!<!h1>"

def index():
	first_name = "JACK"
	fav_pizza=['cheese','tomata','onion','gravy']
	stuff = "this is bold txxxxx"
	return render_template("index.html",
	 first_name=first_name,
	 stuff=stuff,
	 fav_pizza=fav_pizza)


@app.route('/user/<name>')

def user(name):
	return render_template("user.html",user_name=name)
#reate custom error page

#invalid server error 
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#invalid server error 
@app.errorhandler(404)
def page_not_found(e):
	return render_template("500.html"), 500