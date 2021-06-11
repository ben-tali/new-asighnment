# key value pairs
#ben = {
   # "firstname": "Ben",
  #  "lastname": "Tali",
   # "Job Title": 'Engeneer'
#}
# define dicitionaries
#jobtitle = ben["Job Title"]
#print(jobtitle)
#jobtitle = ben.get("JobritritTitle", "Engeneer")
# get a value by key
#ben["Job Title"] = "Teacher"
#print(ben)
# supply a default

# write a program that converts numerical digits to words
#123 => ONE TWO THREE
def printwords(num):
    if num == '0':
        print("Zero ", end = " ")

    elif num == '1':
        print("One ", end = " ")

    elif num == '2':
        print("Two ", end=" ")

    elif num=='3':
        print("Three",end=" ")

    elif num == '4':
        print("Four ", end = " ")

    elif num == '5':
        print("Five ", end = " ")
        
    elif num == '6':
        print("Six ", end = " ")
 
    elif num == '7':
        print("Seven", end = " ")
 
    elif num == '8':
        print("Eight", end = " ")
 
    elif num == '9':
        print("Nine ", end = " ") 

def printWRD(X):
    y = 0
    length = len(X)
    while y < length:
        printwords(X[y])
        y += 1
X = ("0", "2", "6",)
printWRD(X)




