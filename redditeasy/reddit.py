class Reddit:
    def __init__(self, time, image_link, title, upvote_ratio,
                 total_awards, score, downvotes, updated, nsfw, pinned):
        self.time = time
        self.image_link = image_link
        self.title = title
        self.upvote_ratio = upvote_ratio
        self.total_awards = total_awards
        self.score = score
        self.downvotes = downvotes
        self.updated = updated
        self.nsfw = nsfw
        self.pinned = pinned
