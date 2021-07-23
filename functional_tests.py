from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes to check out its
        # homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item

        # She types 'Buy peacock feathers' into a text box

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock featers"

        # There is still a text box for her to enter more todos
        # She enters 'Use peacock feathers to make a fly'

        # The page updates again and now shows both items in her list

        # Edith sees there is a unique url for her to come back to this list later on

        # She goes to that url and her list is still there!

        # She gets off the internet for today


if __name__ == '__main__':
    unittest.main(warnings='ignore')
