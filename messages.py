# -*- coding: utf-8 -*-
"""
@author: Dhruv
"""
import random
from data_connect import *

#Messages In & Out
nameIn=['Who are you','who are you','Who are you?','who are you?','What is your name','Whats ur name','what is your name?','whats ur name?']
nameOut=['My Name is StarterBot','I am StarterBot','My Self StarterBot']

alrightIn=['How are you','how are you','How are you?','how are you?']
alrightOut=['I am Good, What About You','I am Wonderul ;-)']

gritIn=['Hi','hi','hlw','Hlw','Hello','hello','Hellow','hellow']
gritOut=['Hey! Hi There','Hellow','Hi!!']

byeIn=['bye','Bye']
byeOut=['B bye','Bye','Wish you a Great time','Thanks Meeting You']

birthIn=['Today`s Birthday','Birthday Today','Birthday','birthday','who have birthday today?','Who Have Birthday Today?','Who have Birthday today?']
joinIn=['Today`s joiny','join Today','Join','join','who join today?','Who Join Today?','joiny','Joiny']

helpIn=['help','Help','help me','Help me','help Me','Help Me']
helpOut=['How may I Help you?']
#Messages In & Out

def ResponseCommand(command):
    if command in gritIn:
        response=random.choice(gritOut)
    
    elif command in nameIn:
        response=random.choice(nameOut)

    elif command in byeIn:
        response=random.choice(byeOut)

    elif command in birthIn:
        response=TodayBirthDay()    
        
    elif command in joinIn:
        response=TodayJoiny()
        
    elif command in helpIn:
        response=random.choice(helpOut)
        
    elif command in alrightIn:
        response=random.choice(alrightOut)
        
    else:
        response="I am sorry, I am currently under Operation. but as soon as possible i will be well"
    
    return response