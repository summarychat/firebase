from firebase import firebase
import json
import time

firebase = firebase.FirebaseApplication('https://hackthenorthproj.firebaseio.com/')

#Creates a chatroom with a first default message
def create_chatroom(chatroom,user):
        default_msg = "This is your first message!"
        res = json_str(default_msg,user)
        return firebase.post('/'+chatroom+'/Messages',json.loads(res))

#Posts a message to the specified chatroom on Firebase
def post_message(chatroom,sender,msg_content):
        unix_timestamp = int(time.time())
        res = json_str(msg_content,sender)
        return firebase.post('/'+chatroom+'/Messages',json.loads(res))

#Returns a JSON string containing the message content, sender name, and 
#unix timestamp
def json_str(msg,sender):
        unix_timestamp = int(time.time())
        data = {'Msg':msg,'Name':sender,'Time':unix_timestamp}
        return json.dumps(data)

#Rettrieves all messages in a chatroom
def get_messages(chatroom):
        res = firebase.get('/'+chatroom+'/Messages',None)
        return json.dumps(res)

