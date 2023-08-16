# GeoPolitical Analysis

If needed, the code in this folder can separate ads by geographical region, population size of city, and political party of city and create a summary of the percentage of these ads labelled female-associated, male-associated, and neutral.

1.  Run the file 'classify.py'. This file takes CSV files with ads that have already been analyzed by 'decoder.py' (in the 'AnalysisFiles' folder). To change which CSV files will be analyzed, edit the 'FILENAMES' variable. Ensure 'cities.csv' is in the same directory before running this code. This code adds the city of the ad under 'City', the population size of the city under 'Size', the political party of the city under 'Political Stance', and the geographical region under 'Region'.
*  Note that 'cities.csv' might have to be updated when analyzing new ads, as this file does not contain every single city in Canada.
*  Population size classification criteria comes from: https://www.statcan.gc.ca/en/subjects/standard/pcrac/2016/introduction
*  Population data comes from: https://www12.statcan.gc.ca/census-recensement/index-eng.cfm
*  Political Electoral District finder: https://www.elections.ca/scripts/vis/FindED?L=e&PAGEID=20
*  2021 Election Results: https://www.elections.ca/res/cir/maps2/map.asp?map=ERMap_44&lang=e (if the city had multiple ridings, the party with the majority of the ridings was chosen)

2.  Run the file 'separate.py'. This file takes the CSV files that were analyzed by 'classify.py' and separates each ad into a separate CSV file based on geographical region, city population size, and the political party of the city.
