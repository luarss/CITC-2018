# CITC Python B

# Done by:
# Luar Shui Song

# Requirements: First letter of 2nd word = last letter of 1st word
# Valid word (inside txt)
# Not used before
# make sure word_list.txt in the same directory as this file

import time
import pandas as pd   # Pandas parser is much faster than f.open()

start = time.time()

# import file here
f = pd.read_csv("word_list.txt", sep = '\n', header = None)
num = len(f.index)
df = pd.DataFrame(pd.Series(range(1,num+1)), None, ['1'])
# joining the word column with a seprate index column for tracking whether a word is used
f = pd.concat([f,df], axis = 1)  
end = time.time()

print('loading of dictionary done. Took %s seconds' % (end - start))

def wordUsed(word):
    # word_arr gives us the array (if a match is found)
    word_arr = f[f[0]==word]
    index = word_arr.index.tolist() # assume no duplicates
    used = False
    notfound = False
    if not word_arr.empty and int(f.loc[index,'1']) is not 0:
        # word found, not used yet
        f.loc[index, '1'] = 0
        return used,notfound
    if not word_arr.empty and int(f.loc[index, '1']) is 0:
        # word found, used
        used = True
        return used,notfound
    if word_arr.empty:
        # word not found
        notfound = True
        return used,notfound

past = '' # token character
j = False

while True:
    current = input('Please type a word: ')
    used, notfound=wordUsed(current)
    if used:
        print('You typed a word that has been typed before.')
        break
    if current[0] is not past[-1:] and j:
        print('You didn\'t type a word starting with \'%s\'' %past[-1:])
        break
    if notfound:
        print('You didn\'t type a word found in word_list.txt.')
        break
    j = True
    past = current
    

    
    


