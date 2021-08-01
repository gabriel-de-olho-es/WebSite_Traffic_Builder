import webbrowser
import time

count = 0
urls = ['https:https://fagulha-animes.xyz']

while count < 1000:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(1) #Change the according to your internet connection and device 
        count = count + 1
        print(count);

else:
    pass

# Above code may look foolish but trust me it works Just change the urls links to your dezired link
