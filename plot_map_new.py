import codecs

def plot_map(df):
	'''df is the dataframe(sorted nearby locations) with lat & lng'''
	fh = codecs.open('locations.js','w', "utf-8")
	fh.write("locations = [\n")
	count = 0
	output= []

	for i in range(df.shape[0]):
		lat = df['Lat'].iloc[i]
		lng = df['Lng'].iloc[i]
		name = df['Name'].iloc[i]
		address = df['Address'].iloc[i].strip()
		
		output = "["+str(lat)+","+str(lng)+", \""+name+"\", "+ "\""+str(address)+"\"]"
		fh.write(output)
		if i < df.shape[0]-1:
			fh.write(",\n")
		else:
			fh.write("\n];\n")
			fh.close()
		
