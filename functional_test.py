from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Edge()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
		

        #Edith has heard about a cool new online to-do app
        #to do check out its homepage
        self.browser.get('http://localhost:8000')

        #She notices the page title and header mention to-do listss
        self.assertIn ('To-Do', self.browser.title), "Browser title was: " + self.browser.title
        self.fail('Finish the test!')
if __name__ == '__main__':
    unittest.main()
#She is invited to enter a to-do item straight away

#She typs "Buy peacock feathers" into a text box (Edith's hobby
#is trying fly-fishing lures)

#When she hits enter, the page updates, and now the page lists 
#"1: Buy peacock feathers" as an item in a to-do list

#There is still a text box inviting he to add another item, She
#enters "Use peacock feathers to make a fly"（Edith is very methodical）

#The page updates again, and now shows both items on her list

#Edith wonders whether the site will remember her list. Then she sees 
#that the site has generated a unique URL for her -- there is some 
#explanatory text to that effect

#she visits that URLs - her to-do list is still there
#Satisfied, she goes back to sleep 
browser.quit()
