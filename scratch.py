#does not execute javascript
youtube_trending_url='https://www.youtube.com/feed/trending '
import requests
from bs4 import BeautifulSoup

response=requests.get(youtube_trending_url)

print('status code',response.status_code)
with open('trending.html','w') as f:
  f.write(response.text)

doc=BeautifulSoup(response.text,'html.parser')
print('page title',doc.title)

# find all video divs

video_divs=doc.find_all('div',class_='ytd-video-renderer')
print(f'found {len(video_divs)} videos')