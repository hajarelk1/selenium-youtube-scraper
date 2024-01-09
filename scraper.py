from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


YOUTUBE_TRENDING_URL='https://www.youtube.com/feed/trending'

def get_driver():
  chrome_options=Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver=webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):
  VIDEO_DIV_TAG='ytd-video-renderer'
  driver.get(YOUTUBE_TRENDING_URL)
  videos=driver.find_elements(By.TAG_NAME,VIDEO_DIV_TAG)
  return videos

def parse_video(video):
  title_tag=video.find_elements(By.ID,'video-title')
  title=title_tag.text
  url=title_tag.get_attribute('href')

  thumbnail_tag=video.find_elements(By.TAG_NAME,'img')
  thumbnail_url=thumbnail_tag.get_attribute('src')

  channel_div=video.find_elements(By.CLASS_NAME,'ytd-channel-name')
  channel_name=channel_div.text

  description=video.find_elements(By.ID,'description-text')

  return {
    'title': title,
    'url': url,
    'thumbnail_url': thumbnail_url,
    'channel name': channel_name,
    'description': description
  
  }


  


  
if __name__=="__main__":
  print("creating the driver")
  driver=get_driver()
  print('fetching trending videos')
  videos=get_videos(driver)

  print(f'found {len(videos)} videos')

  print('parsing the first 10 videos')

  video_data=[parse_video(video) for video in videos[:10]]
# title,url,thumbnail_url,channel, views,uploaded,description

  
  
  print('title :',title)
  print('url:',url)
  print('thumbnail_url:',thumbnail_url)
  print('Channel name:', channel_name)
  print('descrption;',description)


  


#






