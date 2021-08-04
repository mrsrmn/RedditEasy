Functions
=========================================

A List of Classes
-----------------


Subreddit() / AsyncSubreddit()
''''''''''''''''''''''''''''''''''

This class is for getting posts from a subreddit

* Parameter: client_id (str, Optional) - Your client ID
* Parameter: client_secret (str, Optional) - Your client secret
* Parameter: user_agent (str, Optional) - Your user agent


.. raw:: html

   <hr>

User() / AsyncUser()
''''''''''''''''''''''''''''''''''

This class is for getting posts from a user

* Parameter: client_id (str, Optional) - Your client ID
* Parameter: client_secret (str, Optional) - Your client secret
* Parameter: user_agent (str, Optional) - Your user agent


.. raw:: html

   <hr>


class: Subreddit() / AsyncSubreddit()
--------------------------------------


``get_post()``
''''''''''''''''''''''''''''''''''

* Parameter: subreddit (str) - The name of the subreddit

* Returns: (str) Info about the randomly selected post from the subreddit

* Attributes:

   ``content``: The content of the randomly selected post (Returns a JSON dict if the ``content_type`` is "Gallery")

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created in UTC (epoch)

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair 

   ``subreddit_subscribers`` The number of people in the subreddit

   ``comment_count`` The number comments in the post

   ``is_media`` This will return True or False if the post has some kind of media in it or not

   ``subreddit_name`` This will return the subreddit name

   ``content_type`` This will return the posts content type. Types are: "Image", "Video", "Text", "URL" and "Gallery"


.. raw:: html

   <hr>

``get_new_post()``
''''''''''''''''''''''''''''''''''

* Parameter: subreddit (str) - The name of the subreddit

* Returns: (str) Info about the randomly selected post from the subreddit (new)

* Attributes:

   ``content``: The content of the randomly selected post (Returns a JSON dict if the ``content_type`` is "Gallery")

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created in UTC (epoch)

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair 

   ``subreddit_subscribers`` The number of people in the subreddit

   ``comment_count`` The number comments in the post

   ``is_media`` This will return True or False if the post has some kind of media in it or not

   ``subreddit_name`` This will return the subreddit name

   ``content_type`` This will return the posts content type. Types are: "Image", "Video", "Text", "URL" and "Gallery"


.. raw:: html

   <hr>


``get_top_post()``
''''''''''''''''''''''''''''''''''

* Parameter: subreddit (str) - The name of the subreddit

* Returns: (str) Info about the randomly selected post from the subreddit (This will return the TOP POST OF TODAY)

* Attributes:

   ``content``: The content of the randomly selected post (Returns a JSON dict if the ``content_type`` is "Gallery")

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created in UTC (epoch)

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair

   ``subreddit_subscribers`` The number of people in the subreddit

   ``comment_count`` The number comments in the post

   ``is_media`` This will return True or False if the post has some kind of media in it or not

   ``subreddit_name`` This will return the subreddit name

   ``content_type`` This will return the posts content type. Types are: "Image", "Video", "Text", "URL" and "Gallery"


.. raw:: html

   <hr>

``get_controversial_post()``
''''''''''''''''''''''''''''''''''

* Parameter: subreddit (str) - The name of the subreddit

* Returns: (str) Info about the randomly selected post from the subreddit (controversial)

* Attributes:

   ``content``: The content of the randomly selected post (Returns a JSON dict if the ``content_type`` is "Gallery")

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created in UTC (epoch)

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair 

   ``subreddit_subscribers`` The number of people in the subreddit

   ``comment_count`` The number comments in the post

   ``is_media`` This will return True or False if the post has some kind of media in it or not

   ``subreddit_name`` This will return the subreddit name

   ``content_type`` This will return the posts content type. Types are: "Image", "Video", "Text", "URL" and "Gallery"


.. raw:: html

   <hr>

class: User() / AsyncUser()
-----------------------------

``get_post()``
''''''''''''''''''''''''''''''''''

* Parameter: user (str) - The name of the user

* Returns: (str) Info about the randomly selected post from the user

* Attributes:

   ``content``: The content of the randomly selected post (Returns a JSON dict if the ``content_type`` is "Gallery")

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created in UTC (epoch)

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair 

   ``comment_count`` The number comments in the post

   ``is_media`` This will return True or False if the post has some kind of media in it or not

   ``content_type`` This will return the posts content type. Types are: "Image", "Video", "Text", "URL" and "Gallery"


.. raw:: html

   <hr>

``get_new_post()``
''''''''''''''''''''''''''''''''''

* Parameter: user (str) - The name of the user

* Returns: (str) Info about the randomly selected post from the user (new)

* Attributes:

   ``content``: The content of the randomly selected post (Returns a JSON dict if the ``content_type`` is "Gallery")

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created in UTC (epoch)

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair

   ``comment_count`` The number comments in the post

   ``is_media`` This will return True or False if the post has some kind of media in it or not

   ``content_type`` This will return the posts content type. Types are: "Image", "Video", "Text", "URL" and "Gallery"


.. raw:: html

   <hr>

``get_top_post()``
''''''''''''''''''''''''''''''''''

* Parameter: user (str) - The name of the user

* Returns: (str) Info about the randomly selected post from the user (This will return the TOP POST OF TODAY)

* Attributes:

   ``content``: The content of the randomly selected post (Returns a JSON dict if the ``content_type`` is "Gallery")

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created in UTC (epoch)

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair

   ``comment_count`` The number comments in the post

   ``is_media`` This will return True or False if the post has some kind of media in it or not

   ``content_type`` This will return the posts content type. Types are: "Image", "Video", "Text", "URL" and "Gallery"


.. raw:: html

   <hr>

``get_controversial_post()``
''''''''''''''''''''''''''''''''''

* Parameter: user (str) - The name of the user

* Returns: (str) Info about the randomly selected post from the user (controversial)

* Attributes:

   ``content``: The content of the randomly selected post (Returns a JSON dict if the ``content_type`` is "Gallery")

   ``title``: The title of the randomly selected post

   ``upvote_ratio``: The upvote ratio of the randomly selected post

   ``total_awards``: The number of awards in the randomly selected post

   ``score``: The upvote count of the randomly selected post

   ``downvotes``: The downvote count of the randomly selected post

   ``nsfw``: This will return True or False if the post is NSFW or not

   ``created_at``: The time the randomly selected post got created in UTC (epoch)

   ``author``: The author of the randomly selected post

   ``post_url``: The URL to the randomly selected post

   ``stickied``: This will return True or False if the post is stickied or not

   ``spoiler``: This will return True or False if the post is spoiler or not

   ``post_flair``: This will return the post's flair

   ``author_flair``: This will return the post's author's flair

   ``comment_count`` The number comments in the post

   ``is_media`` This will return True or False if the post has some kind of media in it or not

   ``content_type`` This will return the posts content type. Types are: "Image", "Video", "Text", "URL" and "Gallery"
