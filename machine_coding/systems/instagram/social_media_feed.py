from datetime import datetime


class Post:
    def __init__(self: Post, content: str) -> None:
        self.content: str = content
        self.created_at = datetime.now()
        # self.likes: int = 0
        # self.comments: list[str] = []


class User:
    def __init__(self: User, name: str) -> None:
        self.name = name
        self.follows: set[User] = set()
        self.posts: list[Post] = []

    def to_follow(self: User, followUser: User) -> None:
        self.follows.add(followUser)
    
    def to_unfollow(self: User, unfollowUser: User) -> None:
        try:
            self.follows.remove(unfollowUser)
        except KeyError:
            print(f"{self.name} doesn't follow {unfollowUser.name}")

    def create_post(self: User, content: str) -> None:
        post = Post(content)
        self.posts.append(post)
    
    def get_all_posts(self: User) -> list[Post]:
        return self.posts
    
    def feed(self: User):
        posts = []
        for user in self.follows:
            userPosts = user.get_all_posts()
            for post in userPosts:
                posts.append(post)

        return sorted(posts, key=lambda post: post.created_at, reverse=True)


# user1 = User("Ankur")
# user2 = User("Ayushi")

# user1.create_post("Hello, this is my first post")
# user1.create_post("Hello, this is my second post!")
# user2.to_follow(user1)

# posts = user1.get_all_posts()
# for post in posts:
#     print(post.content)
#     input("Enter to see next post")

# user2.to_follow(user1)
# print("Now user2 follows user1")
# feeds = user2.feed()
# user1.create_post("Hello, this is my third post!")

# for feed in feeds:
#     print(feed.content)
#     input("Enter to continue")

# print("All feeds ended")

import time  # To simulate time gaps between posts

# Create users
alice = User("Alice")
bob = User("Bob")
carol = User("Carol")

# Follow relationships
alice.to_follow(bob)
alice.to_follow(carol)

# Users create posts
bob.create_post("Bob's first post")
time.sleep(1)  # Pause to simulate time passing
carol.create_post("Carol's first post")
time.sleep(1)
bob.create_post("Bob's second post")
time.sleep(1)
carol.create_post("Carol's second post")

# Alice checks her feed
print(f"{alice.name}'s feed (most recent first):")
feed = alice.feed()
for post in feed:
    print(f"{post.created_at.strftime('%H:%M:%S')} - {post.content}")
