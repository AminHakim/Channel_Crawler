import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

#open target website with webdriver
website = 'https://channelcrawler.com/eng/results2/1102862/page:1'
path = '\Python310\Chromedriver'
driver = webdriver.Chrome(executable_path=r'C:\Python310\Chromedriver\chromedriver.exe')
driver.get(website)

#empty list
Youtube_Name = []
Youtube_Link = []
Youtube_Country = []
Subscribers = []
Total_Videos = []
Total_Views = []
Creation_Date = []


#wait before click sign in
time.sleep(1)

fill linkedin username and password
username = "liontroopergeneral@gmail.com"
password = "L1oNG3nErAL2846!"

automated fill in username and password
driver.find_element("xpath", '//*[@name="data[User][username]"]').send_keys(username)
driver.find_element("xpath", '//*[@name="data[User][password]"]').send_keys(password)

wait before click login
time.sleep(1)

click to log in
click_submit = driver.find_element("xpath", '//*[@class="submitbutton btn btn-primary btn-lg"]').click()

#wait
time.sleep(1)




#main loop
#change value at 'while z' for number of pages
z = 0
while z < 1:
    z += 1

#going to intial scraping page
    initial_page = 'https://channelcrawler.com/eng/results2/1102862/page:' + str(z)
    driver.get(initial_page)

# ait
    time.sleep(1)

#get link and name + append to empty list
# change value at 'while y' for how many elements it need for the Xpath (channel crawler only max 20 per page)
    y = 0
    while y < 5:
        y += 1

        #Xpath for name
        yt_name = driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div[2]/div"
                                                          "[" + str(y) + "]/h4/a")
        #Xpath for Country
        yt_country = driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div[2]/div"
                                                             "[" + str(y) + "]/h4/img")
        #Xpath for Details
        yt_deets = driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div[2]/div"
                                                           "[" + str(y) + "]/p[1]/small")
        #get the name + link
        for a in yt_name:
            get_yt_name = a.text
            get_link = a.get_attribute("href")
            Youtube_Name.append(get_yt_name)
            Youtube_Link.append(get_link)

        #get the country by src source
        for b in yt_country:
            get_yt_country = b.get_attribute("src")
            Youtube_Country.append(get_yt_country)

        #get the details with array
        for c in yt_deets:
            array1 = c.text.split('\n')
            Subscribers.append(array1[0])
            Total_Videos.append(array1[1])
            Total_Views.append(array1[2])
            Creation_Date.append(array1[3])

# print process
    print('YT_NAME')
    for a in Youtube_Name:
        print(a)
    print()
    print('YT_LINK')
    for a in Youtube_Link:
        print(a)
    print()
    print('YT_COUNTRY')
    for b in Youtube_Country:
        print(b)
    print()
    print('SUBSCRIBERS')
    for c in Subscribers:
        print(c)
    print()
    print('TOTAL_VIDEOS')
    for c in Total_Videos:
        print(c)
    print()
    print('TOTAL_VIEWS')
    for c in Total_Views:
        print(c)
    print()
    print('CREATION_DATE')
    for c in Creation_Date:
        print(c)
    print()

#quit driver after run
driver.quit()

#exporting to excel process
df = pd.DataFrame({'YT_Name': Youtube_Name, 'YT_Link': Youtube_Link, 'YT_Country': Youtube_Country,
                   'Subscribers': Subscribers, 'Total_Videos': Total_Videos, 'Total_Views': Total_Views,
                   'Creation_Date': Creation_Date})
df.to_excel('YT Test 3.xlsx')
print(df)