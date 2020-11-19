import redditeasy

post = redditeasy.Subreddit("copypasta")
postoutput = post.get_post()

print(f"Posts Title: {postoutput.title}\n"
      f"Posts Image Link: {postoutput.content}\n"
      f"Post Created At: {postoutput.created_at}\n"
      f"Posts Upvote Count: {postoutput.score}\n"
      f"Posts Award Count: {postoutput.total_awards}\n"
      f"NSFW?: {postoutput.nsfw}")
