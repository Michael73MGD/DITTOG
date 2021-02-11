#Reads videos.csv and updates data.csv by calling DITTOG.py
import csv
import time
from selenium import webdriver



videos = 'videos.csv'
with open(videos, 'r', encoding="utf-8", newline='') as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=',')  
    line_count = 0
    for row in csvreader:            
        line_count += 1
        url = row[1]
        title = row[0]
        print("Opening " + url)
        print("Title is " + title)
        driver=webdriver.Chrome('./chromedriver')
        driver.get(url)
        time.sleep(.5)
        #driver.maximize_window()
        driver.set_window_size(1600, 900)
        time.sleep(2)
        driver.execute_script('window.scrollTo(1, 500);')
        time.sleep(2)
        for i in range(1, 50):
            j = i*1000
            driver.execute_script('window.scrollTo(1, '+str(j)+');')
            time.sleep(1)
        time.sleep(3)
        comment_div=driver.find_element_by_xpath('//*[@id="contents"]')
        comments=comment_div.find_elements_by_xpath('//*[@id="content-text"]')
        authors = comment_div.find_elements_by_xpath('//*[@id="author-text"]')
        votes = comment_div.find_elements_by_xpath('//*[@id="vote-count-middle"]')
        time.sleep(.5)
        comment_count = len(comments)
        print("Loaded "+str(comment_count)+" comments.")
        filename = "comments.csv"
        with open(filename, 'a', encoding="utf-8", newline='') as csvfile2:  
            csvwriter = csv.writer(csvfile2)   
            for i in range(0,comment_count):
                comment = comments[i].text
                #print("Scanning comment: "+comment)
                if "Doug is the" in comment or "Doug's the" in comment or "doug is the" in comment or "doug's the" in comment or "Doug the" in comment or "doug the" in comment or "the kind of guy" in comment or "the type of guy" in comment or "the kinda guy" in comment:
                    print("Found one: "+comment)
                    user = authors[i].text
                    likes = votes[i].text
                    line = [comment,user,likes,title]
                    csvwriter.writerow(line)

        driver.quit()
        time.sleep(1)