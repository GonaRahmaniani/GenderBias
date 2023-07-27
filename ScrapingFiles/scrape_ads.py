#scrapes ads by following URLs in specified .txt file
#adds job ads to .csv file containing existing job ads
from playwright.sync_api import sync_playwright
import pandas
import random
import time
with sync_playwright() as pw:

    #text file containing new URLs just collected
    TXTFILENAME = 'nurse_urls.txt'
    #file that ads will be written to
    #this file must already exist with the columns 'Job Title' and 'Job Ad'
    CSVFILENAME = 'nurse_data.csv'

    ad_urls = []

    with open(TXTFILENAME, 'r') as f:
        for line in f:
            ad_urls.append(line.strip())

    for url in ad_urls:

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

        #if page doesn't contain HTML element, close browser and continue   
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
