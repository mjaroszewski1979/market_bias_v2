# Import the unittest module for creating and running tests
import unittest
# Import the re module for regular expression operations
import re
# Import the sys module for system-specific parameters and functions
import sys
# Import the os module for interacting with the operating system
import os


# Adjust the system path to include the parent directory of the current file
current = os.path.dirname(os.path.realpath(__file__))  
parent = os.path.dirname(current)  
sys.path.append(parent)

# Import the application factory function from the run module
import run

# Create the application instance using the factory function
app = run.create_app()


class RoutesTestCase(unittest.TestCase):
    """
    Test case for the application's routes, including index, strategies, about, contact, success, and error pages.
    """

    def test_app_exists(self):
        """
        Ensure that the application instance exists.
        """
        self.assertIsNotNone(app)

    def test_index(self):
        """
        Ensure that the index page loads correctly.
        This method checks the response status code for the GET request to the index route.
        """
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_index_data(self):
        """
        Ensure that the index page returns the expected content.
        This method checks that the response data contains specific text from the index page.
        """
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'The Big Picture' in response.data)

    def test_index_error(self):
        """
        Ensure that the index page loads correctly in case of a RemoteDataError.
        This method checks that the response data does not contain an error message.
        """
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertFalse(b'Fetching data failed' in response.data)

    def test_strategies(self):
        """
        Ensure that the strategies page loads correctly.
        This method checks the response status code for the GET request to the strategies route.
        """
        tester = app.test_client(self)
        response = tester.get('/strategies', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_strategies_data(self):
        """
        Ensure that the strategies page returns the expected content.
        This method checks that the response data contains specific text from the strategies page.
        """
        tester = app.test_client(self)
        response = tester.get('/strategies', content_type='html/text')
        self.assertTrue(b'DUAL MOMENTUM' in response.data)

    def test_strategies_error(self):
        """
        Ensure that the strategies page loads correctly in case of a RemoteDataError.
        This method checks that the response data does not contain an error message.
        """
        tester = app.test_client(self)
        response = tester.get('/strategies', content_type='html/text')
        self.assertFalse(b'Fetching data failed' in response.data)

    def test_about(self):
        """
        Ensure that the about page loads correctly.
        This method checks the response status code for the GET request to the about route.
        """
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_about_data(self):
        """
        Ensure that the about page returns the expected content.
        This method checks that the response data contains specific text from the about page.
        """
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertTrue(b'Technical Analysis' in response.data)

    def test_contact(self):
        """
        Ensure that the contact page loads correctly.
        This method checks the response status code for the GET request to the contact route.
        """
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_contact_data(self):
        """
        Ensure that the contact page returns the expected content.
        This method checks that the response data contains specific text from the contact page.
        """
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertTrue(b'How to Achieve Success' in response.data)

    def test_success_post(self):
        """
        Ensure that the success page loads correctly after a valid POST request.
        This method checks the response data for a thank you message after posting valid data.
        """
        tester = app.test_client(self)
        response = tester.post('/success', 
        data=dict(name='r"[A-Z][a-z]+,?\s+(?:[A-Z][a-z]*\.?\s*)?[A-Z][a-z]+"', 
        email="r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'"), follow_redirects=True)
        self.assertIn(b'Thank you', response.data)

    def test_404(self):
        """
        Ensure that the 404 error page loads correctly.
        This method checks the response status code for the GET request to a non-existent route.
        """
        tester = app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_404_data(self):
        """
        Ensure that the 404 error page returns the expected content.
        This method checks that the response data contains specific text from the 404 error page.
        """
        tester = app.test_client(self)
        response = tester.get('/404', content_type='html/text')
        self.assertTrue(b'the website you were looking for' in response.data)

# Run the test cases
if __name__ == '__main__':
    unittest.main()
