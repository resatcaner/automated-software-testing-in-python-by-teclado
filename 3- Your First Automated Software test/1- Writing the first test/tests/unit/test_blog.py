from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertIsInstance(b.posts, list)
        self.assertEqual(len(b.posts), 0)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('caner', 'resat')
        b2.posts = ['a', 'b']

        b3 = Blog('caner', 'idil')
        b3.posts = ['test']

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'caner by resat (2 posts)')
        self.assertEqual(b3.__repr__(), 'caner by idil (1 post)')


