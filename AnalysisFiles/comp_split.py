#give it a list of csv files with whole ads
#splits into components
#ensure component_titles.py is in same directory

import pandas
from component_titles import job_qual, job_respon
import string

#files containing ads that will be split into components
FILENAMES = [
    'cs_data.csv',
    'eng_data.csv',
    'nurse_data.csv',
]

def clean(s):
    ss = "".join((char for char in s if char not in string.punctuation))
    ss = ss.lower()
    ss = ss.strip()
    return ss

for file in FILENAMES:
    filename = file
    df = pandas.read_csv(filename)

    ads_list = df["Job Ad"].tolist()
    desc = []
    resp = []
    qual = []

    for ad in ads_list:
        l = str(ad).split('.')
        l2 = []
        for line in l:
            l2 = l2 + line.splitlines()

        lines = []
        for line in l2:
            lines.append(clean(line))

        line_itr = iter(lines)
        x = next(line_itr, None)

        d_list = []
        q_list = []
        r_list = []

        d_num = [0,-1]
        q_num = [-1,-1]
        r_num = [-1, -1]
        d2_num = [-1, -1] #in case desc comes at end
        qual_first = False #keep track of if qualifications are listed first
        counter = 0
        end = len(lines)-1

        while (x is not None and d_num[1]==-1):
            #print(x)
            if any(qual in x for qual in job_qual):
                d_num[1] = counter
                q_num[0] = counter
                qual_first = True
            elif any(res in x for res in job_respon):
                d_num[1] = counter
                r_num[0] = counter
                qual_first = False
            x = next(line_itr, None)
            counter += 1

        if (qual_first):
            while (x is not None and q_num[1]==-1):
                #print(x)
                if any(res in x for res in job_respon):
                    q_num[1] = counter
                    r_num[0] = counter
                x = next(line_itr, None)
                counter += 1
        else:
            while (x is not None and r_num[1]==-1):
                #print(x)
                if any(qual in x for qual in job_qual):
                    r_num[1] = counter
                    q_num[0] = counter
                x = next(line_itr, None)
                counter += 1

        if (qual_first):
            while (x is not None and r_num[1]==-1):
                #print(x)
                if ("description" in x):
                    r_num[1] = counter
                    d2_num[0] = counter
                x = next(line_itr, None)
                counter += 1
        else:
            while (x is not None and q_num[1]==-1):
                #print(x)
                if ("description" in x):
                    q_num[1] = counter
                    d2_num[0] = counter
                x = next(line_itr, None)
                counter += 1

        if (d2_num[0]!=-1):
            d2_num[1] = end
        else:
            if (qual_first):
                r_num[1] = end
            else:
                q_num[1] = end

        '''
        print(d_num)
        print(r_num)
        print(q_num)
        print(d2_num)
        print("-------------")
        '''
        d_list = l2[0:d_num[1]]
        q_list = l2[q_num[0]:q_num[1]]
        r_list = l2[r_num[0]:r_num[1]]
        #if there was a second description
        if (d2_num[0]!=-1):
            d_list.append(l2[d2_num[0]:d2_num[1]])

        desc.append(d_list)

        qual.append(q_list)

        resp.append(r_list)

    df["Description"] = desc
    df["Qualifications"] = qual
    df["Responsibilities"] = resp

    d_file = filename.strip(".csv") + "_d.csv"
    q_file = filename.strip(".csv") + "_q.csv"
    r_file = filename.strip(".csv") + "_r.csv"

    df.to_csv(d_file, index=False,columns=["Job Title","Description"], header=["Job Title", "Job Ad"])
    df.to_csv(q_file, index=False,columns=["Job Title","Qualifications"], header=["Job Title", "Job Ad"])
    df.to_csv(r_file, index=False,columns=["Job Title","Responsibilities"], header=["Job Title", "Job Ad"])

