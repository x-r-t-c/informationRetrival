import re
import math


#mine
def idf(dark):
    return 1 + math.log(len(dict1)/dict2[dark])


#mine metro
def metro(docu):# docu is dict
    counter = 0
    for wo in docu:
        counter = counter + docu[wo]*docu[wo] # a^2 + b^2.....
    return math.sqrt(counter) # return root


#WILL BE GIVEN
topk = 2

#SHOULD BE SEPARATE EACH TIME
temp_dict = {}
temp_dict1 = {}
temp_dict2 = {}

#url : dictionary (word : tf)
dict1 = {}

#word : number of urls it appears
dict2 = {}

#url : lenght
dict3 = {}


#start experiement docs
print(type(dict1))
p = 'Suillus. luteus is a bolete fungus common in its native Eurasia and widely introduced elsewhere. English ' \
    'such as "slippery jack" refer to the brown cap, which is slimy in wet conditions. The mushrooms are edible, ' \
    'though not highly regarded, and are often eaten in soups, stews or fried dishes. The fungus grows in coniferous ' \
    'forests in its native range, and pine plantations where introduced. It forms symbiotic associations with living ' \
    'trees by enveloping the underground roots. The fungus produces spore-bearing mushrooms above ground in summer ' \
    'and autumn. The cap often has a distinctive conical shape before flattening with age. Instead of gills, ' \
    'the underside of the cap has pores with tubes extending downward that allow mature spores to escape. The pore ' \
    'surface is yellow, and covered by a membranous partial veil when young. The stalk is pale with small dots near ' \
    'the top. It bears a distinctive ring that is tinged brown to violet on the underside. (Full article...) This ' \
    'picture shows a United States Navy recruitment poster from 1917, based on a cartoon by William Allen Rogers (' \
    '1854–1931) published in the New York Herald during World War I. It shows a personified Germany wading through a ' \
    'sea of dead bodies, with the slogan "Only the Navy Can Stop This" below the drawing, presumably a reference to ' \
    'the U-boat campaign and the sinking of civilian ships such as the Lusitania. Rogers was a self-taught artist and' \
    'began submitting political cartoons to Midwestern newspapers during his teens. He was employed for twenty-five ' \
    'years by Harper s Weekly to illustrate the magazine s editorials; this was followed by daily contributions of ' \
    'political cartoons to the New York Herald for twenty years. '
p1 = 'Aboah was born in London, England, to Charles Aboah, a Ghanaian location scout in the fashion industry and ' \
     'former ' \
     'barrister clerk, and Camilla Lowther, a British fashion businesswoman and talent manager. Her maternal ' \
     'grandmother ' \
     'was an American from California, named Lavinia (née Joyce).[2][3] The Lowther family are members of the Brit ' \
     'nobility, headed by the Earl of Lonsdale.[4] Aboah s maternal great-grandfather was Anthony Lowther, Viscount ' \
     'Lowther, the son of Lancelot Lowther, 6th Earl of Lonsdale. She is a grandniece of James Lowther, 7th Earl of ' \
     'Lonsdale.[2] Through her father, she is related to the Ghanaian politician William Kwasi Aboah. Aboah is the ' \
     'younger sister of fashion model and activist Adwoa Aboah and a second cousin of fashion model Matilda Lowther. ' \
     '[5][6] Aboah was educated at Millfield, a boarding school in Somerset, and later obtained an art degree from ' \
     'School of Visual Arts in New York City.'
p2 = 'Aboah is signed with VIVA Model Management and DNA Models.[7] is She had her first modelling job when she was 6 ' \
     'years old, modelling for the brand Jigsaw.[3] She has modelled in advertisement campaigns for Alexander' \
     'and Miu Miu.[7] In 2010 Aboah and her sister were featured in an advertisement campaign for H&M.[9]' \
     's AW17 fashion show.[10] In September 2018, Aboah, alongside her sister, Adwoa, and her cousin, ' \
     'Alewya Demmisse, were photographed by Mario Sorrenti as the faces of MANGOs AW18 campaign TOGETHER.[11][12]  ' \
     'has been featured in Vogue, The Telegraph Magazine, Love,[13] and i-D and has modelled for Marc Jacobs, ' \
     'Michael Kors, and Burberry.[14][15][16][17] She was photographed alongside Kate Moss for Love magazine s LOVE ' \
     '18.[18]' \
     's music video for the song "Sundress".[19]' \
     's Fall 2019 fashion show.[8] In September 2019, Aboah was the face of Links of London'
url = 'www.li.gr'
url1 = 'www.mamba.out'
url2 = 'www.dra.gr'
#END EXPERIEMENT DOCS

#TEXT PREPERATION
r = re.sub(r'[?|$|.|"|(|)|!]', r'', p) #clean text
x = r.lower().split() #split text
x.sort() #not needed
print(x)  #not needed
l = len(x) #num of words
#END OF TEXT PREPERATION


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


#!!!!!!!!!!!!!!!!!DOC TO DICT
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
