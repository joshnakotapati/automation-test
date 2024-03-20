import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(2)

el = driver.find_element(By.XPATH,"//span[@class='more-arr']")
AC(driver).move_to_element(el).perform()
p_w = driver.current_window_handle
print(p_w)
print(driver.title)
el = driver.find_element(By.XPATH,"//span[normalize-space()='Luxury Trains']")
el.click()
time.sleep(3)
win_handles = driver.window_handles
for win in win_handles:
    if win!=p_w:
        driver.switch_to.window(win)
        print(driver.title)
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[normalize-space()='MAHARAJA EXPRESS']").click()
        time.sleep(2)
        break
window_handles = driver.window_handles
wind = window_handles[2]
driver.switch_to.window(wind)
print(driver.title)
driver.find_element(By.ID,"name").send_keys('joshna')
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("joshnachandra1998@gmail.com")
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//input[@id='number']").send_keys('7989426274')
driver.implicitly_wait(2)
select = Select(driver.find_element(By.XPATH,"//select[@id='train_names']"))
select.select_by_index(1)
time.sleep(2)
select.select_by_visible_text("Palace On Wheels")
time.sleep(3)
driver.find_element(By.ID,"additional_info").send_keys("book the ticket now")
time.sleep(3)
driver.close()
time.sleep(2)
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.find_element(By.XPATH,"//ul[@id='navigation']//a[normalize-space()='HOLIDAYS']").click()
driver.implicitly_wait(2)

















