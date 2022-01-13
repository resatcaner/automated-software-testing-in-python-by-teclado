from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        # This is not a unit test, this contains more than 1 object, so it is an integration test.
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        expected = {'title': 'Test',
                    'author': 'Test Author',
                    'posts': [
                        {'title': 'Test Post', 'content': 'Test Content'}]
                    }

        self.assertDictEqual(b.json(), expected)

    def test_json_no_posts(self):
        b = Blog('Test', 'Test Author')

        expected = {'title': 'Test',
                    'author': 'Test Author',
                    'posts': []}

        self.assertDictEqual(b.json(), expected)
