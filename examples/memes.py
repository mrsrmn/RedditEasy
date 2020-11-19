import redditeasy

post = redditeasy.Subreddit("memes")
postoutput = post.get_post()

print(f"Posts Title: {postoutput.title}\n"
      f"Posts Content: {postoutput.content}\n"
      f"Post Created At: {postoutput.created_at}\n"
      f"Posts Upvote Count: {postoutput.score}\n"
      f"Posts Award Count: {postoutput.total_awards}\n"
      f"NSFW?: {postoutput.nsfw}")
