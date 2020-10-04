# -*- coding: utf-8 -*-
"""
@author: Dhruv
"""

import os
import time
import re
from slackclient import SlackClient


SLACK_BOT_TOKEN=''#Set SlackBot Token Here
# instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN)
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            #user_id=UFKM53JKH
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    # ByDesault Passing a bot`s ID When u are DM..... DHRUV
    if '@' not in message_text:
        message_modified='<@UFKM53JKH> '+message_text 
        print('',message_modified)
        matches = re.search(MENTION_REGEX, message_modified)
    #IF you are messaging from Channel then it will already have bot`s ID.......DHRUV
    else:
        matches = re.search(MENTION_REGEX, message_text)
        print('Msg:-',message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)


def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """
    if command=="hello" or command=="hi" or command=="Hello" or command=="Hi" :
        response = "I am Wonderful, What About You?".format(EXAMPLE_COMMAND)

    elif command== command.startswith('do'):
        response = "Sure...write some more code then I can do that!"
    else:
        # Default response is help text for the user
        response = "I am Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

    # Finds and executes the given command, filling in response
#    response = None

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]

	
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(1)
    else:
        print("Connection failed. Exception traceback printed above.")
