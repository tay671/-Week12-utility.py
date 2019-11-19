#   METHOD USED
#   Tayler Jone
#  ​ CSCI 102 – Section A
#   Week 12 - Part A

def PrintOutput(a):
    print('OUTPUT', a)

def LoadFile(filename):
    List = []
    List.append(filename.readline())
    PrintOutput(List)

def UpdateString(string,replace,location):
    strlist = list(string)
    strlist[location] = replace
    combined = ""join.strlist
    PrintOutput(combined)

def FindWordCount(filename,word):
    count=0
    f=open(filename,'r')
    read=f.readlines()
    for line in read:
        if word in line:
            count=count+1
    PrintOutput(count)

def ScoreFinder():

def Union(list1,list2):
    finallist = list1 + list2
    
def Intersection():

def NotIn():
    
