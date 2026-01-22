import threading
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/',
'https://python.langchain.com/v0.2/docs/tutorials/'

]
def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

# Simple Thread using loop


# threads=[]
# for url in urls:
#     thread=threading.Thread(target=fetch_content,args=(url,))
#     threads.append(thread)
#     thread.start()  


# for t in threads:
#     t.join()

## By Thread Pool

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(fetch_content, urls)
    

print("All web pages fetched")