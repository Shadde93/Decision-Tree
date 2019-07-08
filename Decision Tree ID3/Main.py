import monkdata as m
import dtree as d
import drawtree_qt5 as dt
import random

monk1=m.monk1
monk1test=m.monk1test
monk2=m.monk2
monk2test=m.monk2test
monk3=m.monk3
monk3test=m.monk3test

print("Entropy for monk1: " + str(d.entropy(monk1)))
print("Entropy for monk2: " + str(d.entropy(monk2)))
print("Entropy for monk3: " + str(d.entropy(monk3)))


#Entropy for monk1: 1.0
#Entropy for monk2: 0.957117428264771
#Entropy for monk3: 0.9998061328047111

monktraining=[monk1,monk2,monk3]
monktrainingstr=["monk1","monk2","monk3"]

i=0
while i<3:
    z=0
    while z < 6:
        print("The information gain for attribute " + str(z+1) + " in " + monktrainingstr[i] + " is" + str(d.averageGain(monktraining[i],m.attributes[z])))
        z+=1
    i+=1


#print(d.bestAttribute(monk1,[m.attributes[0],m.attributes[1],m.attributes[2],m.attributes[3],m.attributes[4],m.attributes[5]]))
#print(d.bestAttribute(monk2,[m.attributes[0],m.attributes[1],m.attributes[2],m.attributes[3],m.attributes[4],m.attributes[5]]))
#print(d.bestAttribute(monk3,[m.attributes[0],m.attributes[1],m.attributes[2],m.attributes[3],m.attributes[4],m.attributes[5]]))

#selectedmonk1=d.select(monk1,m.attributes[4],2)

print("Accuracy of monk1 tree on testdata: "+str(d.check(d.buildTree(monk1, m.attributes), monk1test)))
print("Accuracy of monk2 tree on testdata: "+str(d.check(d.buildTree(monk2, m.attributes), monk2test)))
print("Accuracy of monk3 tree on testdata: "+str(d.check(d.buildTree(monk3, m.attributes), monk3test)))
print("Accuracy of monk1 tree on trainingdata: "+str(d.check(d.buildTree(monk1, m.attributes), monk1)))
print("Accuracy of monk2 tree on trainingdata: "+str(d.check(d.buildTree(monk2, m.attributes), monk2)))
print("Accuracy of monk3 tree on trainingdata: "+str(d.check(d.buildTree(monk3, m.attributes), monk3)))

#dt.drawTree(d.buildTree(monk3, m.attributes))

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]
frac=0.3

def Prunetreefunction(tree,testdata):
    bestaccuracy=0
    bestprunetree=tree
    for elem in d.allPruned(tree):
        accuracy=d.check(elem,testdata)
        if accuracy>bestaccuracy:
            bestaccuracy=accuracy
            bestprunetree=elem
    #print(bestaccuracy)
    return bestprunetree

    #Prunetree=d.buildTree(trainingdata, m.attributes)

def Bestprunedtree(treetoprune,testdata,trainingdata):
    bestaccuracy = d.check(treetoprune,testdata)
    if d.check(treetoprune,testdata)<=d.check(Prunetreefunction(treetoprune,testdata),testdata):        
        #print(str(d.check(treetoprune,testdata)) + " vs " + str(d.check(Prunetreefunction(treetoprune,testdata),testdata)))
        Bestprunedtree(Prunetreefunction(treetoprune,testdata),testdata,trainingdata)
        bestaccuracy = d.check(Prunetreefunction(treetoprune,testdata),testdata)
    else:
        #print("Now it is final with " + str(bestaccuracy) )
        print(str(bestaccuracy))
        return treetoprune

#print("beginning" + str(d.check(d.buildTree(monk1train, m.attributes),monk1val)))
#Bestprunedtree(d.buildTree(monk1train, m.attributes),monk1val,monk1train)

ten=1
while ten<=10:
    ten+=1
    monk3train, monk3val = partition(m.monk3, frac)
    Bestprunedtree(d.buildTree(monk3train, m.attributes),monk3val,monk3train)


