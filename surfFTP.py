import requests, re

urls = []
print('\t To exit the program please press Ctrl + C')
def getPage(url):
    print(url)
    html = requests.get(url).text
    global urls
    urls = []
    p = False
    for thing in html.split(" "):
        if thing.startswith('href="'):
            m = str(re.findall(r'"([A-Za-z0-9_\./\\-]*)"', thing))[2:-2]
            if '../' == m:
                p = True
            if p:
                urls.append(m)
    print('Index \t URL')
    [print(f'{i} \t {c}') for i, c in enumerate(urls)]

url = input('please enter the Base URL: ') #  "https://download.freebsd.org/ftp/"
getPage(url)
lastUrl = url
while True:
    i = input('Insert the index of the link you wish to access or /rst to reset to base url: ')
    if i == '/rst':
        print(f'\nYou are now reseted in your pase url: {url}')
        lastUrl = url
        getPage(lastUrl)
    else: 
        lastUrl = lastUrl + urls[int(i)]
        getPage(lastUrl)

