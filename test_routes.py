from flask import current_app
import unittest
import re
from run import create_app



app = create_app()


class FlaskTestCase(unittest.TestCase):

    # Ensures that the application instance exists
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    # Ensures that index page loads correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the index page
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'The Big Picture' in response.data)

    # Ensures that index page loads correctly in case of RemoteDataError
    def test_index_error(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertFalse(b'Fetching data failed' in response.data)

    # Ensures that strategies page loads correctly
    def test_strategies(self):
        tester = app.test_client(self)
        response = tester.get('/strategies', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the strategies page
    def test_strategies_data(self):
        tester = app.test_client(self)
        response = tester.get('/strategies', content_type='html/text')
        self.assertTrue(b'DUAL MOMENTUM' in response.data)

    # Ensures that strategies page loads correctly in case of RemoteDataError
    def test_strategies_error(self):
        tester = app.test_client(self)
        response = tester.get('/strategies', content_type='html/text')
        self.assertFalse(b'Fetching data failed' in response.data)

    # Ensures that about page loads correctly
    def test_about(self):
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the about page
    def test_about_data(self):
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertTrue(b'Technical Analysis' in response.data)

    # Ensures that contact page loads correctly
    def test_contact(self):
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensures that the data returned contains actual text from the contact page
    def test_contact_data(self):
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertTrue(b'How to Achieve Success' in response.data)

    # Ensures that the success page loads correctly given valid name and email
    def test_success_post(self):
        tester = app.test_client(self)
        response = tester.post('/success', 
        data=dict(name='r"[A-Z][a-z]+,?\s+(?:[A-Z][a-z]*\.?\s*)?[A-Z][a-z]+"', 
        email="r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'"), follow_redirects=True)
        self.assertIn(b'Thank you', response.data)

    # Ensures that error/404 page loads correctly
    def test_404(self):
        tester = app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    # Ensures that the data returned contains actual text from the error/404 page
    def test_404_data(self):
        tester = app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertTrue(b'the website you were looking for' in response.data)




if __name__ == '__main__':
    unittest.main()
