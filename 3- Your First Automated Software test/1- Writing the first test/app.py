from blog import Blog
from post import Post

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit.'
POST_TEMPLATE = """
--- {} ---

{}

"""
blogs = dict()


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():  # [(blog_name, Blog), (blog_name, Blog)]
        print(f'- {blog}')


def ask_create_blog():
    title = input('Enter the title: ')
    author = input('Enter the author: ')
    blogs[title] = Blog(title, author)
    print('blog is successfully created: ')


def ask_read_blog():
    title = input('Enter the title: ')
    print_posts(blogs[title])


def print_posts(blog: Blog):
    for post in blog.posts:
        print_post(post)


def print_post(post: Post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_name = input('Enter Blog Name: ')
    title = input('Enter Post Title: ')
    content = input('Enter Content: ')

    blogs[blog_name].create_post(title, content)
