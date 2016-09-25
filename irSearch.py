x = [13, 5, 6, 2, 5]
y = [5, 2, 5, 13]

#iterative search algorithm, loop through x match with recursive search algorithm
def answer(x, y):

#split by positive and negative, 0 as boundry

    x = sorted(x)
    y = sorted(y)
    
    uniqueX = []
    [uniqueX.append(element) for element in x if element not in uniqueX]
    
    x = uniqueX
    
    uniqueY = []
    [uniqueY.append(element) for element in y if element not in uniqueY]   
    
    y = uniqueY

#get larger array list for comparitive purpose

    if len(x) < len(y):
        x,y = y,x
        
    negX = [i for i in x if i <= 0 and i >= x[0]]
    negY = [i for i in y if i <= 0 and i >= y[0]]
    
    posX = [j for j in x if j >= 0 and i <= x[len(x)-1]]
    posY = [j for j in y if j >= 0 and i <= y[len(y)-1]]

#recursive search algorithm
    def twoBrothers(key, doors):
#initial wrapper conditions
        left = 0
        right = len(doors)-1
        found = False
        while left <= right and found == False:
            midpoint = (left + right) // 2
#terminal state
            if doors[midpoint] == key:
                found = True;
#recursive state
#if value less than
            else:
                if key < doors[midpoint]:
                    right = midpoint - 1
#if value greater than
                else:
                    left = midpoint + 1
#return value
        return found

    
    for i in negX:
        negEval = twoBrothers(i, negY)

        if (negEval is False):
            print i
    
    for i in posX:
        posEval = twoBrothers(i, posY)

        if (posEval is False):
            print i    

answer(x, y)