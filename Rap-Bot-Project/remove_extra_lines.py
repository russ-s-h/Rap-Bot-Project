# used to fix some text files if there is extra spaces
def fixFile(original,newfile):
    """Removes extra spaces, and other error in the downloaded raps."""
    fi2 = open(newfile,"w")
    with open(original,'r') as fi:
        for line in fi:
            if not line.isspace() and not line == "" and not "x2" in line.lower() and not "verse" in line.lower():
                li = line.replace("\r","").replace("\n","").replace("&quot;","")
                fi2.write(li+"\n")
    fi2.close()

