import praw
import pdb
import re
import os
from config_skel import *
import obot

if not os.path.isfile('posts_replied_to.txt'):
    posts_replied_to = []
else:
    with open('posts_replied_to.txt','r') as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split('\n')
        posts_replied_to = filter(None, posts_replied_to)

already_done = []

r = obot.login()

subreddit = r.get_subreddit('test')
subreddit_comments = subreddit.get_comments()


def hl4_bot():
    for comment in subreddit_comments:
        if 'half life 4' in comment.body.lower() and comment.id not in already_done:

            try:
                cauthor = comment.author.name
                if cauthor.lower() != REDDIT_USERNAME.lower():
                    count += 1
                    comment.reply('Thanks for mentioning it, kid! It will now be released %r month(s) after Half Life 3\n>I am an automatic bot, for questions ask or PM /u/shows7' % count) 
                    posts_replied_to.append(comment.id)
                    already_done.append(comment.id)
                    print('Commented in thread %s times') % count

            except:
                print('Something went wrong.')
    
    
    with open('posts_replied_to.txt','w') as f:
        for post_id in posts_replied_to:
            f.write(post_id + '\n')


while 1 < 2:
    hl4_bot()
  
