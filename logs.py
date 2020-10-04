# -*- coding: utf-8 -*-
"""
@author: Dhruv
"""
import datetime
import os
import csv

now=datetime.datetime.now()
CurrentMonth = now.month
CurrentYear = now.year
FILE_NAME_EXTEND=str(CurrentMonth)+'_' +str(CurrentYear)

FOLDER_PATH='SlackLogs/'
def LogOfMessage(userId,response,messageIn):
#    NameFromId=NameFromUserId(userId)
#    filename ='Message_'+FILE_NAME_EXTEND
    filename =FOLDER_PATH+'Message_'+FILE_NAME_EXTEND
    file_exists = os.path.isfile('{0}.csv'.format(filename))

    with open(r'{0}.csv'.format(filename),'a',newline='') as f:
       header=['Date', 'Hour','Minute', 'UserId', 'MessageIn', 'MessageOut']
       writer = csv.DictWriter(f, fieldnames = header)
       if(file_exists == False):
            writer.writeheader()
            
       writer.writerow({'Date': now.date(), 'Hour': now.hour,'Minute': now.minute,'UserId':userId, 'MessageIn':messageIn, 'MessageOut':response}) 
       file_exists=True
#       print(now.hour, now.minute)
       
def ErrorLog(EXCEPTION_MESSAGE):
#    print(EXCEPTION_MESSAGE)
    filename =FOLDER_PATH+'Log_'+FILE_NAME_EXTEND
#    filename ='Log_'+FILE_NAME_EXTEND
    with open(filename+'.txt', "w") as file:
        file.write(str(EXCEPTION_MESSAGE))
