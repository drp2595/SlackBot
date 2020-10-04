# -*- coding: utf-8 -*-
"""
@author: Dhruv
"""

import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
from data_connect import *
import random
import os
import sys
import time
import re
from slackclient import SlackClient

today_birthday="".join(NAME_OF_BIRTHDAY)
today_joiny="".join(NAME_OF_JOINY)

SLACK_BOT_TOKEN='xoxb-142362592149-529719120663-YcciJl4y65e3CkcIOOcnUxGt'
slack_client = SlackClient(SLACK_BOT_TOKEN)
starterbot_id = slack_client.api_call("auth.test")["user_id"]

# constants
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        self.main()

nameIn=['Who are you','who are you','Who are you?','who are you?','What is your name','Whats ur name','what is your name?','whats ur name?']
nameOut=['My Name is StarterBot','I am StarterBot','My Self StarterBot']

gritIn=['Hi','hi','hlw','Hlw','Hello','hello','Hellow','hellow']
gritOut=['Hey! Hi There','Hellow','Hi!!']

byeIn=['bye','Bye']
byeOut=['B bye','Bye','Wish you a Great time','Thanks Meeting You']

birthIn=['Today`s Birthday','Birthday Today','Birthday','birthday','who have birthday today?','Who Have Birthday Today?','Who have Birthday today?']
joinIn=['Today`s joiny','join Today','Join','join','who join today?','Who Join Today?']

alrightIn=['How are you','how are you','How are you?','how are you?']
alrightOut=['I am Good, What About You','I am Wonderul ;-)']

helpIn=['help','Help','help me','Help me','help Me','Help Me']
helpOut=['How may I Help you?']

def parse_bot_commands(slack_events):
    
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            #user_id=UFKM53JKH
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    
    if '@' not in message_text:
        message_modified='<@UFKM53JKH> '+message_text 
        print('Msg:-',message_text)
        matches = re.search(MENTION_REGEX, message_modified)
    
    else:
        matches = re.search(MENTION_REGEX, message_text)
        print('Msg:-',message_text)
    
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    response=''

    if command in gritIn:
        response=random.choice(gritOut)
    
    elif command in nameIn:
        response=random.choice(nameOut)

    elif command in byeIn:
        response=random.choice(byeOut)

    elif command in birthIn:
        response=today_birthday    
        
    elif command in joinIn:
        response=today_joiny
        
    elif command in helpIn:
        response=random.choice(helpOut)
    else:
        response="I am sorry, I am currently under Operation. but as soon as possible i will be well"
        
    slack_client.api_call("chat.postMessage",
        channel=channel,
        text=response
        )



    def main(self):
            if slack_client.rtm_connect(with_team_state=False):
                print("Starter Bot connected and running!")
        
            #starterbot_id = slack_client.api_call("auth.test")["user_id"]
    
                while True:
                    command, channel = parse_bot_commands(slack_client.rtm_read())
                    if command:
                        handle_command(command, channel)
                    time.sleep(1)
            else:
                print("Connection failed. Exception traceback printed above.")


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)