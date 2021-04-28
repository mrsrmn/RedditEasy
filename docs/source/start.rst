Getting Started
======================================

Install
-------------
To install RedditEasy, do:

``pip install redditeasy``

OR

``python -m pip install redditeasy``


Async RedditEasy
-----------------
Yes, there is an async version of RedditEasy. To use it, you need to use the Async classes. Which are ``AsyncSubreddit`` and ``AsyncUser``

Here is a small example on using ``AsyncSubreddit``: https://github.com/MakufonSkifto/RedditEasy/blob/main/examples/async_meme.py

You can and should use this in a discord.py bot. The normal classes could cause a `blocking <https://discordpy.readthedocs.io/en/latest/faq.html#what-does-blocking-mean>`_ in an async program.

This **will not** work outside an async function whatsoever.

Usage
-------------

The module will use its own default client info if **AT LEAST ONE** of these are not given: ``client_id``, ``client_secret`` and ``user_agent``.


Without client info
''''''''''''''''''''''''''''''''''
This method is not suggested as it may be slow and throw errors more often

.. code-block:: python
  :linenos:

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
        f"Subreddit Subscribers: {postoutput.subreddit_subscribers}\n"
        f"Comment count: {postoutput.comment_count}\n"
        f"Is Media?: {postoutput.is_media}\n"
        f"Subreddit Name: {postoutput.subreddit_name}")


With client info
''''''''''''''''''''''''''''''''''
.. code-block:: python
  :linenos:

  import redditeasy

  # To get your Reddit API client info go to
  # https://www.reddit.com/prefs/apps
  # and create an app

  # For more detailed explanation, see this image: https://i.imgur.com/Ri13AQu.png

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
        f"Subreddit Subscribers: {postoutput.subreddit_subscribers}\n"
        f"Comment count: {postoutput.comment_count}\n"
        f"Is Media?: {postoutput.is_media}\n"
        f"Subreddit Name: {postoutput.subreddit_name}")


More examples are in the `examples folder <https://github.com/MakufonSkifto/RedditEasy/tree/main/examples>`_


Getting Reddit API Client info
------------------------------------------

To get your Reddit API client info go to
https://www.reddit.com/prefs/apps
and create a script.

.. image:: https://i.imgur.com/Ri13AQu.png
  :width: 400
  :alt: Alternative text

(You don't have to fill "redirect_uri")

Operating Systems
-------------

All of RedditEasy's versions were tested in ``Windows``, ``Linux (Ubuntu)`` and ``MacOS``

Errors
-------------
The module will raise ``KeyError`` if the given user / subreddit is not found

The module will raise ``redditeasy.exceptions.RequestError`` if there was an error with the request. Traceback will show the details about the error

The module will raise ``ValueError`` if the given user / subreddit is empty