# -*- coding: utf-8 -*-
"""
@author: Dhruv
"""
from slackclient import SlackClient
import os
SLACK_BOT_TOKEN='xoxb-142362592149-529719120663-YcciJl4y65e3CkcIOOcnUxGt'
sc = SlackClient(SLACK_BOT_TOKEN)

sc.api_call(
  "chat.postMessage",
  channel="", #Set UserId Here
  text="Testing Purpose From Dhruv",
  as_user=True
)
print("done")
