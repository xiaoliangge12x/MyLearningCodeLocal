states_needed = set(["A","B","C","D","E","F","G","H","I","J","K"])
broadCasts = {}
broadCasts["Nantong"]=set(["A","G","K"])
broadCasts["Beijing"]=set(["B","C","E","G","I"])
broadCasts["Suzhou"]=set(["D","H"])
broadCasts["ShangHai"]=set(["A","E","F","I","J"])
broadCasts["ChangZhou"]=set(["C","D","K"])

chosenCasts = []
while states_needed:
    bestCast = None
    statesForBestCast = set()
    for Cast, statesForCast in broadCasts.items():
        currentStates = states_needed & statesForCast
        if len(currentStates) > len(statesForBestCast):
            bestCast = Cast
            statesForBestCast = currentStates
    chosenCasts.append(bestCast)
    states_needed -= statesForBestCast

print chosenCasts