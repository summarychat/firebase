
msge = "lolol this is so funny haha"

laugh_array = ['lo','lmao','rofl','ha']
day_array = ['mon','tue','wed','thurs','fri','day','th ','rd ']
month_array =['jan','feb','march','april','june','july','aug','sept','oct','nov']

def findLaughScore(msg):
        total=0
        for laugh in laugh_array:
                count = msg.count(laugh)
                total+=count
        return total

#Looks at chat log and searches for any strings containing the
#laugh array sub string. If yes, flags previous message and continues
#searching other messages for laughing sub strings
#If score is over the threshold, mark the flagged message as important
def findLaughter(chatLog):
        chatLog = chatLog.lower()
        chatLog = chatLog.splitlines()
        for i in range(1,len(chatLog),1):
                if findLaughScore(chatLog[i])>3:
                        prevMsg = chatLog[i-1]
                        if (len(chatLog)>=(i+3)):
                                total = 0
                                threshold = 7
                                for j in range(i,i+3,1):
                                        total+=findLaughScore(chatLog[j])
                                        if total>threshold:
                                                return prevMsg
                                        
def flagArray(chatLog,array):
        chatLog = chatLog.lower()
        chatLog = chatLog.splitlines()
        for lines in chatLog:
                for e in array:
                        if e in lines:
                                print lines



def getBoundID(msgID,maxID):
        if (msgID-5)<0:
                lowerbound = 0
        else:
                lowerbound = msgID-5
        if (msgID+5)>maxID:
                upperbound = maxID
        else:
                upperbound = msgID+5
        return upperbound,lowerbound


                                
                                
                                
                
