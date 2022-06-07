from this import s
from tkinter import BROWSE
from webbrowser import BaseBrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def ingresar(mail,passw):
    #Datos que extraemos de la pagina inspeccionando elemento
    browser = webdriver.Chrome() 
    browser.get("https://www.instant-gaming.com/en/") 
    browser.find_element_by_xpath('/html/body/header/div[2]/div/a').click()
    username = browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[4]/div/div/div[1]/div[2]/form/input[1]')
    password = browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[4]/div/div/div[1]/div[2]/form/input[2]')
    for item in mail:
        username.send_keys(item)
        time.sleep(0.1)
    for item in passw:
        password.send_keys(item)
        time.sleep(0.1)
    
    browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[4]/div/div/div[1]/div[2]/form/input[6]').submit()
    time.sleep(5)
def rest(mail):
    browser = webdriver.Chrome() 
    browser.get("https://www.instant-gaming.com/en/lost-password/") 
    inp=browser.find_element_by_xpath('//*[@id="ig-email"]')
    for item in mail:
        inp.send_keys(item)
        time.sleep(0.1)
    browser.find_element_by_xpath('/html/body/div[4]/div/form/div/div/button').click()
    time.sleep(10)
    browser2 = webdriver.Chrome() 
    browser2.get("https://yopmail.com/es") 
    time.sleep(5)
    browser2.find_element_by_xpath('//*[@id="login"]').send_keys(mail)
    time.sleep(3)
    browser2.find_element_by_xpath('//*[@id="refreshbut"]/button').submit()
    time.sleep(5)
    #browser.switch_to.fradriver.find_element_by_xpath('//a[@class="nav-link"][contains(text(),"Profile")]').click()
    browser2.switch_to.frame(browser.find_element_by_xpath("//iframe[@id='ifmail']"))
    time.sleep(2)
    link=browser2.find_element_by_xpath('/html/body/main/div/div/div/table/tbody/tr/td/div[2]/table/tbody/tr/td/div[2]/a').get_attribute('href')
    browser2.get(link)
    newpass='hola2304'
    new=browser2.find_element_by_xpath('//*[@id="ig-new-password-1"]')
    new2=browser2.find_element_by_xpath('//*[@id="ig-new-password-2"]')
    for item in newpass:
        new.send_keys(item)
        time.sleep(0.1)
        new2.send_keys(item)
        time.sleep(0.1)
    browser2.find_element_by_xpath('/html/body/div[4]/div/form/div/button').submit()
    time.sleep(5)
    return newpass
def getmail():
    browser = webdriver.Chrome() 
    browser.get("https://yopmail.com/es/email-generator") 
    time.sleep(2)
    genmail =browser.find_element_by_id('egen')

    txt=genmail.text
    
    return txt
def ver(cuenta):
    browser = webdriver.Chrome() 
    browser.get("https://yopmail.com/es") 
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="login"]').send_keys(cuenta)
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="refreshbut"]/button').submit()
    time.sleep(5)
    #browser.switch_to.fradriver.find_element_by_xpath('//a[@class="nav-link"][contains(text(),"Profile")]').click()
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[@id='ifmail']"))
    time.sleep(2)
    link=browser.find_element_by_xpath('/html/body/main/div/div/div/table/tbody/tr/td/div[2]/table/tbody/tr/td/div[2]/a').get_attribute('href')
    return link 
def crearcuenta():
    generatedmail=getmail()
    browser = webdriver.Chrome() 
    browser.get("https://www.instant-gaming.com/en/") 
    browser.find_element_by_xpath('/html/body/header/div[2]/div/a').click()
    browser.find_element_by_xpath('//*[@id="register-manual"]').click()


    nombre = browser.find_element_by_id('ig-firstname').send_keys('nico')
    time.sleep(1)
    apellido = browser.find_element_by_id('ig-lastname').send_keys('ok')
    time.sleep(1)
    birth=browser.find_element_by_id('ig-birthdate').send_keys('24/03/1997')
    time.sleep(1)
    email = browser.find_element_by_id('ig-email').send_keys(generatedmail)
    time.sleep(1)
    contra1='abc6414224'
    contra = browser.find_element_by_id('ig-pass')
   
    for item in contra1:
        contra.send_keys(item)
        time.sleep(0.1)




    selec = browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[4]/div/div/div[1]/div[1]/div[2]/form/div[2]/label[2]/span')
    browser.execute_script("arguments[0].click();", selec)
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[4]/div/div/div[1]/div[1]/div[2]/form/button').click()
    
    time.sleep(5)
    link=ver(generatedmail)
    time.sleep(1)
    browser.get(link)
    time.sleep(5)
    return generatedmail

def cambiarpa(meil,newpass):
    browser = webdriver.Chrome() 
    browser.get("https://www.instant-gaming.com/en/") 
    browser.find_element_by_xpath('/html/body/header/div[2]/div/a').click()
    username = browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[4]/div/div/div[1]/div[2]/form/input[1]')
    password = browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[4]/div/div/div[1]/div[2]/form/input[2]')
    passw='abc6414224'
    for item in mail:
        username.send_keys(item)
        time.sleep(0.1)
    for item in passw:
        password.send_keys(item)
        time.sleep(0.1)
    
    login=browser.find_element_by_xpath('/html/body/div[10]/div[2]/div[4]/div/div/div[1]/div[2]/form/input[6]').submit()
    time.sleep(3)

    browser.find_element_by_xpath('/html/body/header/div[2]/div[2]/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/header/div[2]/div[2]/div[2]/div/ul/li[5]/a').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[5]/ul/li[5]/a').click()
    time.sleep(1)
    old=browser.find_element_by_xpath('//*[@id="ig-pass1"]')
    new=browser.find_element_by_id('ig-pass2')
    new2=browser.find_element_by_id('ig-pass3')
    for item in passw:
        old.send_keys(item)
        time.sleep(0.1)
    for item in newpass:
        new.send_keys(item)
        time.sleep(0.1)
        new2.send_keys(item)
        time.sleep(0.1)
    
    browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[5]/div[2]/div[6]/div/div[1]/div[3]/form/div/a').submit()
    time.sleep(5)

contra1='abc6414224'
newp='cbc6697111'
mail=crearcuenta()
ingresar(mail,contra1)
cambiarpa(mail,newp)
pas=rest(mail)
ingresar(mail,pas)
