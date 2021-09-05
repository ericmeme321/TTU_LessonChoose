from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import pyautogui
import time

class choose():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.set_page_load_timeout(100)
        self.username = username
        self.password = password
    
    def login(self):    

        login_url = f'https://stucis.ttu.edu.tw/login.php'
        self.driver.get(login_url)

        username_text= WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "ID"))
        )
        password_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "PWD"))
        )

        username_text.clear()
        password_text.clear()
        username_text.send_keys(self.username)
        password_text.send_keys(self.password)
        
        login = self.driver.find_element_by_name('Submit')
                
        login.click()

        time.sleep(1)

    def select(self):
        image = 'noRobot.PNG'
        loc = pyautogui.locateOnScreen(image, grayscale=True, confidence=.5)
        pyautogui.moveTo(loc, duration=0)
        pyautogui.click()

        choose_url = f'https://stucis.ttu.edu.tw/selcourse/FastSelect.php'

        lesson = open('lesson.txt', 'r', encoding = 'latin-1')

        count = 0
        while True:
            count += 1
            try:
                self.driver.get(choose_url)

                button = self.driver.find_element_by_name('Confirm')
                if button:
                    input = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.NAME, "EnterSbj"))
                    )
                    input.clear()
                    for line in lesson.readlines():
                        input.send_keys(line)

                button.click()
                lesson.close
                flg = True
                break

            except NoSuchElementException:
                timeString = time.localtime(int(time.time()))
                struct_time = time.strftime("%m/%d %I:%M:%S", timeString)
                print(f"尚未開放選課 請稍後 嘗試次數 {count} 次\n\
                        目前時間 {struct_time} \n")
                time.sleep(1)
                continue


if __name__ == '__main__':
    username = input("輸入學號:")
    password = input("輸入密碼:")
    someone = choose(str(username), str(password))
    someone.login()
    someone.select()

