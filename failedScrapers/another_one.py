from selenium import webdriver
import csv
import time

driver=webdriver.Chrome('./chromedriver')

driver.get('https://www.youtube.com/watch?v=4LAGNeE5pjA&ab_channel=DougDeMuro"')
time.sleep(.5)
driver.maximize_window()

time.sleep(2)
driver.execute_script('window.scrollTo(1, 500);')


for i in range(1, 15):
    j = i*1000
    driver.execute_script('window.scrollTo(1, '+str(j)+');')
    time.sleep(.25)


comment_div=driver.find_element_by_xpath('//*[@id="contents"]')
comments=comment_div.find_elements_by_xpath('//*[@id="content-text"]')
authors = comment_div.find_elements_by_xpath('//*[@id="author-text"]')

votes = comment_div.find_elements_by_xpath('//*[@id="vote-count-middle"]')
time.sleep(2)


#for i in range(0,len(comments)):
#    print(comments[i].text+" by "+authors[i].text+" with "+votes[i].text+" upvotes.")

title = ''
comment_count = len(comments)
filename = "comments.csv"
with open(filename, 'a', encoding="utf-8", newline='') as csvfile2:  
    csvwriter = csv.writer(csvfile2)   
    for i in range(0,comment_count):
        comment = comments[i].text
        if "Doug is the" in comment or "Doug's the" in comment or "doug is the" in comment or "doug's the" in comment or "Doug the" in comment or "doug the" in comment or "the kind of guy" in comment or "the type of guy" in comment or "the kinda guy" in comment:
            user = authors[i].text
            likes = votes[i].text
            line = [comment,user,likes,title]
            csvwriter.writerow(line)

driver.quit()