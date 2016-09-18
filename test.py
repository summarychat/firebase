from firebase import firebase
import json

firebase = firebase.FirebaseApplication('https://travel-bugg.firebaseio.com/')
#result = firebase.post('/Chatroom/Messages',{'Msg':'hello world','Name':'Jon','Time':'234342'})
result = firebase.get('/User',None)
result=json.dumps(result)
print result

