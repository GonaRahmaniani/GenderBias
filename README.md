# Gender-Decoder-Project
Gender Decoder Project 101
Ella Palter

In case this is helpful for the future completion of the gender decoder project I have written out the steps I took to collect the data from June – August 2022. (updated 2023 by Norah Seigel)

Part 1: AD Collection (ScrapingFiles)

1.  In order to run the code to scrape the ads, several libraries need to be installed which can be done via anaconda or terminal. These libraries include: git, matplotlib, numpy, pandas, playwright.

3.	There are two files included in the code I’ve sent you: ‘scrape_urls.py’ and ‘scrape_ads.py’ which will be used to scrape the data from Indeed.

a.	Run ‘scrape_urls.py’ first. This python file uses a headed browser to collect a series of URLs each leading to a single job ad. This code must run once for each ‘category’ of job ad you’d like to collect. This code can be run multiple times per category to maximize the amount of URLs collected. Change the 'FILENAME' variable to the file containg the correct URLs (which the new URLs will be saved to), and 'START_URL' to the URL with the correct search query.

b.	Run ‘scrape_ads.py’ once the links are collected. This python file goes into each of the URLs collected by the previous scraper to grab the job title and description and write it to a csv file. Each job ‘category’ needs a respective csv file to write the data to, and txt file to grab the URLs from. These can be changed using the 'CSVFILENAME' and 'TXTFILENAME' variables respectively.

Part 2: Decoding (AnalysisFiles)

There are two python files called ‘component_titles.py’ and ‘comp_split.py’. Together these files split each ad into qualifications, description, and responsibilities and create new csv files for each. To specify which files contain the ads edit the 'FILENAMES' variable. The following steps can be done before or after splitting the ads into their components. If you want the decoder data for both the whole ads and the ads split into their components repeat the following steps twice (once on the whole ad csv’s and once on each of the component csv’s). Multiple files may also be specified in the 'FILENAMES' variables to analyze multiple files at once.

1.	Run the python file ‘decoder.py’. Ensure 'allwords2.py' is in the same directory. This will determine if the ad is feminine, masculine, neutral, or nothing for each decoder. This file will also remove duplicate job ads and components containing no text. To specify which files to decode edit the 'FILENAMES' variable. This file may take a while (several minutes!) to run if analyzing multiple files.

2.	Make sure ‘word_strength.py’ is in the same directory as where you’re running the code and run the python file ‘word_count.py’. This code counts the number of appearances of the words in the file ‘gendered_words.csv’ in all of the ads and writes the data under a column called Count of word. This code also weights each word differently (as per the strengths in ‘word_strength.py’) and writes their weighted score under the column called “Word Scores’. To specify which files to analyze edit the 'FILENAMES' variable. This file may also take a while to run if analyzing multiple files.

3.	Run ‘gender_percentage.py’ to get a summary of what percentage of the ads in a particular csv file are masculine, feminine, neutral, or nothing. To specify which files to be included in the final chart edit the 'FILENAMES' variable. Add the corresponding description to the 'DESCRIPTIONS' list at the same index.

4.	Run the python file ‘common_words_charts.py’. This file creates a chart containing the top 20 words found in each csv file. To specify which files to analyze edit the 'FILENAMES' variable.

5.	Run the python file 'strength_count.py'. This file calculates the percentage of gendered words per word count for each ad and puts it under the columns 'Feminine Strength per total' and 'Masculine Strenght per total'. Each ad is then put into different 'bins' with different percentage ranges and these bins are placed under the columns 'Fem total bins' and 'Masc total bins'. Edit the 'FILENAMES' variable to specify which files should be analyzed.

6.	Run the python file 'word_percentage.py'. This file calculates the percentage of ads each gendered word appears in and places this under the columns 'Percentage of Ads Containing Feminine Word' and 'Percentage of Ads Containing Masculine Word'. Edit 'FILENAMES' variable to specify the files to be analyzed.

7.	Run the python file 'word_percentage_top.py'. This file grabs the top 20 words per gender that appear in the highest percentage of ads and put them into two separate csv files (one for feminine and one for masculine). Edit 'FILENAMES' to specify which files to analyze.

Part 3: Making Graphs (GraphFiles)

There are multiple files that are used to create graphs using matplotlib.

1.  Run the file 'common_words_graph.py'. This file grabs the data from the charts that were created using 'common_word_charts.py' and turns them into graphs using matplotlib. The graphs are stored in PNG files. To specify which files to use, edit the 'FILENAMES' variable.

EXAMPLE:
![common_words_eng_2023](https://github.com/nseigel/Gender-Decoder-Project/assets/105315630/0f5ecde7-003d-4f43-8ae8-768aa0b036fa)

3.  The next file, 'percentage_graph.py' uses data from the csv file that was created using the file 'gender_percentage.py'. This file can be run once using the whole file or multiple times after splitting the file into different categories (such as nursing ads, qualification components, etc.). To specify which file should be used to create the graph, edit the 'FILENAMES' variable. Run the file 'percentage_graph.py'. This will create a stacked bar chart for the data in the specified csv file showing the percentage of ads labelled Feminine, Neutral, or Masculine.

EXAMPLE:
![total_gender_percentage](https://github.com/nseigel/Gender-Decoder-Project/assets/105315630/05b6b2e3-e193-44ac-9022-e7c268f42914)

5.  Run the file 'word_bins_graph.py' This file creates graphs using the data that was calculated previously with 'strength_count.py'. Edit the 'FILENAMES' variable to specify which files to create graphs with.

EXAMPLE:
![eng_word_bins](https://github.com/nseigel/Gender-Decoder-Project/assets/105315630/06a17960-3662-4409-ad4e-38a85927db22)

7.  The file 'word_percentage_graph.py' runs once for Feminine words and once for Masculine words. This file grabs the data from the charts created previously with 'word_percentage_top.py' and grabs the words that appear in all three charts, turning the data into graphs. This file creates one graph for feminine words and one graph for masculine words. To specify which files contain the correct data edit the 'NAMES' dictionary. Index 0 contains information for the graph title, and indexes 1, 2, and 3 contain the engineering, computer science, and nursing data files respectively.

EXAMPLE:
![fem_word_percentage](https://github.com/nseigel/Gender-Decoder-Project/assets/105315630/b2b89bff-091b-4e81-936b-405abee8470e)

