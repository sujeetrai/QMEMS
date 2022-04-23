def division():
    try:
        5/0
    except:
        print(" this is division function")
        division()
        this is division function

        Subjects=["American","Indian"]
Verbs=["Play","Watch"]
Objects=["baseball","cricket"]
Subjects
['American', 'Indian']
Verbs
['Play', 'Watch']
Objects
['baseball', 'cricket']
for i in Subjects:
    for j in Verbs:
        for k in Objects:
            print(i,j,k, " ")
            American Play baseball  
American Play cricket  
American Watch baseball  
American Watch cricket  
Indian Play baseball  
Indian Play cricket  
Indian Watch baseball  
Indian Watch cricket  