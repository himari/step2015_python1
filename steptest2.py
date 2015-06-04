import io
import string

#this first part will collect words from the user
print "Enter 0 when you're done entering words.   "
wordList = []
t = True
while (t == True):
    user_input = raw_input("Enter a set of letters for processing:   ")
    if (user_input != '0'):
        wordList.append(user_input)
    else:
        t = False

#this will make a hash table of words in the dictionary;
#each entry will be an array of words that have the same set of letters,
#and the key to each entry will be a sorted set of those letters.
text = open("/usr/share/dict/words")
dict_words = {}
for i in text:
    #this sorts the letters in the word
    j = string.join(sorted(i.strip())).replace(' ', '')
    #check to see if there is an entry for that sorted letter set;
    #if there is, then append the current word to the array of other
    #words that have those same letters; if not, make a new entry in
    #the hash table and make the word the first entry in the new array.
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
