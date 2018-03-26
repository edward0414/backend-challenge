#use Flask framework
#use mongodb as Database
#set up the environment using anaconda
from flask import Flask, request, jsonify
from datetime import datetime
from pymongo import MongoClient

# create the application object
app = Flask(__name__)

#it would be a better idea to save the credentials as environmental secret keys for better security!
#but just for the person to run the code, i will leave it as this
client = MongoClient('mongodb://edward:123456@ds147377.mlab.com:47377/ada_challenge') 

db = client['ada_challenge']

table = db['conversations']


#To-Do:
#-Post to /messages (sender, conversation_id, message)
#	-> validating incoming data (check if its the right format)
#	-> insert to the db according to the conversation_id
#-Get to /conversations/<conversation_id>
#	-> validating incoming id
#	-> query the db


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

			if result is None:
				conv = {
					"id": request.args['conversation_id'], 
					"messages":[
						msg
					]
				}
				table.insert_one(conv)

			else:
				result['messages'].append(msg)
				table.update(query, {'$set': {"messages": result['messages']}})

	resp = jsonify(resp)
	resp.status_code = 201

	return resp

@app.route('/conversations/<conversation_id>')
def conversations(conversation_id):

	conversation_id = str(conversation_id) #to cover the case where the user throw in an integer

	resp = {"id": conversation_id, "messages": "Error: No conversation has started with this id!"}

	query = {"id": conversation_id}

	result = table.find_one(query)
	print "result: ", result

	if result is not None:
		resp['messages'] = result['messages']
		return jsonify(resp)

	else:
		resp = jsonify(resp)
		resp.status_code = 404

		return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4000)
