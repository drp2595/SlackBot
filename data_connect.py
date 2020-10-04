# -*- coding: utf-8 -*-
"""
@author: Dhruv
"""
import pyodbc
import datetime
from logs import *
import sys

CURRENT=datetime.datetime.now()
CURRENT_DATE=CURRENT.day
CURRENT_MONTH=CURRENT.month
CURRENT_YEAR=CURRENT.year
NAME_LIST=[]
NAME_OF_BIRTHDAY=""
NAME_OF_JOINY=""
EXCEPTION_MESSAGE=''

#DB Details
SERVAER_NAME = 'DESKTOP'
DATABASE_NAME = 'Slack'
SERVER_USERNAME = 'sa'
SERVER_PASSWORD = '' #Need to pass Password
MSSQL_DRIVER= '{SQL Server Native Client 11.0}'



userName=[]

def TodayBirthDay():
    birthDay=[]
    NAME_OF_BIRTHDAY=''
    try:
        cnxn = pyodbc.connect('DRIVER='+MSSQL_DRIVER+';SERVER='+SERVAER_NAME+';PORT=1433;DATABASE='+DATABASE_NAME+';UID='+SERVER_USERNAME+';PWD='+ SERVER_PASSWORD)
        cursor = cnxn.cursor()
        cursor.execute("SELECT FirstName FROM dbo.Employee WHERE DAY(DateOfBirth) = ? AND MONTH(DateOfBirth) = ?",(CURRENT_DATE,CURRENT_MONTH))
        for name in cursor:
        	birthDay=",".join(name) #this statement will cut comma/bracket/spaces and give filtered result use with STRING ONLY
        	
        if birthDay!=[]:
            NAME_OF_BIRTHDAY="This Persons have Bday today:-",birthDay
        else:
        	NAME_OF_BIRTHDAY="Sorry no one have Bday Today"
        cursor.close()
        cnxn.close()
    except:
        EXCEPTION_MESSAGE='InBirthday:'+str(sys.exc_info()[0])
        ErrorLog(EXCEPTION_MESSAGE)
        NAME_OF_BIRTHDAY='Something Going Wrong!'
    return NAME_OF_BIRTHDAY

def TodayJoiny():
    joinDay=[]
    NAME_OF_JOINY=''
    try:
        cnxn = pyodbc.connect('DRIVER='+MSSQL_DRIVER+';SERVER='+SERVAER_NAME+';PORT=1433;DATABASE='+DATABASE_NAME+';UID='+SERVER_USERNAME+';PWD='+ SERVER_PASSWORD)
        cursor = cnxn.cursor()
        cursor.execute("SELECT FirstName FROM dbo.Employee WHERE DAY(DateOfJoin) = ? AND MONTH(DateOfJoin) = ?",(CURRENT_DATE,CURRENT_MONTH))
        for name in cursor:
        	joinDay=",".join(name) #this statement will cut comma/bracket/spaces and give filtered result use with STRING ONLY
        	
        if joinDay!=[]:
            NAME_OF_JOINY="This Persons joins today:-",joinDay
        else:
        	NAME_OF_JOINY="Sorry no one join Today"
        cursor.close()
        cnxn.close
    except:
        EXCEPTION_MESSAGE='InJoiny:'+str(sys.exc_info()[0])
        ErrorLog(EXCEPTION_MESSAGE)
        NAME_OF_JOINY='Something Going Wrong!'
    return NAME_OF_JOINY

def NameFromUserId(userId): 
#    print("hi")
    try:
        cnxn = pyodbc.connect('DRIVER='+MSSQL_DRIVER+';SERVER='+SERVAER_NAME+';PORT=1433;DATABASE='+DATABASE_NAME+';UID='+SERVER_USERNAME+';PWD='+ SERVER_PASSWORD)
        cursor = cnxn.cursor()
        cursor.execute("SELECT FirstName FROM dbo.Employee WHERE SlackId = '?'",(userId))
        print("SELECT FirstName FROM dbo.Employee WHERE SlackId =",(userId))
        for name in cursor:
            print("hello")
#            userName=",".join(name) #this statement will cut comma/bracket/spaces and give filtered result use with STRING ONLY
#        if userName!=[]:
#            return userName
#        else:
#            print("No User Found")
        cursor.close()
        cnxn.close
    except:
        EXCEPTION_MESSAGE='InUserNameFound:'+str(sys.exc_info()[0])
        ErrorLog(EXCEPTION_MESSAGE)
        
#def main():
#    named=NameFromUserId(userId)
#    print(named)
#    
#if __name__== "__main__" :
#     main()
