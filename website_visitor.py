import webbrowser
import time
# from pykeyboard import PyKeyboard

count = 0
urls = ['https://github.com/somj57/somj57/blob/master/README.md','https://github.com/somj57/somj57/blob/master/README.md','https://github.com/somj57/somj57/blob/master/README.md']
# k = PyKeyboard()

while count < 1000:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(1)
        # k.press_keys(['Command','W'])
        count = count + 1
        print(count);

else:
    pass