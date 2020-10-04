from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class YtLiker:
    def __init__(self, username, password, target_video):
        self.bot = webdriver.Chrome('driver/chromedriver.exe')
        self.username = username
        self.password = password
        self.target_video = target_video

    def login(self):
        bot = self.bot
        bot.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        bot.implicitly_wait(20)
        self.bot.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.bot.find_element_by_xpath('//input[@type="email"]').send_keys(self.username)
        self.bot.find_element_by_xpath('//*[@id="identifierNext"]').click()
        # sleep(3)
        self.bot.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(self.password)
        self.bot.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(Keys.RETURN)

        # self.bot.find_element_by_xpath('//*[@id="passwordNext"]').click()
        # sleep(2)
        # confirm dialog
        try:
            self.bot.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/span/span').click()
        except:
            pass
        self.bot.get(self.target_video)

    def like(self):
        if not 'style-default-active' in self.bot.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]').get_attribute("class"):
            self.bot.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').click()

    def subscribe(self):
        if self.bot.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button/yt-formatted-string').text != 'Subscribed':
            self.bot.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button').click()

    def quit(self):
        self.bot.quit()

target_video = "https://www.youtube.com/watch?v=W7Jbpl65HTk"

with open('credentials.txt') as f:
    for x in f.readlines():
        username = x.split(' ')[0]
        password = x.split(' ')[1]
        a = YtLiker(username, password, target_video)
        try:       
            a.login()     
            a.like()
            a.subscribe()
        except:
            print("[-] Login failed -->", username)
            pass
        finally:
            a.quit()


