Functions
=========================================

A List of Classes
-----------------

.. code-block::
  :linenos:

  Subreddit()

* Parameter: subreddit (str) - The name of the subreddit

.. code-block::
  :linenos:

  User()

* Parameter: user (str) - The name of the user

class: Subreddit()
---------------------

.. code-block::
  :linenos:

  get_image()

* Parameter: None

* Returns: (str) Post content of the randomly selected post from the subreddit

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

   ``pinned``: This will return True or False if the post is pinned or not

   ``created_at``: The time the randomly selected post got created

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

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

   ``pinned``: This will return True or False if the post is pinned or not

   ``created_at``: The time the randomly selected post got created

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not



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

   ``pinned``: This will return True or False if the post is pinned or not

   ``created_at``: The time the randomly selected post got created

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not


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

   ``pinned``: This will return True or False if the post is pinned or not

   ``created_at``: The time the randomly selected post got created

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not



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

   ``pinned``: This will return True or False if the post is pinned or not

   ``created_at``: The time the randomly selected post got created

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not



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

   ``pinned``: This will return True or False if the post is pinned or not

   ``created_at``: The time the randomly selected post got created

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not
