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

if __name__=="__main__":
  print("creating the driver")
  driver=get_driver()

  print('fetching the page')
  driver.get(youtube_trending_url)

  print('get the video divs')
  video_div_class='ytd-video-renderer'
  video_divs=driver.find_elements(By.CLASS_NAME,video_div_class)


  print(f'found {len(video_divs)} videos')
  

#






