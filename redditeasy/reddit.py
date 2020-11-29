class Reddit:
    def __init__(self, content, title, upvote_ratio,
                 total_awards, score, downvotes, created_at, nsfw, pinned, author, post_url, stickied, spoiler,
                 post_flair, author_flair):
        self.content = content
        self.title = title
        self.upvote_ratio = upvote_ratio
        self.total_awards = total_awards
        self.score = score
        self.downvotes = downvotes
        self.created_at = created_at
        self.nsfw = nsfw
        self.pinned = pinned
        self.author = author
        self.post_url = post_url
        self.stickied = stickied
        self.spoiler = spoiler
