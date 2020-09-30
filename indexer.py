import re
import math

# url : dictionary (word : tf)
dict1 = {}

# word : number of urls a word appears in
dict2 = {}


# idf calculation
def idf(word):
    return 1 + math.log(len(dict1)/dict2[word])


# metro
def metro(docu):  # docu is dict
    counter = 0
    for word in docu:
        counter = counter + docu[word]*docu[word]  # a^2 + b^2.....
    return math.sqrt(counter)  # return root


def indexing_data(data):
    for url in data:
        update_data(url, data[url])


def update_data(url, paragraph):
    temp_dict = {}  # TEMPORAL DICTIONARY
    # TEXT PREPARATION
    para = str(paragraph)
    cleaner = ";.,:${}[]'&*()^%$#@!"
    for char in cleaner:
        para = para.replace(char, "")
    clean_p = re.sub(r'[?|+$."()!]', r'', para)  # clean text
    x_par = clean_p.lower().split()  # split text
    no_w = len(x_par)  # num of words
    # DOC TO DICT (ανεστραμένος καταλογος)
    for word in x_par:  # for each word in doc
        if word in temp_dict:  # if not the first time the word is found in this doc
            temp_dict[word] = temp_dict[word] + 1/no_w  # add to term frequency
        else:  # if the first time
            if word in dict2:  # if the word appeared in any other docs
                dict2[word] = dict2[word] + 1  # increase docs with this word in it counter
            else:  # if first encounter with the word
                dict2.update({word: 1})
            temp_dict.update({word: 1/no_w})
    dict1.update({url: temp_dict})  # store dictionary for further use


def query_processor(query):
    # query processing
    query_dict = {}  # query temp dict
    cleaner = ";.,:${}[]'&*()^%$#@!"
    for char in cleaner:
        query = query.replace(char, "")
    clean_query = re.sub(r'[?|$."()!]', r'', query)  # clean text
    xquery = clean_query.lower().split()  # split text
    no_query = len(xquery)  # number of words in query
    for word in xquery:
        if word in query_dict:
            query_dict[word] = query_dict[word] + 1 / no_query
        else:
            query_dict.update({word: 1 / no_query})
    # cosine tf/idf dict
    sim = {}
    # cosine tf/idf calc for all urls in dict1
    temp_query = metro(query_dict)  # calculating only once
    for di in dict1:  # for each url(doc)
        nominator = 0
        temporal = dict1[di]  # get the dict
        for word in xquery:  # for word in query
            if word in temporal:  # if in examined dict
                nominator = nominator + idf(word) * temporal[word] * query_dict[word]  # add idf* tf in doc *tf in query
        if nominator > 0:  # if nothing is found, don't enter
            denominator = metro(temporal) + temp_query  # denominator
            sim.update({di: nominator / denominator})  # score of url match
    # sort depending on query
    # make dict to list sort it and back to dict
    top_similarity = dict((value, key) for (key, value) in (sorted((1 - value, key) for (key, value) in sim.items())))
    return top_similarity


"""

#WILL BE GIVEN
topk = 2

#SHOULD BE SEPARATE EACH TIME
#temp_dict = {}
temp_dict1 = {}
temp_dict2 = {}



#url : lenght
dict3 = {}




#TEXT PREPARATION
r = re.sub(r'[?|$|.|"|(|)|!]', r'', p) #clean text
x = r.lower().split() #split text
x.sort() #not needed
print(x)  #not needed
l = len(x) #num of words
#END OF TEXT PREPARATION


print(l)
r1 = re.sub(r'[?|$|.|"|(|)|!]', r'', p1)
x1 = r1.lower().split()
x1.sort()
print(x1)
l1 = len(x1)
print(l1)
r2 = re.sub(r'[?|$|.|"|(|)|!]', r'', p2)
x2 = r2.lower().split()
x2.sort()
print(x2)
l2 = len(x2)
print(l2)


#DOC TO DICT
for word in x: # for each word in doc
    if word in temp_dict: #if not hte first time the word is found in this doc
        temp_dict[word] = temp_dict[word] + 1/l # add to term frequency
    else: #if the first time 
        if word in dict2: #if the word appeared in any other docs
            dict2[word] = dict2[word] + 1 #increase docs with this word in it counter
        else: #if first encounter with the word
            dict2.update({word: 1})
        temp_dict.update({word: 1/l})
print(temp_dict)#not needed
print(dict2)#not needed
dict3[url] = l #update dict url with the size of words of url

dict1.update({url: temp_dict}) #store dictionary for further use
# EO DOC tO DICT


for w in x1:
    if w in temp_dict1:
        temp_dict1[w] = temp_dict1[w] + 1/l
    else:
        if w in dict2:
            dict2[w] = dict2[w] + 1
        else:
            dict2.update({w: 1})
        temp_dict1.update({w: 1/l})
print(temp_dict1)
print(dict2)
dict3[url1] = l1

dict1.update({url1: temp_dict1})

for w in x2:
    if w in temp_dict2:
        temp_dict2[w] = temp_dict2[w] + 1/l
    else:
        if w in dict2:
            dict2[w] = dict2[w] + 1
        else:
            dict2.update({w: 1})
        temp_dict2.update({w: 1/l})
print(temp_dict2)
print(dict2)
dict3[url2] = l2

dict1.update({url2: temp_dict2})

print(dict1)

#querry proccessing
qdict = {} # querry temp dict
q = 'is aboah september bolete september'
xq = q.lower()
xq = xq.split()
lq = len(xq)
print(xq)
for w in xq:
    if w in qdict:
        qdict[w] = qdict[w] + 1/lq
    else:
        qdict.update({w: 1/lq})
print(qdict)

#cosine tf/idf dict
fa = {}

#cosine tf/idf calc for all urls in dict1
tempquerry = metro(qdict)
for di in dict1: # for each url(doc) 
    nominator = 0
    denominator = 0
    temporal = dict1[di] #get the dict
    for w in xq: #for word in querry
        if w in temporal: #if in examined dict
            nominator = nominator + idf(w)*temporal[w]*qdict[w] # add idf * tf in doc * tf in querry
    if nominator > 0: # if nothing is found dont enter
        denominator = metro(temporal) + tempquerry # denominator 
        fa.update({di: nominator/denominator}) #score of url match


#sort depending on querry
#make dict to list sort it and back to dict
ta = dict((value, key) for (key, value) in (sorted((1-value, key) for (key, value) in fa.items())))

#top-k
for w in ta: #shows topk results
    if topk > 0:
        print(w)
        topk = topk-1
    else:
        break


"""
