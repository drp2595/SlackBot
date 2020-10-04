# -*- coding: utf-8 -*-
"""
@author: Dhruv
"""
from messages import *
from logs import *
import time
import datetime
import re
from slackclient import SlackClient

# constants
SLACK_BOT_TOKEN='xoxb-142362592149-529719120663-YcciJl4y65e3CkcIOOcnUxGt'
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
HR_CHANNLE='UC328QS0K' #need to change with Hr`s SlackId


slack_client = SlackClient(SLACK_BOT_TOKEN)
starterbot_id = slack_client.api_call("auth.test")["user_id"]


def parse_bot_commands(slack_events):
    
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
#            user_id=UFKM53JKH
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    
    if '@' not in message_text:
        message_modified='<@UFKM53JKH> '+message_text 
#        print('Msg:-',message_text)
        matches = re.search(MENTION_REGEX, message_modified)
    
    else:
        matches = re.search(MENTION_REGEX, message_text)
#        print('Msg:-',message_text)
    
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    response=ResponseCommand(command)
#    print("Res",response)
    slack_client.api_call("chat.postMessage",
        channel=channel,
        text=response
        )
    LogOfMessage(channel,response,command)

if __name__ == "__main__":
#def connect():
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
    
#        starterbot_id = slack_client.api_call("auth.test")["user_id"]

    
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
#                print(channel)
            now = datetime.datetime.now()
#            print(now.minute)
            if (now.hour==12) and (now.minute==00) and (now.second==00):
                BirthCommand='Birthday Today'
                handle_command(BirthCommand,HR_CHANNLE)
            if (now.hour==12) and (now.minute==00) and (now.second==10):
                JoinCommand='join Today'
                handle_command(JoinCommand,HR_CHANNLE)

            time.sleep(1)
    else:
        print("Connection failed. Exception traceback printed above.")
