# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
try:
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()
except:
    print("There was an error")

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()

# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
news_soup = soup(html, 'html.parser')

# Find all hemisphere containers
hemisphere_divs = news_soup.find_all('div', class_="item")

# Loop through hemisphere containers and click on image urls
for hemisphere in range(len(hemisphere_divs)):
    hem_link = browser.find_by_css("a.product-item h3")
    hem_link[hemisphere].click()
    
    
    # Initiate new html object and parse beautiful soup with html
    img_detail = browser.html
    imagesoup = soup(img_detail, 'html.parser')
    # Find image url and assign it to a variable
    hem_url = imagesoup.find('img' , class_='wide-image')['src']
    # Create full image url by adding image url with base url
    img_url = f'https://marshemispheres.com/{hem_url}'
    # Find image title and assign it to a variable
    img_title = browser.find_by_css('.title').text
    # Append image urls and titles to hemisphere_image_urls
    hemisphere_image_urls.append({"title": img_title,
                              "img_url": img_url})
    browser.back()
    
browser.quit()

hemisphere_image_urls




