# GeoPolitical Analysis

If needed, the code in this folder can separate ads by geographical region, size of city, and political party of city and create a summary of the percentage of these ads labelled female-associated, male-associated, and neutral.

1.  Run the file 'classify.py'. This file takes CSV files with ads that have already been analyzed by 'decoder.py' (in the 'AnalysisFiles' folder). To change which CSV files will be analyzed, edit the 'FILENAMES' variable. Ensure 'cities.csv' is in the same directory before running this code. This code adds the city of the ad under 'City', the population size of the city under 'Size', the political party of the city under 'Political Stance', and the geographical region under 'Region'.
*  Note that 'cities.csv' might have to be updated when analyzing new ads, as this file does not contain every single city in Canada.
*  Population size classification criteria comes from: https://www.statcan.gc.ca/en/subjects/standard/pcrac/2016/introduction
*  Population data comes from: https://www12.statcan.gc.ca/census-recensement/index-eng.cfm
*  Political Electoral District finder: https://www.elections.ca/scripts/vis/FindED?L=e&PAGEID=20
*  2021 Election Results: https://www.elections.ca/res/cir/maps2/map.asp?map=ERMap_44&lang=e (if the city had multiple ridings, the party holding the majority of the ridings was chosen)

2.  Run the file 'separate.py'. This file takes the CSV files that were analyzed by 'classify.py' and places each ad into a new CSV file based on geographical region, city population size, and the political party of the city. To change which CSV files will be analyzed edit the 'FILENAMES' variable. This code will create sixteen new CSV files, one for each region, population size, and political party, containing the corresponding ads.

3.  Run the file 'percentage_chart_geo.py'. This file takes each of the sixteen CSV files created in step 2 and creates 3 new CSV files. Each CSV file contains a summary of the percentage of ads labelled female-associated, male-associated, and neutral for geographical regions, population size, and political affiliations (one CSV file for each category).

4.  Run the file 'graph_geo.py'. This file creates three stacked bar charts showing the percentage of ads labelled female-associated, male-associated, and neutral for each CSV file that was created in step 3

EXAMPLE:
![region_gender](https://github.com/nseigel/Gender-Decoder-Project/assets/105315630/63701d12-bc3b-4595-9cf1-e291d4000fa3)
