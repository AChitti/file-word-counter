def countWords():
    fileName=input("What file's words should be counted?")
    numOfWords=0
    file=open(fileName,'r')
    for line in file:
        words=line.split( )
        numOfWords=numOfWords+len(words)
    print("Number of words: ")
    print(numOfWords)
countWords()