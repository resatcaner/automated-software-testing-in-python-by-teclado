from unittest import TestCase
import app
from unittest.mock import patch
from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self):
        """creates the object for every each test below in the class"""
        blog = Blog('Test', 'Test Author')  # Create a new object
        app.blogs = {'Test': blog}

    def test_menu_prints_promt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:  # patches the builtin print method, replacing the function
            app.print_blogs()
            mocked_print.assert_called_with(
                '- Test by Test Author (0 posts)')  # calls the function but not checking the result, checking if the function is called with correct params

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        app.blogs['Test'].create_post('Test Post', 'Test Content')
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(app.blogs['Test'])
            mocked_print_post.assert_called_with(app.blogs['Test'].posts[0])

    def test_print_post(self):
        post = Post('Post title', 'Post Content')
        expected_print = app.POST_TEMPLATE.format('Post title', 'Post Content')
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        with patch('builtins.input') as mockup_input:
            mockup_input.side_effect = ('Test', 'Test Post', 'Test Content')
            app.ask_create_post()
            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test Post')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'Test Content')

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
                app.menu()
                mocked_ask_create_blog.assert_called()
