#use flask
#use mongodb
#set up the environment using anaconda
from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify, make_response
from datetime import datetime
from pymongo import MongoClient

# create the application object
app = Flask(__name__)

client = MongoClient('mongodb://edward:123456@ds147377.mlab.com:47377/ada_challenge')
db = client['ada_challenge']

table = db['conversations']



# * request.get_json()
#To-Do:
#-Post to /messages (sender, conversation_id, message)
#	-> validating incoming data (check if its the right format)
#	-> insert to the db according to the conversation_id
#-Get to /conversations/<conversation_id>
#	-> validating incoming id
#	-> query the db
#-Some test cases


@app.route('/messages', methods=['GET', 'POST'])
def messages():

	resp = {"successful": False, "message": "Usage: sender, conversation_id, message"}
	
	if request.method == 'POST':

		if "sender" in request.args and "conversation_id" in request.args and "message" in request.args:
			resp["successful"] = True

			msg = {
			"sender": request.args['sender'],
			"message": request.args['message'],
			"created": datetime.utcnow()
			}

			resp["message"] = msg

			query = {"id": request.args['conversation_id']}
			result = table.find_one(query)
			print "result", result

			if result is None:
				print "here"
				conv = {
				"id": request.args['conversation_id'], 
				"messages":[
					msg
				]}
				table.insert_one(conv)

			else:
				result['messages'].append(msg)
				table.update(query, {'$set': {"messages": result['messages']}})

	return jsonify(resp)

@app.route('/conversations/<conversation_id>', methods=['GET', 'POST'])
def conversations(conversation_id):

	return "jsonify"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4000)
