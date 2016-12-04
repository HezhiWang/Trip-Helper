import codecs
import urllib.request

def plot_map(f):
	'''f is the dataframe(sorted nearby locations) with lat & lng'''
	fhand = codecs.open('location.js','w', "utf-8")
	fhand.write("myData = [\n")
	count = 0
	output= []

	for i in range(f.shape[0]):
    
    	lat = f['lat'].iloc[i]
    	lng = f['lng'].iloc[i]
    	name = f['name'].iloc[i]
    	address = f['address'].iloc[i].strip()
    	try:
        	count += 1
        	if count > 1 : fhand.write(",\n")
        	output = "["+str(lat)+","+str(lng)+", \""+name+"\", "+ "\""+str(address)+"\"]"
        	fhand.write(output)
    	except:
        	continue

	fhand.write("\n];\n")
	fhand.close()

    page = urllib.request.urlopen('hotel_addr_plot.html')


