from BeautifulSoup import BeautifulSoup
import requests
import time
import math

BASEURL = "http://www.bitcoincharts.com/?page="
FILENAME = "/Users/shrayas/code/hacks/bitcoin-news/output.txt"

f = open(FILENAME,'w')

start = time.time()

for i in xrange(1,151):

    print "Processing " + str(i) + "/150"

    requestURL = BASEURL + str(i)
    response = requests.get(requestURL)
    responseText = response.text

    soup = BeautifulSoup(responseText)

    fpBoxDiv = soup.find('div',{'class':'fp-box'});
    h3s = fpBoxDiv.findAll('h3')

    for h3 in h3s:
        dateOfPublish = h3.find('span',{'class':'extra'}).text
        newsArticleLink = h3.find('a').get('href')
        newsArticleHeadline = h3.find('a').text

        record = dateOfPublish + "|" + newsArticleLink +"|"+ newsArticleHeadline + "\n"
        record = record.encode('ascii','ignore')

        f.write(record)


f.close()

end = time.time()

print "done, took " + str(math.floor(end-start)) + "s"

'''
r = requests.get("http://www.google.com")
print r.text
'''
