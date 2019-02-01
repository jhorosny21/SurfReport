import time
import requests
from bs4 import BeautifulSoup
import lxml, lxml.html
import json
#import urllib.request as ur



def measure_time():
    iterations = 10000000
    start_time = time.time()
    for x in range(iterations):
        time_since_started = time.time() - start_time
        time_per_iteration = time_since_started / (x + 1)
        iterations_remaining = iterations - x
        estimated_time_to_complete = iterations_remaining * time_per_iteration
        print(('Time till complete %s' % estimated_time_to_complete), end='\r')

    end_time = time.time()
    return print('Duration: {}'.format(end_time - start_time))

column_names = [ 'index', 'name', 'market_cap', 'price', 'past_24_volume', 'total_supply', 'change_24' ]

def print_page_title(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table', attrs={"id":"currencies"})
    rows = table.find_all('tr')
    data = []
    for row in rows:
        dict = {}
        columns = [ i.text.replace('\n', '') for i in row.find_all('td') ]
        if len(columns) > 7:
            for x in range(7):
                dict[column_names[x]] = columns[x]
            data.append(dict)

    for object in data:
        dict = {}
        columns =[ i.text.replace('\n', '') for i in row. find_all('td') ]
        index = int(object['index'])
        name = object['name']
        if index > 0:
            print (index)
            print (name)
        #dict = {}
        #columns = [i.text.replace('\n', '')]

    #print(data[50])



    #f = requests.get(url)
    #soup = BeatifulSoup(url)
    #response = requests.get(url)
    #soup = BeautifulSoup(response.text, features ='lxml')
    #print(soup.find(id='[fiftyTwoWeekHighChange]''[INTC]''[Nasdac]''[summary]''[pagename]''[Quote]'))
    #html = requests.urlopen(url)
    #qtree = html.fromstring(page.content)
    #quote = qtree.xpath('//span[@class="time_rtq_ticker"]')
    #print(r.encoding) #use for finding out the encoding code for a new website

    #print('This is the', r.content)

    # return print('This is the text', r.text)
    #print('This is the headers', r.headers)
    #print('This is the history', r.history)
    #print(r.headers.get('content-type', 'unkown'))
    #print(soup.find(id=[fiftyTwoWeekHighChange][INTC][Nasdac][summary][pagename][Quote]))
    #f = urlib.urlopen()
    #myfile = f.read()
    #print(myfile)
    #print(lxml.html.tostring('element'))
    #print('Quote', html.tostring(quote[0]))
    #print('F Text', f.text)

    #12/26: Ended the day by fixing some of the bugs within the script adding more organization to the script itself as well, trying to figure out how to add variables and look up specfiic stock prices. Next step finish debugging at add variable searches.

def print_Beatiful_Soup(url):
    f = requests.get(url)
    #print(soup.find(id='[fiftyTwoWeekHighChange]''[INTC]''[Nasdac]''[summary]''[pagename]''[Quote]''[Intel Corporation]''[INTC stock chart]''[Intel Corporation stock chart]''[stock chart]' '[stocks]' '[quotes]' '[finance]''["symbol":"INTC"]["meta":{"property":{"twitter:site":"@YahooFinance"]''[fb:pages:90376669494]'))



def html():
        html = requests.urlopen()
        # print(html.read())

#def stock_quote(url):
    #page = request.get(url)
    #qtree = html.fromstring(page.content)
    #quote = qtree.xpath('//span[@class = "time_rtq_ticker"]')
    #print 'quote', html.tostring(quote[0])
    #for loop
    #for x in quote:
        #print ('Quote'), html.tostring(x)
        #print ('Shares outstanding', 'Shares')









#print_page_title('https://www.yahoo.com')
#print_page_title('https://www.google.com')
#print_page_title('https://www.news.google.com')
print_page_title('https://coinmarketcap.com/')
# print_page_title()
