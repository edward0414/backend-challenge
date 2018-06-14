### Set Up

Set up the environment by installing the packages in the requirements.txt file.
-> "pip install pymongo Flask" or "pip install -r requirements.txt"

Run the command "python app.py" in the command line. 

Then the server will be up and running on the localhost port 4000. 

The two endpoints "/messages" and "/conversations/<conversation_id>" will be available for services. Use them according to the readMe file!


### Test

Similar to how to run the main app.py file, run the command "python test.py" to test the endpoints.

Test cover:
1) correct behaviour of /conversations endpoint
2) incorrect behaviour of /conversations endpoint: not used conversation_id
3) incorrect behaviour of /conversations endpoint: incorrect parameter
4) correct behaviour of /messages endpoint
5) incorrect behaviour of /messages endpoint: missing field
6) incorrect behaviour of /messages endpoint: invalid conversation_id
7) correct process of creating a new conversation


### Database

It is a NoSQL database using MongoDB. Hosted on mlab.

Schema:

conversations
- id: String
- messages: [{
	sender: String,
	message: String,
	created: String
}]


### Feedback

It is a fun and short challenge! The whole challenge did not take me long to finish (less than 5 hours), but it is still a good way to see if people have a good understanding of databases and RESTful design. Though I prefer the challenge to be a bit more structure, this is perfectly fine.
