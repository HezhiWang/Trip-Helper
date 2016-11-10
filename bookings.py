# web crawler for Booking.com 
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver3 = webdriver.Chrome()
driver4 = webdriver.Chrome()

base = "http://www.booking.com/searchresults.html?aid=304142&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmcgV1c19ueYgBAZgBMbgBB8gBDNgBA-gBAfgBAqgCAw&sid=c6e9dc7aa93ac2e0ec4cbd9ef8daec72&class_interval=1&dest_id=20088325&dest_type=city&group_adults=2&group_children=0&hlrd=0&label_click=undef&no_rooms=1&review_score_group=empty&room1=A%2CA&sb_price_type=total&score_min=0&search_selected=1&src=index&src_elem=sb&ss=New%20York%20City%2C%20New%20York%20State%2C%20United%20States%20of%20America&ss_raw=new&ssb=empty&sshis=0&rows=15&offset="
for i in range(0, 3):
    p = i*15
    driver3.get(base + str(p))
    # price rank
    for link in driver3.find_elements_by_class_name('sr_price_estimate'):
        print (link.find_element_by_css_selector('div').get_attribute('class')[-2])
    # find hotel url
    for link in driver3.find_elements_by_class_name('sr-hotel__title'):
        url = link.find_element_by_css_selector('a').get_attribute('href')
        driver4.get(url)
        
        # find hotel name
        name = driver4.find_element_by_css_selector('#hp_hotel_name')
        print( "Name: " + name.text)
        
        try:
            total = driver4.find_element_by_css_selector('span.rating.notranslate')
            tscore = total.text
            #print ("Total Score: " + tscore)
        except NoSuchElementException:
            tscore = '-999'
        print ("Total Score: " + tscore)
            
        try:
            loc = driver4.find_element_by_css_selector('div.best-review-score')
            lscore = loc.text   
        except NoSuchElementException:
            lscore = '-999'
            #print ("Loc Score: " + lscore)
        print ("Loc Score: " + lscore)                
        
        # find address         
        addr = driver4.find_element_by_css_selector('p#showMap2.address.address_clean')
        print ("address: " + addr.text)