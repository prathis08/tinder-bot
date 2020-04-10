from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from secrets import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome("c:\webdriver\chromedriver")

    def login(self):
        def check_exists_by_xpath(xpath):
            try:
                element = self.driver.find_element_by_xpath(xpath)
            except NoSuchElementException:
                return None
            return element

        self.driver.get('https://tinder.com')

        sleep(4)

        check_more_options = check_exists_by_xpath('//button[text()="More Options"]')
        if (check_more_options != None):
            check_more_options.click()

        sleep(2)

        fb_btn = self.driver.find_element_by_css_selector('button[aria-label="Log in with Facebook"]')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        sleep(4)
        
        try:
            popup_0 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/button/span')
            popup_0.click()
        except:
            popup_0 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/button')
            popup_0.click()
            

        sleep(2)
        
        try:
            popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
            popup_1.click()
        except:
            popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_1.click()


        sleep(2)
        

        try:
            popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
            popup_2.click()
        except:
            popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
            popup_2.click()
            

        sleep(2)

        try:
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button/span').click()
        except:
            pass

        self.auto_swipe()

    def like(self):
        like_btn = self.driver.find_element_by_css_selector('button[aria-label="Like"]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_css_selector('button[aria-label="Nope"]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(1.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.close_tinder_plus()

    def close_popup(self):
        popup_4 = self.driver.find_element_by_xpath('//span[text()="Not interested"]')
        popup_4.cli5ck()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//a[text()="Keep Swiping"]')
        match_popup.click()

    def close_tinder_plus(self):
        tinder_plus_popup =  self.driver.find_element_by_xpath('//span[text()="No Thanks"]')
        tinder_plus_popup.click()
        self.driver.quit()
        exit(0)

bot = TinderBot()
bot.login()

