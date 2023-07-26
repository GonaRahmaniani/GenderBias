from playwright.sync_api import sync_playwright
import random
import time

with sync_playwright() as pw:
    
    #PAGE_NUMBER = 0
    FILENAME_OLD = 'nurse_urls_old.txt'
    FILENAME = 'nurse_urls.txt'
    START_URL = "https://ca.indeed.com/jobs?q=nurse"

    old_urls = []

    with open(FILENAME_OLD, 'r') as f:
        for line in f:
            old_urls.append(line.strip())
    
    def scrape_urls(url, old_list):
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 500, "height": 500})
        page = context.new_page()

        page.goto(str(url))  # go to url

        urls = []
        title_boxes = page.locator("//h2[contains(@class,'jobTitle')]")
        for box in title_boxes.element_handles():
            url = 'https://ca.indeed.com' + box.query_selector("a").get_attribute("href")
            if url not in old_urls:
                urls.append(url)
                old_urls.append(url)
    
        global FILENAME
        filename = FILENAME
        with open(filename, 'a') as f:
            for url in urls:
                f.write(url + '\n')

        next_url = 'https://ca.indeed.com' + page.locator('//a[contains(@data-testid, "pagination-page-next")]').get_attribute('href')

        browser.close()
        #for testing purposes
        #global PAGE_NUMBER
        #PAGE_NUMBER += 1
        if next_url is not None: #and PAGE_NUMBER < 5:
            #time.sleep(random.uniform(1.0, 3.0))
            scrape_urls(next_url, old_urls)

    scrape_urls(START_URL, old_urls)

    '''with open(FILENAME, 'r') as n:
        with open(FILENAME_OLD, 'a') as o:
            for line in n:
                o.write(line.strip() + '\n')'''
