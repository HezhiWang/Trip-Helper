import urllib.request
# for py2, use "import urllib"
from bs4 import BeautifulSoup 
base0 = "http://www.booking.com"
base1 = "http://www.booking.com/searchresults.html?aid=304142&label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmcgV1c19ueYgBAZgBMbgBB8gBDNgBA-gBAfgBAqgCAw&sid=c6e9dc7aa93ac2e0ec4cbd9ef8daec72&class_interval=1&dest_id=20088325&dest_type=city&group_adults=2&group_children=0&hlrd=0&label_click=undef&no_rooms=1&review_score_group=empty&room1=A%2CA&sb_price_type=total&score_min=0&search_selected=1&src=index&src_elem=sb&ss=New%20York%20City%2C%20New%20York%20State%2C%20United%20States%20of%20America&ss_raw=new&ssb=empty&sshis=0&rows=15&offset="
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
    # for py2: use "ht = urllib.urlopen(url).read()"
    soup = BeautifulSoup(ht, "lxml")
    # find price rank
    for t in soup.find_all('div',class_ = 'room_details'):
        if t.div:
            pricerank = t.div.div.get('class')[-2][-1]
            pricelist.append(pricerank)
            #print("price: ", pricerank)
        else:
            pricerank = -999
            pricelist.append(pricerank)
            #print("price: ", pricerank)
    # find review number
    for t in soup.find_all("div",class_ = 'reviewFloater'):
        rev = t.div.text.strip().replace("\n",' ').split(' ')
        if rev[0]=='Show':
            totalreview = -999
            treviewlist.append(totalreview)
            #print("total review: ", totalreview)
        else:
            totalreview = rev[-2]
            treviewlist.append(totalreview)
            #print("total review: ", totalreview)
        
    # find hotel link
    for t0 in soup.find_all("a",class_="hotel_name_link"):
        hurl = base0 + t0.get('href',None)
        hthotel = urllib.request.urlopen(hurl).read()
        souphotel = BeautifulSoup(hthotel, "lxml")
        # find hotel name
        for t1 in souphotel.find_all('span',class_ = 'fn'):
            name = t1.text.strip()
            namelist.append(name)
            #print('name: ', name)
        # find address & lng & lat
        for t2 in souphotel.find_all('span', class_ = 'hp_address_subtitle'):
            addr = t2.text.strip()
            addrlist.append(addr)
            lng = t2.get('data-bbox').split(',')[0]
            lat = t2.get('data-bbox').split(',')[1]
            lnglist.append(lng)
            latlist.append(lat)
            #print('addr: ', t2.text.strip())
            #print('lat:',lat, 'lng:',lng)
        # avg score
        reviews = souphotel.find_all('div', class_ = 'hp-gallery-review')    
        for t in reviews:
            if t.div.div:
                avgscore = t.div.div.get('data-review-score')
                avgscorelist.append(avgscore)
                #print('avgscore:', avgscore)
                
                for t in souphotel.find_all('li', class_ = 'clearfix one_col'):
                    allscorelist.append(t.text.strip().split('\n'))
                locscore = allscorelist[2][-1]
                locscorelist.append(locscore)
                #print('locscore:',locscore)
            else:
                locscore = -999
                avgscore = -999
                locscorelist.append(locscore)
                avgscorelist.append(avgscore)
                #print('avgscore:', avgscore)
                #print('locscore:',locscore)
    print(i)

d = {'name':namelist, 'price':pricelist, 'address':addrlist,'lat':latlist,'lng':lnglist,'avgscore':avgscorelist, 'locscore':locscorelist,'total_review':treviewlist} 
bookingDB = pd.DataFrame(d)
bookingDB.to_csv('booking.csv')
print(bookingDB)





