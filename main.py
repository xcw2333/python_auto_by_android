from appium import webdriver
import time
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
  'platformName': 'Android', 
  'platformVersion': '11',
  'deviceName': 'xxx', 
  'appPackage': 'com.ss.android.ugc.aweme.lite', 
  'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity', 
  'unicodeKeyboard': True, 
  'resetKeyboard': True, 
  'noReset': True,     
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
sum=0
def swipe_down(driver,star_y=0.9,stop_y=0.1,duration=1000):
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    x1 = int(x * 0.5)
    y1 = int(y * star_y)
    x2 = int(x * 0.5)
    y2 = int(y * stop_y)
    driver.swipe(x1, y1, x2, y2, duration)
i=3
while i==3:
    sum+=1
    swipe_down(driver)
    print('tim_sum:',sum)
    time.sleep(1)
input('**** Press to quit..')
driver.quit()