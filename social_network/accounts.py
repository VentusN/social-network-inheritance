from social_network import posts

class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email  = email 
        self.following=[]
        self.posts=[]

    def add_post(self, post):
        self.posts.append(post)
        post.set_user(self)

    def get_timeline(self):
        timeline =[]
        for user in self.following:
            for post in user.posts:
              timeline.append(post)
        return sorted(timeline, key = lambda x: x.timestamp)

    def follow(self, other):
        self.following.append(other)


