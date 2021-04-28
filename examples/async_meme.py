import redditeasy
import asyncio

# To get your Reddit API client info go to
# https://www.reddit.com/prefs/apps
# and create an app

# For more detailed explanation, see this image: https://i.imgur.com/Ri13AQu.png
# Please note that the async classes of RedditEasy will not work outside an async function whatsoever

# This example does not work in Python <3.7, see this: https://stackoverflow.com/a/52796732/12920146


async def meme(subreddit):
    post = redditeasy.AsyncSubreddit(subreddit=subreddit,  # Subreddit name
                                     client_id="",         # Your client ID
                                     client_secret="",     # Your client secret
                                     user_agent=""         # Your user agent (ex: ClientName/0.1 by YourUsername")
                                     )

    postoutput = await post.get_post()

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
          f"Subreddit Name: r/{postoutput.subreddit_name}")


asyncio.run(meme("dankmemes"))
