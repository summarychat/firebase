from firebase import firebase
import json

firebase = firebase.FirebaseApplication('https://hackthenorthproj.firebaseio.com/')
#result = firebase.post('/Chatroom/Messages',{'Msg':'hello world','Name':'Jon','Time':'234342'})
result = firebase.get('/Chatroom/Messages',None)
result=json.dumps(result)
print result
dic = json.loads(result)
print dic[dic.keys()[1]]
