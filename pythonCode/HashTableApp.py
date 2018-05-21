# Hash Table application, Avoid repetition
voter = {}   # Creat a hash table
def votedPerson(name):
    if voter.get(name):
        print "Kick out!"
    else:
        voter[name] = True
        print "Welcome "+name+" Vote!"

votedPerson("Mike")
votedPerson("Bright")
votedPerson("Bright")
votedPerson("Jimmy")
votedPerson("Mike")