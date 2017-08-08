from urllib import request
import random
goog_url = 'https://www.ibm.com/support/knowledgecenter/SVU13_7.2.1/com.ibm.ismsaas.doc/reference/AssetsImportExtendedSample.csv'
def download_files_from_web(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str= str(csv)
    lines = csv_str.split("\\n")
    name = random.randrange(1,1000)
    dest_url = str(name) +".csv"
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_files_from_web(goog_url)

