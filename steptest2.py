import io
import string

print "Enter 0 when you're done entering words.   "
wordList = []
t = True
while (t == True):
    user_input = raw_input("Enter a set of letters for processing:   ")
    if (user_input != '0'):
        wordList.append(user_input)
    else:
        t = False

text = open("/usr/share/dict/words")
dict_words = {}
for i in text:
    #this sorts the letters in the word
    j = string.join(sorted(i.strip())).replace(' ', '')

    if j in dict_words:
        dict_words[j].append(i)
    else:
        dict_words[j] = []
        dict_words[j].append(i)
text.close()

#this will output the possible combinations
for i in wordList:
    sortedLetters = string.join(sorted(i.strip())).replace(' ', '')
    if (sortedLetters in dict_words):
        s = string.join(dict_words[sortedLetters]).replace(' ', '\t')
        print i + " can be:\n\t" + s
