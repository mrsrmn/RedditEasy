Changelog
======================================


Version 3.6.1
--------------
* RedditEasy works faster now


Version 3.6.1
--------------
* Gallery content JSON key, "media", now returns a dict


Version 3.6.0
---------------

* ``created_at`` now returns Epoch (int)
* Added gallery support
* Added "Gallery" to ``content_type``
* ``content`` now returns a JSON dict if the ``content_type`` is "Gallery"
* Removed "subreddit", "user" from Subreddit, User and put them in ``get_post()`` as parameter



Version 3.5.0
--------------

* Added a ``content_type`` to the return of ``Subreddit``, ``AsyncSubreddit``, ``User`` and ``AsyncUser``
