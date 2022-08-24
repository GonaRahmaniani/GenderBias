#this spider goes through indeed search and stores individual ad websites in a pickle file so the ad spider can collect the
#job title and job ad of the individual ads

import os
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "websites"
    #put in url that you want websites from ex:// https://ca.indeed.com/Engineer-jobs
    start_urls = ['https://ca.indeed.com/Nursing-jobs?vjk='
    ]
    #parse puts scrapes websites from indeed and goes to the next pages until it has retrieved 
    #all of the individual job ad websites and stores it in a text file 
    def parse(self,response):
        website_old_list = []
        filename = 'nurse.txt'

        if os.path.exists(filename):
            with open(filename,'r') as f:
                for line in f:
                    website_old_list.append(line)
                
        
        # websites is a list that spider gets from indeed website page with multiple ads on it
        websites = response.css('h2.jobTitle a::attr(href)').extract()
        #print('\n\n\n\n')
        #print(response.css('h2.jobTitle a::attr(href)').get())
        #print('\n\n\n')
        #return
        #print(websites)
        i =  0 
        while i < len(websites):
            websites[i] = response.urljoin(response.css('h2.jobTitle a::attr(href)')[i].extract())
            i += 1
        
        #new code to get websites
        #websites = response.css('h2.jobTitle a::attr(href)').getall()
        #for item in websites:
         #   item = 'https://ca.indeed.com'+item

        #print('\n\n\n\n')
        #print(websites)
        #print('\n\n\n\n')
        #return
    
        #creating new list with all websites 
        website_new_list = website_old_list+websites
        website_new_list = list(set(website_new_list))

        # saving it to a text file
        with open(filename,'w') as f: 
            for item in website_new_list:
                f.write(str(item) + '\n')
                
           
        # follow pagination link
        next_page_url = response.css('div.pagination a::attr(href)')[-1].get()
        next_page_url = 'https://ca.indeed.com'+next_page_url
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
