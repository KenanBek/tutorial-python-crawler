import random
import requests
from bs4 import BeautifulSoup

	
def get_page(url, ctimeout=10, rtimeout=30):
    uas = [
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
        "Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.01",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    ]
    user_agent = random.choice(uas)
    headers = {
        "Connection": "close",  # another way to cover tracks
        "User-Agent": user_agent
    }
    response = requests.get(
        url,
        headers=headers,
        timeout=(ctimeout, rtimeout)  # connect, read
    )
    return response.content

def get_page_selector(url, ctimeout=10, rtimeout=30):
    content = get_page(url, ctimeout=ctimeout, rtimeout=rtimeout)
    soup = BeautifulSoup(content, "html5lib")
    return soup

page_selector = get_page_selector("https://www.google.com.tr/search?q=hello")

page_selector.title
