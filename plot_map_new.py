import codecs

def plot_map(df):
	'''df is the dataframe(sorted nearby locations) with lat & lng'''
	fh = codecs.open('locations.js','w', "utf-8")
	fh.write("locations = [\n")
	count = 0
	output= []

	for i in range(df.shape[0]):
		lat = df['lat'].iloc[i]
		lng = df['lng'].iloc[i]
		name = df['name'].iloc[i]
		address = df['address'].iloc[i].strip()
		
		output = "["+str(lat)+","+str(lng)+", \""+name+"\", "+ "\""+str(address)+"\"]"
		fh.write(output)
		if i < df.shape[0]-1:
			fh.write(",\n")
		else:
			fh.write("\n];\n")
			fh.close()
		
