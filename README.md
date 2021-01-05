[![Documentation Status](https://readthedocs.org/projects/redditeasy/badge/?version=latest)](https://redditeasy.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/github/license/MakufonSkifto/redditeasy)](LICENSE.md)
[![GitHub stars](https://img.shields.io/github/stars/MakufonSkifto/redditeasy)](https://github.com/ExpDev07/coronavirus-tracker-api/stargazers) 
[![PyPI version](https://badge.fury.io/py/redditeasy.svg)](https://badge.fury.io/py/redditeasy)

# RedditEasy

RedditEasy is an API wrapper for the Reddit JSON API

## Install
To install RedditEasy, do:

``pip install redditeasy`` 

OR

``python -m pip install redditeasy``

## Documentation
Docs can be found [here](https://redditeasy.readthedocs.io/en/latest/)

## Usage
<span style="font-size:larger;">THE MODULE WILL USE ITS OWN DEFAULT CLIENT INFO IF **AT LEAST ONE** OF THESE ARE NOT GIVEN: `client_id=`, `client_secret`,
and `user_agent`.</span>

### Without client info
This method is not suggested as it may be slow and throw errors more often

```python
import redditeasy

post = redditeasy.Subreddit(subreddit="dankmemes")   #Subreddit name

postoutput = post.get_post()

print(f"Posts Title: {postoutput.title}\n"
      f"Posts Content: {postoutput.content}\n"
      f"Posts Author: u/{postoutput.author}\n"
      f"Posts URL: {postoutput.post_url}\n"
      f"Spoiler?: {postoutput.spoiler}\n"
      f"Post Created At: {postoutput.created_at}\n"
      f"Posts Upvote Count: {postoutput.score}\n"
      f"Posts Award Count: {postoutput.total_awards}\n"
      f"NSFW?: {postoutput.nsfw}\n"
      f"Post Flair: {postoutput.post_flair}\n"
      f"User Flair: {postoutput.author_flair}\n"
      f"Subreddit Subscribers: {postoutput.subreddit_subscribers}")

```

### With client info

```python
import redditeasy

"""
To get your client ID, client secret and user agent go to:
https://www.reddit.com/prefs/apps
and create an app
"""


post = redditeasy.Subreddit(subreddit="dankmemes",   #Subreddit name
                            client_id="",            #Your client ID
                            client_secret="",        #Your client secret
                            user_agent=""            #Your user agent (ex: ClientName/0.1 by YourUsername")
                            )

postoutput = post.get_post()

print(f"Posts Title: {postoutput.title}\n"
      f"Posts Content: {postoutput.content}\n"
      f"Posts Author: u/{postoutput.author}\n"
      f"Posts URL: {postoutput.post_url}\n"
      f"Spoiler?: {postoutput.spoiler}\n"
      f"Post Created At: {postoutput.created_at}\n"
      f"Posts Upvote Count: {postoutput.score}\n"
      f"Posts Award Count: {postoutput.total_awards}\n"
      f"NSFW?: {postoutput.nsfw}\n"
      f"Post Flair: {postoutput.post_flair}\n"
      f"User Flair: {postoutput.author_flair}\n"
      f"Subreddit Subscribers: {postoutput.subreddit_subscribers}")

```


More examples are in the [examples folder](https://github.com/MakufonSkifto/RedditEasy/tree/main/examples)

## Errors

The module will raise ``KeyError`` if the given user / subreddit is not found

The module will raise ``redditeasy.exceptions.RequestError``  if there was an error with the request. Traceback will show the details about the error