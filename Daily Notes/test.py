def translate(translation,msg):
    msglist=msg.split(' ')
    translist=[]
    for word in msglist:
        if  word in translation:
            translist.append(translation[word])
        else:
            translist.append(word)
    return ' '.join(translist)

if __name__ == "__main__":
    import doctest
    doctest.testmod()