#use flask
#use mongodb
#set up the environment using anaconda
from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify, make_response
from pymongo import MongoClient

client = MongoClient('mongodb://edward:123456@ds221609.mlab.com:21609/')
db = client['conversations']



#To-Do:
#-Post to /messages (sender, conversation_id, message)
#-Get to /conversations/<conversation_id>
#-Validating incoming data (to post)
#-Some test cases
