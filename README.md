# Gender-Decoder-Project
Gender Decoder Project 101
Ella Palter

In case this is helpful for the future completion of the gender decoder project I have written out the steps I took to collect the data from June – August 2022.

Part 1: AD Collection

1.	Get relatively familiar with Scrapy by watching some YouTube tutorials. 

2.	There are two spiders included in the code I’ve sent you: ‘testing_ads.py’ and ‘testing_webs.py’

a.	Run ‘testing_webs.py’ first. This python file uses scrapy to collect a series of URLs that each leads to a single job ad. This code must run once for each ‘category’ of job ad you’d like to collect. Each job ‘category’ also needs a respective text file to write the URLs to.
b.	Run ‘testing_ads.py’ once the links are collected. This python file goes into each of the URLs collected by the previous scraper to grab the job title and description and write it to a csv file. Each job ‘category’ needs a respective csv file to write the data to. 
*When running the scrapy code make sure everything is in the right directory. If you run the code under the biggest ‘parent’ folder in the scrapy project everything should be fine.

Part 2: Decoding

There are two python files called ‘component_titles.py’ and ‘comp_split.py’. Together these files split each ad into qualifications, description, and responsibilities and create new csv files for each. The following steps can be done before or after splitting the ads into their components. If you want the decoder data for both the whole ads and the ads split into their components repeat the following steps twice (once on the whole ad csv’s and once on each of the component csv’s).

1.	Run the python file ‘decoder.py’. This will determine if the ad is feminine, masculine, neutral, or nothing for each decoder. 

2.	Run the python file ‘word_count.py’. This code counts the number of appearances of the words in the file ‘gendered_words.csv’ in all of the ads and writes the data under a column called Count of word.

3.	Make sure ‘word_strength.py’ is in the same directory as where you’re running the code and run ‘word_score.py’. This code weights each word differently (as per the strengths in ‘word_strength.py’) and writes their weighted score under the column called “Word Scores’. 

4.	Run ‘gender_percentage.py’ to get a summary of what percentage of the ads in a particular csv file are masculine, feminine, neutral, or nothing. This file must be run once for each csv file. 

5.	Run the python file ‘make_graphs.py’. This file creates a chart containing the top 20 words found in each csv file. 

![image](https://user-images.githubusercontent.com/110196682/186507840-6bf03186-cc52-49cb-97bc-641c7bca9414.png)
