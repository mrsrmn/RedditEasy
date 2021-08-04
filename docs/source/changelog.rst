Changelog
======================================

Version 3.6.0
---------------

* ``created_at`` now works returns Epoch (int)
* Added gallery support
* Added "Gallery" to ``created_at``
* ``content`` now returns a JSON dict if the ``content_type`` is "Gallery"
* Removed "subreddit", "user" from Subreddit, User and put it in ``get_post()`` as parameter



Version 3.5.0
--------------

* Added a ``content_type`` to the return of ``Subreddit``, ``AsyncSubreddit``, ``User`` and ``AsyncUser``
