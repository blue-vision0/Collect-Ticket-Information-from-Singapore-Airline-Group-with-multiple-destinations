from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from prettytable import PrettyTable


# # 隐藏webdriver
# # 参考自https://zhuanlan.zhihu.com/p/191033198
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# option.add_experimental_option('useAutomationExtension', False)
#
# PATH = r"D:\anaconda\envs\WebScraping\drivers\chromedriver.exe"
#
# # 隐藏webdriver
# driver = webdriver.Chrome(PATH, options=option)
# driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
#     'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
# })
# # 打开网页
# driver.maximize_window()
# url = "https://www.singaporeair.com/zh_CN/cn/home#/book/bookflight"
# driver.get(url)
#
# # 填写出发和目的地信息
# driver.find_element(By.ID, "flightOrigin1").send_keys("SIN")
# sleep(1)
# driver.find_element(By.CLASS_NAME, "suggestion__entry").click()
# driver.find_element(By.ID, "bookFlightDestination").send_keys('PVG')
# sleep(1)
# driver.find_element(By.CLASS_NAME, "suggestion__entry").click()
# driver.find_element(By.ID, "departDate1").click()
# driver.find_element(By.CLASS_NAME, "form-label").click()
#
# res = []
#
# for i in range(8):
#     sleep(2)
#     alldates = driver.find_elements(By.XPATH,
#                                     "//div[@class='calendar_month_left']//ul[@class='calendar_days']//li[@date-data]")
#     for dates in alldates:
#         date = dates.text
#         feature = dates.get_attribute('date-data')
#         if date != ' ':
#             print(feature)
#             try:
#                 price = dates.find_element(By.CLASS_NAME, "calendar-histogram-details")
#                 money = price.text
#                 if money != '':
#                     print(price.text)
#                 else:
#                     money = "No ticket"
#                     print(money)
#                 res.append([feature, money])
#             except:
#                 print("Fail to find")
#     driver.find_element(By.CLASS_NAME, "right").click()
#
# driver.quit()
# mytable = PrettyTable(["date", "price", "trip"])
# for [date, price] in res:
#     mytable.add_row([date, price + '$', "SIN --> 上海"])
# print(mytable)


# //*[@id="hwidget"]/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div[2]/form/div[1]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/label

class CheckTicket():

    def __init__(self):
        # 隐藏webdriver
        # 参考自https://zhuanlan.zhihu.com/p/191033198
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('useAutomationExtension', False)
        # option.headless = True

        PATH = r"D:\anaconda\envs\WebScraping\drivers\chromedriver.exe"

        # 隐藏webdriver
        driver = webdriver.Chrome(PATH, options=option)
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
        })
        driver.maximize_window()
        # driver.minimize_window()
        self.driver = driver
        self.res = []

    def set_trip(self, destination: str, depature="SIN"):
        self.driver.maximize_window()
        url = "https://www.singaporeair.com/zh_CN/cn/home#/book/bookflight"
        self.driver.get(url)
        self.driver.find_element(By.ID, "flightOrigin1").send_keys(depature)
        sleep(0.5)
        self.driver.find_element(By.CLASS_NAME, "suggestion__entry").click()
        self.driver.find_element(By.ID, "bookFlightDestination").send_keys(destination)
        sleep(0.5)
        self.driver.find_element(By.CLASS_NAME, "suggestion__entry").click()
        self.driver.find_element(By.ID, "departDate1").click()
        self.driver.find_element(By.CLASS_NAME, "form-label").click()
        self.driver.minimize_window()

    def collect_information(self, end_time: str, destination: str):
        end_time = end_time.split("-")
        end_year = int(end_time[0])
        end_month = int(end_time[1])

        i = 0
        while i < 12:
            sleep(2)
            alldates = self.driver.find_elements(By.XPATH,
                                                 "//div[@class='calendar_month_left']//ul[@class='calendar_days']//li[@date-data]")
            for dates in alldates:
                date = dates.text
                feature = dates.get_attribute('date-data')
                if date != ' ':
                    print(feature)
                    try:
                        price = dates.find_element(By.CLASS_NAME, "calendar-histogram-details")
                        money = price.text
                        if money != '':
                            money = money + '$'
                            print(money)
                        else:
                            money = "No ticket"
                            print(money)
                        self.res.append([feature, money, "新加坡 --> " + destination])
                    except:
                        print("Fail to find")
            self.driver.find_element(By.CLASS_NAME, "right").click()
            i += 1
            [year, month, _] = self.res[-1][0].split('-')
            if int(year) >= end_year and int(month) >= end_month:
                break

    def search(self, dest: str, ddl: str):
        maps = {"上海": "PVG", "成都": "CTU", "重庆": "CKG", "香港": "HKG", "深圳": "SZX"}
        self.set_trip(maps[dest])
        self.collect_information(ddl, dest)

    def show(self):
        mytable = PrettyTable(["date", "price", "trip"])
        self.res.sort(key=lambda x: x[0])
        for [date, price, trip] in self.res:
            if price[-1] == '$':
                mytable.add_row([date, price, trip])
        self.driver.quit()
        print(mytable)


res = CheckTicket()
res.search("重庆", "2023-01")
res.search("上海", "2023-01")
res.search("成都", "2023-01")
res.search("深圳", "2023-01")
res.show()
