import redditeasy

# To get your Reddit API client info go to
# https://www.reddit.com/prefs/apps
# and create an app

# For more detailed explanation, see this image: https://i.imgur.com/Ri13AQu.png


post = redditeasy.User(user="gallowboob",  # Username
                       client_id="",       # Your client ID
                       client_secret="",   # Your client secret
                       user_agent=""       # Your user agent (ex: ClientName/0.1 by YourUsername")
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
      f"Comment count: {postoutput.comment_count}")
