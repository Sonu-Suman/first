
# Facebook login using python



from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


user_name = input("Enter your name: ")
usr_psswd = input("Enter your password: ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
print("Opend Facebook")
sleep(2)


usr_name_bx = driver.find_element_by_id('email')
usr_name_bx.send_keys(user_name)
print("Email enter")
sleep(1)


usr_psswd_bx = driver.find_element_by_id('pass')
usr_psswd_bx.send_keys(usr_psswd)
print('Password enter')
sleep(1)


login_bx = driver.find_element_by_id('loginbutton')
login_bx.click()

print("Done")
input("Enter anything for quit: ")
driver.quit()
print("Finished")