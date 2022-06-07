from this import s
from webbrowser import BaseBrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
def ingresar(meil,pa):
    #Datos que extraemos de la pagina inspeccionando elemento
    browser = webdriver.Chrome()  
    browser.get("https://spdigital.cl") 
    browser.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/span[2]/span[1]/button').click()
    username = browser.find_element_by_id("userEmail")
    password = browser.find_element_by_id("password")
    
    
    #Cambiar las credenciales
    username.clear()
    username.click()
    for item in meil:
        username.send_keys(item)
        time.sleep(0.1)

    password.clear()
    password.click()

    for item in pa:
        password.send_keys(item)
        time.sleep(0.1)
    
    #Emula el hacer click en "Iniciar Sesion"
    login_attempt = browser.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/span[2]/span[1]/div/div/button[1]').click()
    time.sleep(3)

def rest(meil):
    browser = webdriver.Chrome() 
    browser.get("https://spdigital.cl") 
    browser.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/span[2]/span[1]/button').click()

    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/span[2]/span[1]/div/div/a/span').click()
    M=browser.find_element_by_id('userEmail')
    for item in meil:
        M.send_keys(item)
        time.sleep(0.1)
    browser.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div[4]/section[1]/div/div/div[2]/div[2]/button').click()
    time.sleep(2)
    browser2 = webdriver.Chrome() 
    browser2.get("https://yopmail.com/es") 
    time.sleep(5)
    browser2.find_element_by_xpath('//*[@id="login"]').send_keys(meil)
    time.sleep(3)
    browser2.find_element_by_xpath('//*[@id="refreshbut"]/button').submit()
    time.sleep(5)
    #browser.switch_to.fradriver.find_element_by_xpath('//a[@class="nav-link"][contains(text(),"Profile")]').click()
    browser2.switch_to.frame(browser.find_element_by_xpath("//iframe[@id='ifmail']"))
    time.sleep(2)
    link=browser2.find_element_by_xpath('//html/body/main/div/div/div/table/tbody/tr[2]/td/p[3]/a').get_attribute('href')
    browser3=webdriver.Chrome()
    browser3.get(link)
    newp='abc123456'
    browser3.find_element_by_id('password').send_keys(newp)
    browser3.find_element_by_id('password2').send_keys(newp)
    browser3.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/section[1]/div/div/div[2]/button').click()
    time.sleep(2)
    return newp
def cambiarpa(meil,newpass):
    browser = webdriver.Chrome() 
    browser.get("https://spdigital.cl") 
    browser.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/span[2]/span[1]/button').click()
    username = browser.find_element_by_id("userEmail")
    password = browser.find_element_by_id("password")
    mail = meil
    passw = "123456789"
    #Cambiar las credenciales
    username.clear()
    username.click()
    for item in mail:
        username.send_keys(item)
        time.sleep(0.1)

    password.clear()
    password.click()

    for item in passw:
        password.send_keys(item)
        time.sleep(0.1)
    browser.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/span[2]/span[1]/div/div/button[1]').click()
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/span[2]/span[1]/button').click()
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/span[2]/span[1]/div/div/a').click()
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/section[1]/div/div/div[1]/a[6]').click()
    time.sleep(2)
    oldpa=browser.find_element_by_id('oldPassword')
    newpa=browser.find_element_by_id('newPassword')
    newpa2=browser.find_element_by_id('confirmPassword')
    for item in passw:
        oldpa.send_keys(item)
        time.sleep(0.1)
    for item in newpass:
        newpa.send_keys(item)
        time.sleep(0.1)
        newpa2.send_keys(item)
        time.sleep(0.1)
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/section[1]/div/div/div[2]/div/div/div[2]/form/button').click()

    
def lol():
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
    link=browser.find_element_by_xpath('/html/body/main/div/div/div/table/tbody/tr[2]/td/p[3]/a').get_attribute('href')
    return link 

    





def crearcuenta():
    generatedmail=lol()
    browser = webdriver.Chrome() 
    browser.get("https://spdigital.cl") 
    time.sleep(5)
    button = browser.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/span[2]/span[1]/button').click()
    button2 = browser.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div/span[2]/span[1]/div/div/button[2]').click()
    time.sleep(1)
    nombre = browser.find_element_by_id('userFirstName').send_keys('nico')
    time.sleep(1)
    apellido = browser.find_element_by_id('userLastName').send_keys('ok')
    rut= browser.find_element_by_id('userRUT').send_keys('5764802-3')
    email = browser.find_element_by_id('userEmail').send_keys(generatedmail)
    telefono= browser.find_element_by_id('userPhone').send_keys('+56952544569')
    contra1='123456789'
    contra = browser.find_element_by_id('password')
    contra2 = browser.find_element_by_id('password2')
    for item in contra1:
        contra.send_keys(item)
    for item in contra1:
        contra2.send_keys(item)
    



    selec = browser.find_element_by_id('terms')
    browser.execute_script("arguments[0].click();", selec)

    submitt = browser.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div[4]/section[1]/div/div[6]/button').click()
    link=ver(generatedmail)
    time.sleep(1)
    browser.get(link)
    time.sleep(2)
    return generatedmail

newpas='987654321'
genmeil=crearcuenta()
cambiarpa(genmeil,newpas)
time.sleep(2)
#ingresar(genmeil,newpas)
n=rest(genmeil)
ingresar(genmeil,n)
