import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# hashtag = input("Enter Hash Tag (e.g. viral): ")
# n = int(input("Number Of Posts: "))
hashtag = 'viral'
n = 5


driver = Chrome(
    executable_path='/Users/tahirsiddique/Desktop/Tiktok Scrapper/myScrapper/chromedriver')

driver.get(f'https://www.tiktok.com/tag/{hashtag}')

elems = driver.find_elements(
    By.XPATH, '//div[@data-e2e="challenge-item"]')
links = []
reserver = 0
for i in range(n):
    s = elems[i]
    link = s.find_element(By.TAG_NAME, 'a').get_attribute('href')
    if(link not in links):
        print(link)
        links.append(link)
        reserver = i
    else:
        i = reserver

driver.get('https://snaptik.app/en')

action = ActionChains(driver)
for link in links:
    input = driver.find_element(By.TAG_NAME, 'input')
    input.send_keys(link)

    button = driver.find_element(By.XPATH, '//span[@class="form-submit"]')
    action.move_to_element(button).click().perform()
    driver.refresh()
    time.sleep(5)
