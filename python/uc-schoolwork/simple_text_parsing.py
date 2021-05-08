# import html file and create list of lines
import urllib.request
url = "http://shakespeare.mit.edu/romeo_juliet/full.html -o rj.html"
fp = urllib.request.urlopen(url)
rjlines = fp.readlines()
# utf8 decode
for i in range(1,len(rjlines)):
    rjlines[i] = rjlines[i].decode("utf8")
    pass

# first tried python regex to get the name to use as key
# m = re.search('(?<=<A NAME=speech[0-9]+><b>)\w+', script[i])
# name = m.group(0) # needs fixed "width"
# made a function to extract name from a line
def get_names(line):
    start = line.index('<b>') + 3
    end = line.index('</b>')
    name = line[start:end]
    return(name.lower())

# main function to create dictionary of the speaker name
# and the number of lines for that speaker
def line_count(script):
    dic = {}
    for i in range(1,len(script)):
        # check if the line starts with the following pattern : "<A NAME=speech"
        # line with speaker name
        if script[i].startswith('<A NAME=speech'):

            # get name
            name = get_names(script[i])

            line_count = 0 # count number of line
            line_index = i+2 # count line number for the while loop below

            # while speaker "speaking"
            while (script[line_index].startswith('<A NAME=')):
                line_count = line_count + 1
                line_index = line_index + 1

            # adding to the dictionary
            # update existing key or add new key
            if name in dic.keys():
                dic[name] += line_count
            else:
                dic[name] = 1
    return(dic)

rjdic = line_count(rjlines)

print(max(rjdic, key=rjdic.get), max(rjdic.values()))
