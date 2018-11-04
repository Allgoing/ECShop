from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(r'file:///E:/demo.html')

    driver.find_element_by_class_name('wait').click()
    element = WebDriverWait(driver, 10, 0.5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'red'))
    )
    print(element.text)

    # element = WebDriverWait(driver, 10, 0.5).until(
    #             EC.visibility_of_element_located((By.XPATH,"//div[@id='display']/div"))
    #             )
    # print element.text




