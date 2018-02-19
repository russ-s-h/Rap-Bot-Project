# text processing from websites
import urllib2
import time
class Song():
    def __init__(self):
        self.lyrics = []
    def addLine(self,line):
        """Add line to song"""
        self.lyrics.append(line)
    def readLines(self):
        """Get lines from song object"""
        return self.lyrics
class Artist():
    def __init__(self,artist):
        self.songs = []
        self.artist = artist
        self.output = open("rap.txt","w")
    def loadLinksFromArtistPage(self):
        """Loads data from azlyrics page of artist, and identifies then downloads all songs done by artist. Outputs to file."""
        # Opens a web page of songs list.
        website = urllib2.urlopen("http://www.azlyrics.com/" + self.artist[0] + "/" + self.artist + ".html")
        links = []
        current = website.readline()
        found = False
        # find song link list in the website
        while current != '' and not found:
            if "var songlist = [" in current:
                # we hit the song link list
                found = True
            current = website.readline()
        # hit the song link list (javascript variable list)
        finish = False
        while current != '' and not finish:
            if "]" in current:
                # end of the variable list
                finish = True
            i = current.index('h:') # first index of the url
            while True:
                if current[i:i+2] == "..":
                    i += 2
                    break
                elif current[i:i+3] == "com":
                    i += 3
                    break
                i += 1
            n = i
            while current[n] != '"':
                n += 1
            links.append(current[i:n])

            current = website.readline()
        # loop through song link list and download each song
        for n, link in enumerate(links):
            if self.loadSongLyrics(link) == None:
                break
            print n+1, "links done out of", len(links)
        self.output.close()
        return True
    def loadSongLyrics(self,address):
        """Loads specific song lyrics and saves to file."""
        time.sleep(55)
        # error catching to incase website does not respond
        try:
            website = urllib2.urlopen("http://www.azlyrics.com" + address)
        except:
            return None
        current = website.readline()
        found = False
        # look for position on website that is the beginning of song
        while current != "" and not found:
            if "<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->" in current:
                # FOUND THE SONG
                found = True
            current = website.readline()
        end = False
        lyrics = Song()
        # extract HTML formating and write to file
        while current != "" and not end:
            if "</div>" in current:
                end = True
            else:
                remove = ["\n","<br>","<i>","</i>","[","]"]
                for item in remove:
                    current = current.replace(item,"")
                if current != "":
                    self.output.write(current+"\n")
                    lyrics.addLine(current)
            current = website.readline()
            # strip off stuff
        # flush file to make sure all gets written incase of program crashing
        self.output.flush()
        self.songs.append(lyrics)
        return True

# Example download
artist = Artist("eminem")
artist.loadLinksFromArtistPage()

