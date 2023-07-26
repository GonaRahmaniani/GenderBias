#automates word counting for ads in a .csv file
#we have 7 decoders; decoders 1 and 6 are identical, as are 3 and 5
#note that in decoder 7, an ad is never masculine unless there are
#considerably more masculine words; it may consider an ad with
#no female words to be fem/neutral

import pandas
import allwords2 as allwords #wordlists for our decoders
import re

def decode(ad, fem_list, masc_list, isScore=False, isEploy=False, isTotal=False, isBeapplied=False, isBruin=False):
    #print("ad: %s\n\n" % ad)
    #print("AD # = %d" % counter)
    f_counter = 0
    f = 0
    m_counter = 0
    m = 0
    wc = 0
    track = 0 #keep track of what word we're on
    words = ad.split()
    split = [] # a list of all words in the ad

    for word in words:
        split = split + (re.split('\W+', word)) #split by punctuation

    for word in split:
        word = word.lower()
        #if (word!=''):
            #wc += 1 #count number of words
        #print("Current word: %s" % word)
        found = False

        if (found == False):
            for fem_word in fem_list: #checks fragments
                #if (isEploy==False):
                if word.startswith(fem_word):
                    #f_counter += 1
                    found = True
                    if (isEploy == True):
                        if (word not in f_words):
                            f_counter += 1
                            f_words.append(word)
                    elif (isTotal == True):
                        if (word.startswith('responds') or word.startswith('interpersonal') or word.startswith('responsible') or word.startswith('committee')):
                            f_counter += 2
                            f_words.append(word)
                        else:
                            f_counter += 1
                            f_words.append(word)
                    elif (isBeapplied == True):
                        if (word.startswith('sharepoint') or word.startswith('committee') or word.startswith('collaborations') or word.startswith('shareable') or word.startswith('trustworthiness') or word.startswith('dependent') or word.startswith('responsibly') or word.startswith('dependency') or word.startswith('honestly')):
                            f_counter += 0
                        elif (word.startswith('she') and word!='she'):
                            f_counter += 0
                        else:
                            f_counter += 1
                            f_words.append(word)
                    elif (isBruin == True):
                        if (word.startswith('interpersonal') or word.startswith('inter-personal')):
                            f_counter += 2
                        else:
                            f_counter += 1
                            f_words.append(word)
                    else:
                        f_counter += 1
                        f_words.append(word)
                    #print(word)
                    break
                '''else:
                    if (word in fem_word):
                        f_counter += 1
                        found = True
                        f_words.append(word)
                        #print(word)
                        break
'''
        if (found == False):
            for masc_word in masc_list:
                #if (isEploy==False):
                if word.startswith(masc_word):
                    #m_counter += 1
                    found = True
                    if (isEploy == True):
                        if (word not in m_words):
                            m_counter +=1
                            m_words.append(word)
                    elif (isTotal == True):
                        if (word.startswith('analytical')):
                            m_counter += 2
                            m_words.append(word)
                        elif (word.startswith('determinants') or word.startswith('individuali') or word.startswith('competency') or word.startswith('confidential') or word.startswith('individuals') or word.startswith('analytically') or word.startswith('analyzers') or word.startswith('objectives') or word.startswith('actively')):
                            m_counter += 0
                        else:
                            m_counter +=1
                            m_words.append(word)
                    elif (isBeapplied== True):
                        if (word.startswith('competencies') or word.startswith('decisions') or word.startswith('competition') or word.startswith('analyzer') or word.startswith('objectives') or word.startswith('actively') or word.startswith('individually') or word.startswith('confidential') or word.startswith('competency') or word.startswith('athletes') or word.startswith('logical')):
                            m_counter += 0
                        else:
                            m_counter +=1
                            m_words.append(word)

                    else:
                        m_counter +=1
                        m_words.append(word)
                    #print(word)
                    break
                    '''
                else:
                    if (word in masc_word):
                        m_counter += 1
                        found = True
                        m_words.append(word)
                        #print(word)
                        break
'''
        #if (found == False) and (isThree==True or isScore==True):
        #    if word.endswith("est"):
        #        m_counter += 1
        #        m_words.append(word)

        if (found == True):
            if (track == 0): #if the first word in the ad is gendered
                phrase = word + " " + split[1] #context is 2 words
            elif (track == len(split)-1): #if the last word in the ad is gendered
                phrase = split[track-1] + " " + word #context is 2 words
            else:
                phrase = split[track-1] + " " + word + " " + split[track+1] #context is 3 words
            c_text.append(phrase) #add context phrase to list

        #debugging statements
        #print("f: %d" % f_counter)
        #print("m: %d" % m_counter)

        track += 1 #increment word counter

    if (isScore == True): #our scoring parameters; only do once per ad
        sentence = ad.split()
        word_count.append(len(sentence)) #count words once

    #calculate numeric value; +1.0 for female, -1.0 for male, divided by total
    if (f_counter + m_counter > 0):
        calc = (f_counter - m_counter)/(f_counter + m_counter)
    else:
        calc = 0.0000

    fc_list.append(f_counter)
    mc_list.append(m_counter)

    #compare results!
    if (isEploy==False):
        if (f_counter > m_counter):
            return ("Female", round(calc,4))
        elif ((f_counter == 0) and (m_counter == 0)):
            return ("Nothing", round(calc,4))
        elif (f_counter == m_counter):
            return ("Neutral", round(calc,4))
        else:
            return ("Male", round(calc,4))
    else:
        if (f_counter >= m_counter-2):
            return ("Female/Neutral", round(calc,4))
        else:
            return ("Male", round(calc,4))

