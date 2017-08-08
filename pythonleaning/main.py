import random
import urllib.request

def Download_web_image(url):
    name = random.randrange(1,1000)
    Full_name = str(name) + ".jpeg"
    urllib.request.urlretrieve(url, Full_name)


Download_web_image()