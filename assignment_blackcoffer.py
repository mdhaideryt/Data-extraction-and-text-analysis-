#for other links, it is just required to paste that link from excel file named output data structure in ...
#... url(7th line) and change the text file name as mentioned in URL_ID of that excel file. One more thing is...
#... to put proper class name by openeing each link and right clicking on title and content of that webpage ...
#... then go to inspect and put proper classname.
import requests
from bs4 import BeautifulSoup
url = "https://insights.blackcoffer.com/ai-healthcare-revolution-ml-technology-algorithm-google-analytics-industrialrevolution/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    title_element = soup.find('h1',class_="entry-title")  #entry-title #tdb-title-text
    title_text = title_element.get_text()
    content_element = soup.find(class_="td-post-content tagdiv-type")  #td-post-content tagdiv-type
    content_text = content_element.get_text()

    with open('123.txt', 'w', encoding='utf-8') as file:
        file.write(f'{title_text}')
        file.write(content_text)
    print(title_text)
    print(content_text)

t = open('123.txt', 'r', encoding='utf-8')
a=t.readlines()
#print(a)
number_of_sentences=len(a)
#print(number_of_sentences)
t.close()
t = open('123.txt', 'r', encoding='utf-8')
t_list=t.read().split()
print(t_list)
pos=open('positive-words.txt')
neg=open('negative-words.txt')
pos_list=pos.read().split()
neg_list=neg.read().split()
number_of_words=0
positive_score,negative_score=0,0
for i in t_list:
    for j in i:
        if j not in "abcdefghijklmnopqrstuvwxyz":
            i.replace(j," ")
print(t_list)
for i in t_list:
    if i in pos_list:
        positive_score+=1
    if i in neg_list:
        negative_score+=1
    number_of_words+=1
count,number_of_complex_words=0,0
for i in t_list:
    if (i[-1]=='s' and i[-2]=='e') or (i[-1]=='d' and i[-2]=='e'):
        continue
    for j in i:
        if j in "aeiou":
            count+=1
            if count>2:
                number_of_complex_words+=1
                continue
print(f"positive score={positive_score}")
print(f"negative score={negative_score}")
polarity_score=(positive_score-negative_score)/((positive_score+negative_score)+0.000001)
print(f"polarity score={polarity_score}")
total_Words_after_cleaning=number_of_words/number_of_sentences
#print(f"total_Words_after_cleaning={total_Words_after_cleaning}")
Subjectivity_Score = (positive_score + negative_score)/ ((total_Words_after_cleaning) + 0.000001)
print(f"Subjectivity_Score={Subjectivity_Score}")
average_sentence_length=number_of_words/number_of_sentences
print(f"average_sentence_length={average_sentence_length}")
percentage_of_complex_words=number_of_complex_words/number_of_words
print(f"percentage_of_complex_words={percentage_of_complex_words}")
fog_index=0.4*(average_sentence_length+percentage_of_complex_words)
print(f"fog_index={fog_index}")
average_number_of_words_per_sentence=number_of_words/number_of_sentences
print(f"average_number_of_words_per_sentence={average_number_of_words_per_sentence}")
print(f"complex_word_count={number_of_complex_words}")
print(f"word_count={number_of_words}")
print(f"syllable per word={percentage_of_complex_words}")
pos.close()
neg.close()
t.close()

import re
words_to_count = ["I", "we", "my", "ours", "us"]
word_counts = {word: 0 for word in words_to_count}
with open('123.txt', 'r',encoding='utf-8') as file:
    t_list = file.read()
    for word in words_to_count:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        matches = pattern.finditer(t_list)
        for match in matches:
            word_counts[word] += 1
total_count = sum(word_counts.values())
print(f'personal_pronoun_Count: {total_count}')

total_number_of_characters=0
for i in t_list:
    for j in i:
        total_number_of_characters+=1
average_word_length=total_number_of_characters/number_of_words
print(f"average_word_length={average_word_length}")

print(positive_score)
print(negative_score)
print(polarity_score)
print(Subjectivity_Score)
print(average_sentence_length)
print(percentage_of_complex_words)
print(fog_index)
print(average_number_of_words_per_sentence)
print(number_of_complex_words)
print(number_of_words)
print(percentage_of_complex_words)
print(total_count)
print(average_word_length)




