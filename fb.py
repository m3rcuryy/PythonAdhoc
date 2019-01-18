from selenium import webdriver 
from time import sleep 

usr=raw_input("enter username:\n")
pwd==raw_input("enetr password:\n")

driver = webdriver.Firefox() 
driver.get('https://www.facebook.com/') 
print ("Opened facebook") 
sleep(1) 

username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 

password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Password entered") 

login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 

print ("Done") 
raw_input('Press anything to quit') 
driver.quit() 
print("Finished") 

