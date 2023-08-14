#Intended use: help create training data for NLP model
#Takes CSV file full of eng or cs ads and classifies them as
#low, mid, or high level under a column 'Classification'
#if testing the accuracy of this program, set TESTING to True
#if testing this program, the CSV file should have a column
#'Human Classification' containing the correct job level classification
#when testing, program will print overall accuracy score
#and recall and precision scores for low, mid, and high levels
import pandas
import key_words_all as data

FILENAME = 'cs_data_test.csv'
TESTING = True

df = pandas.read_csv(FILENAME)
title_list = df['Job Title'].tolist()
ad_list = df['Job Ad'].tolist()

low_scores = []
mid_scores = []
high_scores = []
low_words = []
mid_words = []
high_words = []
labels = []
num_phrases_list = []

if TESTING:
    human = df['Human Classification'].tolist()

for ad in ad_list:
    ad = ad.lower()
    low_score = 0
    mid_score = 0
    high_score = 0
    low_word_list = []
    mid_word_list = []
    high_word_list = []
    num_phrases = 1
    for phrase in data.list_low_ad:
        if phrase in ad:
            low_score += data.dict_low_ad[phrase]
            low_word_list.append(phrase)
            num_phrases += 1
    for phrase in data.list_medium_ad:
        if phrase in ad:
            mid_score += data.dict_medium_ad[phrase]
            mid_word_list.append(phrase)
            num_phrases += 1
    for phrase in data.list_high_ad:
        if phrase in ad:
            high_score += data.dict_high_ad[phrase]
            high_word_list.append(phrase)
            num_phrases += 1

    low_scores.append((low_score))
    num_phrases_list.append(num_phrases)
    low_words.append(low_word_list)
    mid_scores.append(mid_score)
    mid_words.append(mid_word_list)
    high_scores.append(high_score)
    high_words.append(high_word_list)

index = 0
for title in title_list:
    title = title.lower()
    low_score = low_scores[index]
    mid_score = mid_scores[index]
    high_score = high_scores[index]
    low_word_list = low_words[index]
    mid_word_list = mid_words[index]
    high_word_list = high_words[index]
    num_phrases = num_phrases_list[index]
    label = ''
    for phrase in data.list_low_title:
        if phrase in title:
            low_score += data.dict_low_title[phrase]
            low_word_list.append(phrase)
            num_phrases += 1
    for phrase in data.list_medium_title:
        if phrase in title:
            mid_score += data.dict_medium_title[phrase]
            mid_word_list.append(phrase)
            num_phrases += 1
    for phrase in data.list_high_title:
        if phrase in title:
            high_score += data.dict_high_title[phrase]
            high_word_list.append(phrase)
            num_phrases += 1
    if low_score > mid_score and low_score > high_score:
        label = 'low'
    elif mid_score > low_score and mid_score > high_score:
        label = 'mid'
    elif high_score > low_score and high_score > mid_score:
        label = 'high'
    else:
        label = 'mid'

    low_scores[index] = low_score/num_phrases
    low_words[index] = low_word_list
    mid_scores[index] = mid_score/num_phrases
    mid_words[index] = mid_word_list
    high_scores[index] = high_score/num_phrases
    high_words[index] = high_word_list
    labels.append(label)
    index += 1

if TESTING:
    correct = 0
    total = 0
    for i in range(0, len(human)):
        if human[i].strip() == labels[i].strip():
            correct += 1
        if human[i] != 'irrelevant' and human[i] != 'unclear':
            total += 1
    accuracy = correct/total * 100
    print('Total Relevant Ads: ' + str(total))
    print('Overall Accuracy: ' + str(accuracy) + '%')

    df = pandas.DataFrame({
        'Job Title' : title_list,
        'Job Ad' : ad_list,
        'Human Classification' : human,
        'Classification' : labels,
        'Low Score' : low_scores,
        'Low Phrases' : low_words,
        'Mid Score' : mid_scores,
        'Mid Phrases' : mid_words,
        'High Score' : high_scores,
        'High Phrases' : high_words,
    })
else:
    df = pandas.DataFrame({
    'Job Title' : title_list,
    'Job Ad' : ad_list,
    'Classification' : labels,
    'Low Score' : low_scores,
    'Low Phrases' : low_words,
    'Mid Score' : mid_scores,
    'Mid Phrases' : mid_words,
    'High Score' : high_scores,
    'High Phrases' : high_words,
})

df.to_csv(FILENAME)

if TESTING:
    df = pandas.read_csv(FILENAME)
    answers = df['Human Classification'].tolist()
    answers = [answer.strip() for answer in answers]
    predictions = df['Classification']
    predictions = [prediction.strip() for prediction in predictions]

    CLASSES = [
        'low',
        'mid',
        'high',
    ]

    for CLASS in CLASSES:
        index = 0
        tp = 0
        tn =  0
        fp = 0
        fn = 0

        for answer in answers:
            prediction = predictions[index]
            if answer != 'unclear' and answer != 'irrelevant' and answer != 'french' and answer != 'varying':
                if answer == CLASS and prediction == CLASS:
                    tp += 1
                elif answer == CLASS and prediction != CLASS:
                    fn += 1
                elif answer != CLASS and prediction == CLASS:
                    fp += 1
                elif answer != CLASS and prediction != CLASS:
                    tn += 1
            index += 1

        precision = round(((tp / (tp + fp)) * 100), 2)
        recall = round(((tp / (tp + fn)) * 100), 2)
        fscore = round(((2 * precision * recall)/(precision + recall)), 2)
        print(CLASS + ' precision: ' + str(precision) + '%')
        print(CLASS + ' recall: ' + str(recall) + '%')
        print(CLASS + ' f1 score: ' + str(fscore) + '%')
