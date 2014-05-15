__author__ = 'ryan'

import time
import praw
import pprint

"""
def findCommentsToReplyTo:
    return
def doSomethingUseful:
    return
"""
target_username = 'blehbleh3213'
pp = pprint.PrettyPrinter(indent=4)

print("*** Running Hot Or Not Reddit Bot ***",)
r = praw.Reddit("hot or not bot v1.0 by /u/hot_or_not_bot")
username = "hot_or_not_bot"
password = "Le37z%*5%O"
rounds = 1
r.login(username, password)
if r.is_logged_in():
    print("Login Successful")
else:
    print("Could not log in with supplied credentials, exiting program")
    exit(1)
running = True
while running:
    print("running round " + str(rounds))
    commentsToReplyList = {}
    subreddit = r.get_subreddit('testbot')  # testing grounds for robot
    for submission in subreddit.get_hot(limit=20):
        if str(submission.author).find(username) != -1:
            flattenedComments = praw.helpers.flatten_tree(submission.comments)
            for comment in flattenedComments:
                #print(comment,)
                if str(comment.author).find(target_username) != -1:
                    commentsToReplyList[comment.id] = comment.body
                elif str(comment.author).find(username) != -1:
                    adjustedParentID = comment.parent_id[comment.parent_id.find("_")+1:]
                    if adjustedParentID in commentsToReplyList.keys():
                        del commentsToReplyList[adjustedParentID]
            for comment in flattenedComments:
                if comment.id in commentsToReplyList.keys():
                    comment.reply("I found you " + target_username + "!")
                    print("adding comment",)
    rounds += 1
    time.sleep(15) # qwer
"""
for dictKey in commentsToReplyList.keys():
    print(dictKey, commentsToReplyList[dictKey])
    r.get_info(thing_id=comment_id)
"""

#commentsToReplyList.append(comment.parent_id)
            #pp.pprint(vars(comment))
        #pp.pprint(vars(submission))
        #submissionComments = submission.comments

#r.send_message('swordo', 'test PM', 'waka')


#submission.add_comment('text')

#comment = submission.comments[0]
#comment.reply('test')

#item.upvote()
#item.downvote()
#item.clear_vote()
"""
for submission in subreddit.get_hot(limit=20):
    print(submission,)
    pp.pprint(vars(submission))
        # Test if it contains a PRAW-related question
"""

"""
user = r.get_redditor(username)

limit = 70
gen = user.get_comments(limit)
for thing in gen:
    print("subreddit: ", thing.subreddit.display_name,)
    print("message: ", thing,)
"""