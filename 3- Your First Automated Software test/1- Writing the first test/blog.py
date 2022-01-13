from post import Post


class Blog:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f'{self.title} by {self.author} ({len(self.posts)} post{"s" if len(self.posts) !=1 else ""})'

    def create_post(self, title, content):
        post = Post(title, content)
        self.posts.append(post)

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts],
        }
