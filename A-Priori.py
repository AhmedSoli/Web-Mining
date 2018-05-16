# Calculates the support of an item in a list of transactions as described by Apriori
def support(items,transactions):
    counter = 0
    present = False
    for (ID,transaction) in transactions:
        present = True
        for item in items:
            if item not in transaction:
                present = False
        if present:
            counter += 1
            
    return (counter/len(transactions))

# Calculates the confidence of an item in a list of transactions as described by Apriori
def confidence(itemLeft,itemRight,transactions):
    counterLeft = 0
    counterRight = 0
    for (ID,transaction) in transactions:
        if itemLeft in transaction:
            counterLeft += 1
            if itemRight in transaction:
                counterRight += 1
    return (counterRight / counterLeft)

def loadData():
    with open('data/weblog.csv') as file:
        content = file.readlines()
        lines = [x.strip() for x in content]
    dict = {}
    for i in range(1,len(lines)):
        linesSplit = lines[i].split(',')
        userID = linesSplit[0]
        websiteName = linesSplit[1]
        if userID not in dict:
            dict.update({userID: []})
        dict[userID].append(websiteName)
    return dict





## Example of usage
# Data file syntax: userID, websiteName

# you may also want to remove whitespace characters like `\n` at the end of each line
items = []
items.append('Knowledge Base')
dict = loadData()


print("Support for Knowledge Base")
print(support(items,dict.items()))

items.append('Support Desktop')

print("Support for Knowledge Base and Support Desktop")
print(support(items,dict.items()))

items.append('MS Office')

print("Support for Knowledge Base,Support Desktop and MS Office")
print(support(items,dict.items()))


print("Confidence For Knowledge Base => Support Desktop")
print(confidence('Knowledge Base','Support Desktop',dict.items()))