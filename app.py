from selenium import webdriver
from time import sleep

class YtLiker:
    def __init__(self, username, password, target_video):
        self.bot = webdriver.Chrome('driver/chromedriver.exe')
        self.username = username
        self.password = password
        self.target_video = target_video

    def login(self):
        bot = self.bot
        print("\nStarting Login process!\n")
        bot.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        bot.implicitly_wait(10)
        self.bot.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.bot.find_element_by_xpath('//input[@type="email"]').send_keys(self.username)
        self.bot.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.bot.find_element_by_xpath('//input[@type="password"]').send_keys(self.password)
        self.bot.find_element_by_xpath('//*[@id="passwordNext"]').click()
        print("\nLoggedin Successfully!\n")
        sleep(2)
        self.bot.get(self.target_video)
    
    def like(self):
        if not 'style-default-active' in self.bot.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]').get_attribute("class"):
            self.bot.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').click()

    def subscribe(self):
        if self.bot.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button/yt-formatted-string').text != 'Subscribed':
            self.bot.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button').click()

    def quit(self):
        self.bot.quit()


a = YtLiker("", "", "https://www.youtube.com/watch?v=W7Jbpl65HTk")
a.login()
a.like()
a.subscribe()
a.quit()
