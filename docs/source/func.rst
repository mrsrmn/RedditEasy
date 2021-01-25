Functions
=========================================

A List of Classes
-----------------

.. code-block::
  :linenos:

  Subreddit()

* Parameter: subreddit (str) - The name of the subreddit
* Parameter: client_id (str, Optional) - Your client ID
* Parameter: client_secret (str, Optional) - Your client secret
* Parameter: user_agent (str, Optional) - Your user agent

.. code-block::
  :linenos:

  User()

* Parameter: user (str) - The name of the user
* Parameter: client_id (str, Optional) - Your client ID
* Parameter: client_secret (str, Optional) - Your client secret
* Parameter: user_agent (str, Optional) - Your user agent


THE MODULE WILL USE ITS OWN DEFAULT CLIENT INFO IF **AT LEAST ONE** OF THESE ARE NOT GIVEN: ``client_id=``, ``client_secret``,
and ``user_agent``.

To get your client ID, client secret and user agent go to:
https://www.reddit.com/prefs/apps
and create an app

For more detailed explanation, see this image: https://i.imgur.com/Ri13AQu.png


class: Subreddit()
---------------------


.. code-block::
  :linenos:

  get_post()

* Parameter: None

* Returns: (str) Info about the randomly selected post from the subreddit

* Attributes:

   ``content``: The content of the randomly selected post

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair 

   ``subreddit_subscribers`` The number of people in the subreddit

.. code-block::
  :linenos:

  get_new_post()

* Parameter: None

* Returns: (str) Info about the randomly selected post (new)

* Attributes:

   ``content``: The content of the randomly selected post

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair 

   ``subreddit_subscribers`` The number of people in the subreddit



.. code-block::
  :linenos:

  get_controversial_post()

* Parameter: None

* Returns: (str) Info about the randomly selected post (new)

* Attributes:

   ``content``: The content of the randomly selected post

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair 

   ``subreddit_subscribers`` The number of people in the subreddit


class: User()
---------------------

.. code-block::
  :linenos:

  get_post()

* Parameter: None

* Returns: (str) Info about the randomly selected post from the user

* Attributes:

   ``content``: The content of the randomly selected post

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair 



.. code-block::
  :linenos:

  get_new_post()

* Parameter: None

* Returns: (str) Info about the randomly selected post (new)

* Attributes:

   ``content``: The content of the randomly selected post

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair 



.. code-block::
  :linenos:

  get_controversial_post()

* Parameter: None

* Returns: (str) Info about the randomly selected post (new)

* Attributes:

   ``content``: The content of the randomly selected post

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair 
