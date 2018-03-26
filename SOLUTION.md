### Set Up

Set up the environment by installing the packages in the requirements.txt file.
-> "pip install pymongo Flask" or "pip install -r requirements.txt"

Run the command "python app.py" in the command line. 

Then the server will be up and running on the localhost port 4000. 

The two endpoints "/messages" and "/conversations/<conversation_id>" will be available for services. Use them according to the readMe file!



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
