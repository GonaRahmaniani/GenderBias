#this spider goes through all the individual ad websites and pulls the job title and the job ads and puts it in a csv file 
#with columns 'Job Title' and 'Job Ads'
import scrapy
import pandas


class AdsSpider(scrapy.Spider):
    name = "ads"
    start_urls = []
    filename = 'nurse.txt'
    # start_urls are from text file called cs.txt
    with open(filename,'r') as f:
        for line in f:
            start_urls.append(line.strip())
    
    start_urls = list(filter(None, start_urls))
    
    #print("\n\n\n\n")
    #print(start_urls)
    #print("\n\n\n\n")
    #exit
        #start_urls = pickle.load(f)
    
    # parse gets title and job ad and puts it in csv file named master_list
    def parse(self, response):
        #filename = '/Users/ellapalter/Downloads/tutorial/tutorial/spiders/cs_postcovid.csv'
        filename = 'nurse_data.csv'
        ad_df = pandas.read_csv(filename)
        job_ad = '. '.join(response.xpath(".//div[@class='jobsearch-jobDescriptionText']//text()").extract()).strip()
        job_title = response.css('title::text').extract_first()
        temp_df = pandas.DataFrame({
        'Job Title':[job_title],
        'Job Ad':[job_ad]
        })
        appended_data = pandas.concat([ad_df,temp_df],ignore_index = True, sort = True)
        appended_data.to_csv(filename,index=False)