Getting Started
======================================

Install
-------------
To install RedditEasy, do:

``pip install redditeasy``

OR

``python -m pip install redditeasy``

Documentation
-------------
Docs can be found [here]()

Usage
-------------

.. code-block:: python
  :linenos:

  import redditeasy

  post = redditeasy.Subreddit("memes")
  postoutput = post.get_post()

  print(f"Posts Title: {postoutput.title}\n"
        f"Posts Content: {postoutput.content}\n"
        f"Posts Author: u/{postoutput.author}\n"
        f"Posts URL: {postoutput.post_url}\n"
        f"Spoiler?: {postoutput.spoiler}\n"
        f"Post Created At: {postoutput.created_at}\n"
        f"Posts Upvote Count: {postoutput.score}\n"
        f"Posts Award Count: {postoutput.total_awards}\n"
        f"NSFW?: {postoutput.nsfw}")


More examples are in the `examples folder <https://github.com/MakufonSkifto/RedditEasy/tree/main/examples>`_

Errors
-------------
The module will raise ``KeyError`` if the given user / subreddit is not found