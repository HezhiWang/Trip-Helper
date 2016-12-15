import urllib.request
from bs4 import BeautifulSoup
'''
This module is a webscraper that gets information of hotels in NYC from booking.com.
It uses urllib to open urls and read the source html , and beautifulsoup to extract information,
including name, address, scores, reviews and latitudes & longitudes.
''' 
base0 = "http://www.booking.com"
# base url for Manhattan
base1 = "http://www.booking.com/searchresults.html?aid=304142&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmcgV1c19ueYgBAZgBMbgBB8gBDNgBA-gBAfgBAqgCAw&sid=c6e9dc7aa93ac2e0ec4cbd9ef8daec72&class_interval=1&dest_id=20088325&dest_type=city&group_adults=2&group_children=0&hlrd=0&label_click=undef&no_rooms=1&review_score_group=empty&room1=A%2CA&sb_price_type=total&score_min=0&search_selected=1&src=index&src_elem=sb&ss=New%20York%20City%2C%20New%20York%20State%2C%20United%20States%20of%20America&ss_raw=new&ssb=empty&sshis=0&rows=15&offset="
# base url for Brooklyn
# base2 = "http://www.booking.com/searchresults.html?aid=376370&label=bdot-XGU4XCNgAdnROGBcUOKsoQS77084489314%3Apl%3Ata%3Ap1%3Ap21%2C078%2C000%3Aac%3Aap1t1%3Aneg%3Afi%3Atiaud-146342138710%3Akwd-334108349%3Alp9003562%3Ali%3Adec%3Adm&lang=en-us&sid=4a944c8fb061415dbfbfa4c6b63bb734&src=searchresults&src_elem=sb&error_url=http%3A%2F%2Fwww.booking.com%2Fsearchresults.html%3Faid%3D376370%3Blabel%3Dbdot-XGU4XCNgAdnROGBcUOKsoQS77084489314%253Apl%253Ata%253Ap1%253Ap21%252C078%252C000%253Aac%253Aap1t1%253Aneg%253Afi%253Atiaud-146342138710%253Akwd-334108349%253Alp9003562%253Ali%253Adec%253Adm%3Bsid%3D4a944c8fb061415dbfbfa4c6b63bb734%3Bcity%3D20089077%3Bclass_interval%3D1%3Bdest_id%3D20085207%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Bhlrd%3D0%3Bhyb_red%3D0%3Binac%3D0%3Blabel_click%3Dundef%3Bnha_red%3D0%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Bredirected_from_city%3D0%3Bredirected_from_landmark%3D0%3Bredirected_from_region%3D0%3Breview_score_group%3Dempty%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bscore_min%3D0%3Bsearch_selected%3D1%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bss%3DBrooklyn%252C%2520New%2520York%2520State%252C%2520United%2520States%2520of%2520America%3Bss_all%3D0%3Bss_raw%3Dbroo%3Bssb%3Dempty%3Bsshis%3D0%3Bssne_untouched%3DQueens%3Btrack_hp_back_button%3D1%26%3B&ss=Brooklyn&ssne=Brooklyn&ssne_untouched=Brooklyn&city=20085207&checkin_month=&checkin_monthday=&checkin_year=&checkout_month=&checkout_monthday=&checkout_year=&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&ss_raw=Brooklyn&dest_id=&dest_type=&search_pageview_id=09802bb6cc700264&search_selected=false&sshis=0&rows=15&offset="

# base url for Queens
# base3 = "http://www.booking.com/searchresults.en-us.html?aid=376370&label=bdot-XGU4XCNgAdnROGBcUOKsoQS77084489314%3Apl%3Ata%3Ap1%3Ap21%2C078%2C000%3Aac%3Aap1t1%3Aneg%3Afi%3Atiaud-146342138710%3Akwd-334108349%3Alp9003562%3Ali%3Adec%3Adm&lang=en-us&sid=4a944c8fb061415dbfbfa4c6b63bb734&src=index&src_elem=sb&error_url=http%3A%2F%2Fwww.booking.com%2Findex.html%3Faid%3D376370%3Blabel%3Dbdot-XGU4XCNgAdnROGBcUOKsoQS77084489314%253Apl%253Ata%253Ap1%253Ap21%252C078%252C000%253Aac%253Aap1t1%253Aneg%253Afi%253Atiaud-146342138710%253Akwd-334108349%253Alp9003562%253Ali%253Adec%253Adm%3Bsid%3D4a944c8fb061415dbfbfa4c6b63bb734%3Bsb_price_type%3Dtotal%26%3B&ss=Queens%2C+New+York+State%2C+USA&checkin_month=&checkin_monthday=&checkin_year=&checkout_month=&checkout_monthday=&checkout_year=&nflt=&sb_acc_types=1&room1=A%2CA&no_rooms=1&group_adults=2&group_children=0&ss_raw=queens&ac_position=1&ac_langcode=en&dest_id=20089077&dest_type=city&&sshis=0&rows=15&offset="

pricelist = []
namelist = []
addrlist = []
latlist = []
lnglist = []
avgscorelist = []
locscorelist = []
treviewlist = []
allscorelist = []
for i in range(0, 52):
    p = i*15
    url = base1 + str(p)
    ht = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(ht, "lxml")

    # find price rank
    for t in soup.find_all('div',class_ = 'room_details'):
        if t.div:
            pricerank = t.div.div.get('class')[-2][-1]
            pricelist.append(pricerank)
        else:
            pricerank = -999
            pricelist.append(pricerank)
    # find review number
    for t in soup.find_all("div",class_ = 'reviewFloater'):
        rev = t.div.text.strip().replace("\n",' ').split(' ')
        if rev[0]=='Show':
            totalreview = -999
            treviewlist.append(totalreview)
        else:
            totalreview = rev[-2]
            treviewlist.append(totalreview)
        
    # find hotel link
    for t0 in soup.find_all("a",class_="hotel_name_link"):
        hurl = base0 + t0.get('href',None)
        hthotel = urllib.request.urlopen(hurl).read()
        souphotel = BeautifulSoup(hthotel, "lxml")
        # find hotel name
        for t1 in souphotel.find_all('span',class_ = 'fn'):
            name = t1.text.strip()
            namelist.append(name)
            
        # find address & lng & lat
        for t2 in souphotel.find_all('span', class_ = 'hp_address_subtitle'):
            addr = t2.text.strip()
            addrlist.append(addr)
            lng = t2.get('data-bbox').split(',')[0]
            lat = t2.get('data-bbox').split(',')[1]
            lnglist.append(lng)
            latlist.append(lat)
            
        # avg score
        reviews = souphotel.find_all('div', class_ = 'hp-gallery-review')    
        for t in reviews:
            if t.div.div:
                avgscore = t.div.div.get('data-review-score')
                avgscorelist.append(avgscore)
                
                
                for t in souphotel.find_all('li', class_ = 'clearfix one_col'):
                    allscorelist.append(t.text.strip().split('\n'))
                locscore = allscorelist[2][-1]
                locscorelist.append(locscore)
                
            else:
                locscore = -999
                avgscore = -999
                locscorelist.append(locscore)
                avgscorelist.append(avgscore)
                

d = {'Name':namelist, 'Price':pricelist, 'Address':addrlist,'Lat':latlist,'Lng':lnglist,'Avgscore':avgscorelist, 'Locscore':locscorelist,'Total_review':treviewlist} 
bookingDB = pd.DataFrame(d)
bookingDB.to_csv('bookingNYC.csv')