#pull wordlists
dec1_f = allwords.list1_f #decoder 1
dec1_m = allwords.list1_m

dec2_f = allwords.list2_f #decoder 2
dec2_m = allwords.list2_m

dec3_f = allwords.list3_f #decoder 3 and 5
dec3_m = allwords.list3_m

dec4_f = allwords.list4_f #decoder 4
dec4_m = allwords.list4_m

dec6_f = allwords.list6_f #decoder 6 BRUIN
dec6_m = allwords.list6_m

dec7_f = allwords.list5_f #decoder 7
dec7_m = allwords.list5_m

score_f = allwords.superset_f #our superset for scoring
score_m = allwords.superset_m

true='y'

while true=='y':

    #pull ads
    filename = input("Enter .csv file with ads: ")
    ads_df = pandas.read_csv(filename)
    ads_df = ads_df.drop_duplicates()
    #get column of ad text
    #ads_list = ads_df["Job Ad"].tolist()
    ads_list = [x for x in ads_df["Job Ad"] if str(x) != 'nan']

    #decode!
    results_1 = []
    results_2 = []
    results_3 = [] #and 5
    results_4 = []
    results_6 = []
    results_7 = []
    fc_list = []
    mc_list = []
    score_decoder = []

    word_count = []
    #stores the words for each ad
    masc_words = []
    fem_words = []
    context = []

    #for working with each ad;
    m_words = []
    f_words = []
    c_text = []
    f_counter = 0
    m_counter = 0

    #counter = 0 #keeps track of what ad we're on
    for ad in ads_list:
        #reset lists
        f_words.clear()
        m_words.clear()
        c_text.clear()
        #counter += 1
        #score_decoder.append(decode(ad, score_f, score_m, isScore=True))
        #store only score decoder words
        #masc_words.append(m_words[:])
        #fem_words.append(f_words[:])
        #context.append(c_text[:])

        #decoder 1 and 6
        results_1.append(decode(ad, dec1_f, dec1_m, isScore=True))
        #decoder 2
        results_2.append(decode(ad, dec2_f, dec2_m, isTotal=True))
        #decoder 3 and 5
        #results_3.append(decode(ad, dec3_f, dec3_m, isThree=True))
        #decoder 4
        results_4.append(decode(ad, dec4_f, dec4_m, isBeapplied=True))
        #decoder 6
        results_6.append(decode(ad, dec6_f, dec6_m, isBruin=True))
        #decoder 7
        #results_7.append(decode(ad, dec7_f, dec7_m, isEploy=True))
        masc_words.append(m_words[:])
        fem_words.append(f_words[:])
        context.append(c_text[:])
        '''
        #store all decoder words
        masc_words.append(m_words[:])
        fem_words.append(f_words[:])
        context.append(c_text[:])
        print("\n")
        print("MASC WORDS:")
        print(masc_words)
        print("FEM WORDS:")
        print(fem_words)
        print("\n\n-------------------------------------------------")
        '''

    ads_df["Decoder 1"] = pandas.Series(results_1)
    ads_df["Decoder 2"] = pandas.Series(results_2)
    #ads_df["Decoder 3"] = pandas.Series(results_3)
    ads_df["Decoder 4"] = pandas.Series(results_4)
    #ads_df["Decoder 5"] = pandas.Series(results_3)
    ads_df["Decoder 6"] = pandas.Series(results_6)
    #ads_df["Decoder 7"] = pandas.Series(results_7)
    #ads_df["Scoring Decoder"] = pandas.Series(score_decoder)
    ads_df["Feminine words"] = pandas.Series(fem_words)
    ads_df["Masculine words"] = pandas.Series(masc_words)
    ads_df["Context"] = pandas.Series(context)
    #total number of words
    ads_df["Word count"] = pandas.Series(word_count)
    #ads_df["f_counter"] = pandas.Series(fc_list)
    #ads_df["m_counter"] = pandas.Series(mc_list)

    #debugging; check a specific ad
    #print(decode(ads_list[203], dec1_f, dec1_m, isThree=False))

    if (input("Write results to working .csv file? (y/n) ")=='y'):
        ads_df.to_csv(filename,index=False)

    true=input("do it again? (y/n)")
