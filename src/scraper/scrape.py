from bs4 import BeautifulSoup
import requests

def scrape_for_names(url):
  response = requests.get(url)
  
  if response.status_code != 200:
    print(f"Can't connect to: {url}")
    raise Exception()
  
  soup = BeautifulSoup(response.text, 'html.parser')
  spans = soup.find_all('span', 'repo')
  pinned_repos_names = [] 
  for span in spans:
    pinned_repos_names.append(span.text)
  
  return pinned_repos_names