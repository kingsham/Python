import webbrowser
import time
import random
while True: 
	sites=random.choice(['google.com','indeed.com','bing.com',]) // An array of random sites that will open 
	visit="http://{}".format(sites)
	webbrowser.open(visit)
	seconds=random.randrange(3,20) // the sites will open for 20 seconds 
	time.sleep(seconds)
