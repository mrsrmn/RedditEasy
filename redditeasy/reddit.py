class Reddit:
    def __init__(self, image_link, title, upvote_ratio,
                 total_awards, score, downvotes, nsfw, pinned):
        self.image_link = image_link
        self.title = title
        self.upvote_ratio = upvote_ratio
        self.total_awards = total_awards
        self.score = score
        self.downvotes = downvotes
        self.nsfw = nsfw
        self.pinned = pinned
