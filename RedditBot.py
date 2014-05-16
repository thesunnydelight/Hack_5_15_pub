"""
this bot is a novelty account where 30% of the time, it will respond to a look of disapproval unicode string (ಠ_ಠ).  It will search
   through the user's history to try to figure out the nationality and gender of the poster and reply with "an oriental man looks
   disapprovingly to a world of vile creatures"
"""

__author__ = 'ryan'

import time
import praw
import pprint

botUsername = "ttt123_bot"
password = "q2w3e4r"
botStompingGrounds = "testbot"
secondsToWaitBeforeNextRound = 15

def findCommentsToReplyTo():
    commentsToReplyList = {}
    subreddit = r.get_subreddit(botStompingGrounds)  # testing grounds for robot
    for submission in subreddit.get_hot(limit=20):
        flattenedComments = praw.helpers.flatten_tree(submission.comments)
        for comment in flattenedComments:
            #print(comment,)
            if str(comment.body).find("ಠ_ಠ") != -1:
                commentsToReplyList[comment.id] = comment.body
            elif str(comment.author).find(botUsername) != -1:
                adjustedParentID = comment.parent_id[comment.parent_id.find("_")+1:]
                if adjustedParentID in commentsToReplyList.keys():
                    del commentsToReplyList[adjustedParentID]
        for comment in flattenedComments:
            if comment.id in commentsToReplyList.keys():
                doSomethingUseful(comment)

def doSomethingUseful(comment):
    comment.reply("I found a look of disapproval!")
    print("adding comment",)

#  start here
pp = pprint.PrettyPrinter(indent=4)
print("*** Running Bot ***",)
r = praw.Reddit("look_bot v1.0 by /u/ttt123_bot")

rounds = 1
r.login(botUsername, password)
if r.is_logged_in():
    print("Login Successful")
else:
    print("Could not log in with supplied credentials, exiting program")
    exit(1)
while 1:
    print("running round " + str(rounds))
    findCommentsToReplyTo()
    rounds += 1
    time.sleep(secondsToWaitBeforeNextRound)
