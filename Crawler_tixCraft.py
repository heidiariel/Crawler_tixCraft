from selenium.webdriver import Chrome
import time
'''總共有7步需要修改'''


driver = Chrome("./chromedriver")
'''第一步，要購買的演唱會網址'''
driver.get("https://tixcraft.com/activity/detail/19_KarenMok") #要買的演唱會票網址, 拓元
#driver.find_element_by_xpath('//a[@href="#login"]').click()
driver.find_element_by_link_text("會員登入").click()

#for迴圈+try ,如果網頁還沒跑好就sleep1秒
for i in range(100):
    try:
        #driver.find_element_by_id("loginGoogle").click()
        '''第二步，選FB登陸，是google就改成google'''
        driver.find_element_by_xpath("//a[@href='/login/facebook']").click()
    except:
        time.sleep(1)
    else:
        break
'''第三步，登陸賬密'''
#!!!!FB賬號!!!!
#!!!!FB密碼!!!!
driver.find_element_by_id("email").send_keys("!!!!FB賬號!!!!")
driver.find_element_by_id("pass").send_keys("!!!!FB密碼!!!!")
driver.find_element_by_id("loginbutton").click()

#直到"立即訂購"的連接出現, 刷新1000次
for i in range(1000):
    #
    for a in range(100):
        try:
            '''第四步，要購買的演唱會網址,改後面19_'''
            driver.find_element_by_xpath("//a[@href='/activity/game/19_KarenMok']").click()
        except:
            time.sleep(1)
        else:
            break
    for b in range(100):
        try:
            '''第五步，選擇場次'''
            driver.find_element_by_id("keySearchGameList").send_keys("2019/12/07 (六) 19:30")
        except:
            time.sleep(1)
        else:
            break
    try:
        driver.find_element_by_xpath('//input[@value="立即訂購"]').click()
    except:
        driver.refresh()
    else:
        break


for i in range(100):
    try:
        '''第六步，選位置，黃3I區'''
        driver.find_element_by_xpath("//a[contains(text(),'黃3I區')]").click()
    except:
        time.sleep(1)
    else:
        break

for i in range(100):
    try:
        # 勾選已經詳細閱讀xxxxx
        driver.find_element_by_id("TicketForm_agree").click()
    except:
        time.sleep(1)
    else:
        break

driver.find_element_by_id("TicketForm_ticketPrice_05").click()
'''第七步，選擇票的張數 value="幾張" '''
driver.find_element_by_xpath('//option[@value="4"]').click() #選要幾張票

'''
driver.refresh() # 刷新方法 refresh
driver.file_detector_context("#login").click() #text
'''
