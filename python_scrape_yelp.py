import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
chromedriver = "/Users/wanghezhi/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver1 = webdriver.Chrome(chromedriver)

file = open("/Users/wanghezhi/Desktop/restaurants_data.txt", "w")
for i in range(3):
    a = str(i * 10)
    url1 = "https://www.yelp.com/search?find_loc=New+York,+NY"
    url2 = "&start=" + a
    url3 = "&cflt=restaurants"
    url = url1 + url2 + url3
    driver1.get(url)

    for i in range(10):
        output_string = driver1.find_elements_by_css_selector("h3.search-result-title")[i].text + ":" + driver1.find_elements_by_css_selector("span.review-count")[i].text + ":" + driver1.find_elements_by_css_selector("span.business-attribute")[i].text + ":" + driver1.find_elements_by_css_selector("address")[i].text + ":" + driver1.find_elements_by_css_selector("span.neighborhood-str-list")[i].text + ":" + driver1.find_elements_by_css_selector("span.category-str-list")[i].text + "\n"
        #print(driver1.find_elements_by_css_selector("span.neighborhood-str-list")[i].text)
        #print(driver1.find_elements_by_css_selector("span.category-str-list")[i].text)
        file.write(output_string)

file.close()