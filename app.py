# ---- Flask Hello World ---- #

# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!?!?!?!"

# adding a new route called test which will return Hello in text
@app.route("/test/<search_query>")	
def search(search_query):
	return search_query

# creating one of three new views
@app.route("/integer/<int:value>")
def int_type(value):
	print ("value + 1")
	return "correct"

# create second of the thrid new view
@app.route("/float/<float:value>")
def float_type(value):
	print ("value + 1")
	return "correct"

#dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
	print (value)
	return "correct"

#adding a new route
@app.route("/name/<name>")
def indesx(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name), 200
	else:
		return "Not Found", 404

# start the development server using the run() method
if __name__ == "__main__":
	app.run()