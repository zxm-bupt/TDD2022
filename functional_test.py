from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

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
        self.assertIn ('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder')
                )

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_element(By.TAG_NAME, 'tr')
        self.assertTure(
                any(row.text == '1:Buy peacock feathers' for row in rows)
                )
        self.fail('Finish the test!')
if __name__ == '__main__':
    unittest.main()
