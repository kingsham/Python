import webbrowser
import time
import random
while True:
	sites=random.choice(['google.com','indeed.com','bing.com',])
	visit="http://{}".format(sites)
	webbrowser.open(visit)
	seconds=random.randrange(3,20)
	time.sleep(seconds)
