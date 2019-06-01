from django.test import TestCase, Client

class BlogTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_index_access(self):
        res = self.c.get('/')
        self.assertEqual(res.status_code, 200)

    def test_create_access(self):
        res = self.c.get('/login')
        self.assertEqual(res.status_code, 200)
    