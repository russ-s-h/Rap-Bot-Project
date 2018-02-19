import string
import markovify
import time
import text_manipulation
class Song():

    def __init__(self,title="Donkey Kong Raps",length=8):
        self.title = title
        self.length = length
        self.rhymeScheme = []
        self.generateModel()
        alpha = string.ascii_lowercase
        letter_ind = 0
        for i in range(self.length/2):
            self.rhymeScheme.append(alpha[letter_ind])
            self.rhymeScheme.append(alpha[letter_ind])
            letter_ind += 1
        self.generateSong()
    def outputSong(self):
        """Prints out the song as text"""
        for line in self.song:
            print line
    def getLyrics(self):
        """Returns lyrics of song as list of sentences"""
        return self.song
    def generateSong(self):
        """Generates song and saves to variable"""
        self.song = ["" for x in range(self.length)] # establish array of length song
        i = 0
        while i < self.length:
            # check if this line has already been completed and confirm not at last letter
            if self.song[i] == "" and (i != self.length-1):
                # current letter in rhyme scheme
                let = self.rhymeScheme[i]
                for x in range(i+1,self.length):
                    if self.rhymeScheme[x] == let:
                        # next occurence in rhyme scheme
                        next_occurence = x
                        break
                pair = self.generateRhymingPair()
                self.song[i] = pair[0]
                self.song[next_occurence] = pair[1]
            i += 1
        # check if last line of song was completed if not add line
        if self.song[-1] == "":
            self.song[-1] = self.generateLine()

        return True

    def generateRhymingPair(self, tries=10):
        """ generates a rhyming pair of sentences"""
        while True:
            sent1 = self.generateLine()

            for i in range(tries):
                sent2 = self.generateLine()
                if text_manipulation.compare(sent1.split()[-1],sent2.split()[-1]) > 1:
                    return (sent1,sent2)

    def generateModel(self):
        """Creates the model using markovify"""
        with open("rap.txt") as f:
            text = f.read()
        self.model =  markovify.Text(textmerge)

    def generateLine(self):
        """Generates sentence using markovify"""
        sent = self.model.make_sentence()
        while sent == None or len(sent) > 140:
            sent = self.model.make_sentence()
        return sent


# CODE TO GENERATE SONGS USING OBJECTS EXAMPLE
for i in range(1):
    t1 = time.time()
    song = Song()
    t2 = time.time()
    with open('song'+str(i)+".txt",'w') as fi:
        for lyric in song.getLyrics():
            # lyric = censor(lyric) USE TO CENSOR
            fi.write(lyric+"\n")
        fi.write("\nGenerated in " + str(t2-t1) + " seconds.")


