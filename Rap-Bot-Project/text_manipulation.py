import nltk
import re

def censor(sent):
    """Censors sentence, returns sentence censored"""
    censoredRegex = [("f[a-z][a-z]k","f**k"),("nigg\w+","*****"),("shit","poop"),("fag","***"),("bitch","*****"),("pussy","*****")]
    for censored in censoredRegex:
        sent = re.sub(censored[0],censored[1],sent, flags=re.IGNORECASE) # what does r do?
    return sent

def compare(w1, w2):
    """compare pronouciation, rank how close they are"""
    w1 = cleanUp(w1)
    w2 = cleanUp(w2)
    w1_phones = phones(w1)
    w2_phones = phones(w2)
    sim_pts = 0

    top_score = 0
    for pronounce1 in w1_phones: # Loop through all pronounciations of word 1
        for pronounce2 in w2_phones: # Loop through all pronounciations of word 2 b/c  of tomato tomato
            if len(pronounce1) > len(pronounce2):
                for i in range(len(pronounce2))[::-1]: # goes from end of shortest word indexes
                    if pronounce2[i] == pronounce1[i]: # Checking if phonemes is same at index
                        sim_pts += 1
                        if pronounce2[-1].isdigit(): # IF digit means stress, meaning higher points because the same phonemes is stressed.
                            sim_pts += 1
            else:
                for i in range(len(pronounce1))[::-1]:
                    if pronounce2[i] == pronounce1[i]:
                        sim_pts += 1
                        if pronounce2[-1].isdigit():
                            sim_pts += 1
            if sim_pts > top_score:
                top_score = sim_pts
            sim_pts = 0
    return top_score
def phones(w):
    """find all the ways the word is said"""
    phone_dic = nltk.corpus.cmudict.dict()
    if w not in phone_dic:
        return ['']
    return phone_dic[w]

def cleanUp(word):
    """Removes end sentence punctuation"""
    letters = "?,.!"
    for letter in letters:
        word = word.replace(letter, " ")
    return word.strip().lower()