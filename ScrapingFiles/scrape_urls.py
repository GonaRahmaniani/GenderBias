#scrapes URLs leading to individual job ads from indeed
#yields a .txt file full of URLs
from playwright.sync_api import sync_playwright
import random
import time

with sync_playwright() as pw:
    
    #name of the file containing nurse URLS (this file should already exist)
    FILENAME = 'nurse_urls.txt'
    #URL that scraper will start from
    #change term after 'q=' in URL to change the search term
    START_URL = "https://ca.indeed.com/jobs?q=nurse"

    old_urls = []

    with open(FILENAME, 'r') as f:
        for line in f:
            old_urls.append(line.strip())
    
    def scrape_urls(url, old_list):
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 500, "height": 500})
        page = context.new_page()

        page.goto(str(url))  # go to url

        #collecting URLs and adding them to list if they're not duplicates
        urls = []
        title_boxes = page.locator("//h2[contains(@class,'jobTitle')]")
        for box in title_boxes.element_handles():
            url = 'https://ca.indeed.com' + box.query_selector("a").get_attribute("href")
            if url not in old_urls:
                urls.append(url)
                old_urls.append(url)
    
        global FILENAME
        with open(FILENAME, 'a') as f:
            for url in urls:
                f.write(url + '\n')

        #next page of urls
        next_url = 'https://ca.indeed.com' + page.locator('//a[contains(@data-testid, "pagination-page-next")]').get_attribute('href')

        browser.close()
        if next_url is not None:
            scrape_urls(next_url, old_urls)

    scrape_urls(START_URL, old_urls)