from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
youtube_trending_url='https://www.youtube.com/feed/trending'

def get_driver():
  chrome_options=Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')

  driver=webdriver.Chrome(options=chrome_options)

  return driver


def get_videos(driver):
  video_div_tag='ytd-video-renderer'
  driver.get(youtube_trending_url)
  videos=driver.find_elements(By.TAG_NAME,video_div_tag)
  return videos

  
if __name__=="__main__":
  print("creating the driver")
  driver=get_driver()
  print('fetching trending videos')
  videos=get_videos(driver)

  print(f'found {len(videos)} videos')
  

#






