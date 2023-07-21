from playwright.sync_api import sync_playwright
import pandas
import random
import time
with sync_playwright() as pw:

    TXTFILENAME = 'nurse_urls.txt'
    CSVFILENAME = 'nurse_data.csv'

    ad_urls = []

    with open(TXTFILENAME, 'r') as f:
        for line in f:
            ad_urls.append(line.strip())

    #use for testing on one ad:
    #ad_urls = ad_urls.[0]

    page_number = 0

    for url in ad_urls:

        page_number += 1

        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width' : 500, 'height' : 500})
        
        page = context.new_page()
        page.goto(str(url))
        timeout = False

        try:
            filename = 'temp.txt'
            title = page.locator('//title').inner_text()
            temp_ad = page.locator('//div[@id="jobDescriptionText"]').inner_text().strip()
            ad = ''
            
            #making job description text one line
            with open(filename, 'w') as f:
                f.write(temp_ad)

            with open(filename, 'r') as f:
                for line in f:
                    ad += line.strip() + ' '

            with open(filename, 'w') as f:
                f.write('')
            
        except:
            timeout = True
            page.close()

        if not timeout:
            ad_df = pandas.read_csv(CSVFILENAME)
            temp_df = pandas.DataFrame({
                'Job Title' : [title],
                'Job Ad' : [ad],
            })

            appended_data = pandas.concat([ad_df,temp_df], ignore_index=True, sort=False)

            appended_data.to_csv(CSVFILENAME, index=False)

            page.close()
            browser.close()

            #time.sleep(random.uniform(1.0, 3.0))

            #if page_number ==2:
                #page_number = 0
                #sec = random.uniform(1.0, 5.0)
                #time.sleep(sec)