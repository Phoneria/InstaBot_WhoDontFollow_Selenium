from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

username = "************"
password = "************"

client= "username"


class Instagram :

    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)
        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")


        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        self.browser.maximize_window()
        time.sleep(5)

    def search_user(self,find_user):
        time.sleep(5)
        self.browser.get(f"https://www.instagram.com/{find_user}")

    def go_following(self):
        time.sleep(5)
        buttons = self.browser.find_elements(By.CLASS_NAME,"_aa_5")
        buttons[2].click()

    def go_followers(self):
        time.sleep(5)
        buttons = self.browser.find_elements(By.CLASS_NAME, "_aa_5")
        buttons[1].click()

    def get_following(self):
        time.sleep(5)
        my_list= []
        followers= self.browser.find_elements(By.CSS_SELECTOR,"._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm")
        for follower in followers:
            a= follower.text.split("\n")
            my_list.append(a[0])

        return (my_list)

    def get_follower(self):
        time.sleep(5)
        my_list = []
        followers = self.browser.find_elements(By.CSS_SELECTOR,
                                               "._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm")
        for follower in followers:
            a = follower.text.split("\n")
            my_list.append(a[0])

        return (my_list)

    def scroll_following(self):
        time.sleep(1)

        action = ActionChains(self.browser)
        number = int(self.browser.find_elements(By.CLASS_NAME, "_aa_5")[2].text.split(" ")[0])

        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()

        time.sleep(1)

        window=  self.browser.find_element(By.CLASS_NAME,"_ab8w._ab94._ab97._ab9h._ab9m._ab9p._abch._abcm")


        window.click()
        time.sleep(1)
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
        for i in range(number*3):
            action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
            time.sleep(0.5)
        return number

    def scroll_follower(self):
        time.sleep(1)

        action = ActionChains(self.browser)
        number = int(self.browser.find_elements(By.CLASS_NAME, "_aa_5")[1].text.split(" ")[0])

        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()

        time.sleep(1)

        window = self.browser.find_element(By.CLASS_NAME, "_ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm")

        window.click()
        time.sleep(1)

        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
        for i in range(number * 4):
            action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
            time.sleep(0.5)

        return number

    def close_window(self):

        time.sleep(1)
        self.browser.find_element(By.CLASS_NAME,"_ac7b._ac7d").click()

    def close(self):
        self.browser.close()
try:
    instagram = Instagram(username,password)

    instagram.signIn()
    instagram.search_user(client)

    instagram.go_following()
    following_number=instagram.scroll_following()
    following = [instagram.get_following()]
    instagram.close_window()

    instagram.go_followers()
    follower_number=instagram.scroll_follower()
    follower = [instagram.get_follower()]
    print("Follower : ",follower)
    print("Following : ",following)
    
    print("Who Dont Follow : ")
    for i in following[0][0:following_number]:
        if not i in follower[0][0:follower_number]:
            print(i)


    instagram.close_window()
except :
    pass

finally:
    instagram.close()









for i in following[0][0:following_number]:
    if not i in follower[0:follower_number]:
        print(i)
