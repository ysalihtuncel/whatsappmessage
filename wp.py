from selenium import webdriver

driver = webdriver.Chrome('/home/Desktop/chromedriver')  #chrome driver nerede tanımlı ise orası
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ') #whatsapp konuşmasındaki kişi yada grubun doğru ismi
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code') #tarayıcıdan qr kod okutulmalu, okutulduysa herhangi birşey yapmaya gerek yok

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3u328') #her whatsapp kullanıcısının mesaj gönderme alanındaki <div> id si farklıdır. Sayfayı incele yapıp değiştirebilirsiniz.

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-') #her whatsapp kullanıcısının mesaj gönderme alanındaki <button> id si farklıdır. Sayfayı incele yapıp değiştirebilirsiniz.
    button.click()
