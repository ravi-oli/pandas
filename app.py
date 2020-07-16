# Import libraries
import flask 
from flask import request


# Initialize flask application
app_flask = flask.Flask(__name__)


# Define API route
@app_flask.route("/count-characters")
def count_characters(methods=['GET']):

	# Fetch query parameter from get request
	query_parameters = request.args
	string = query_parameters['string']

	# return length of the string
	return "{}".format(len(string))


@app_flask.route("/join-names")
def join_two_names(methods=['GET']):

	# Fetch query parameter from get request
	query_parameters = request.args
	first_name = query_parameters['fname']
	last_name = query_parameters['lname']

	return "{} - {}".format(first_name, last_name)


# Port number: 0 - 65535
# 0-1000 are system ports
# 22: SSH
# 80: HTTP
# 443: HTTPS


# Start server
app_flask.run(port=80)