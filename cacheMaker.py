import mechanize
from BeautifulSoup import BeautifulSoup

sitemapUrl="http://www.raspberryweather.com/sitemap.xml" # REPLACE WITH YOUR OWN SITEMAP
parsedUrl=[] #contains urls from sitemap

browser=mechanize.Browser()
try:
        print "Getting the sitemap"
        response=browser.open(sitemapUrl)
except:
        print "Something went wrong"
        exit()

soup=BeautifulSoup(response)

for url in soup.findAll('loc'):
        url=str(url)
        url=url[5:]                     # i know i know, could be done nicer
        parsedUrl.append(url[:len(url)-6])
        
#visit the sites and generate a cache
for url in parsedUrl:
        print "Visiting: "+url
        browser.open(url)
        print "Done, cache created"

print "Finished, if you want to check, have a look at /wp-content/cache"
