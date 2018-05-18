import apriori as ap
import pprint      
import os


def loadData(fileName):
    with open(os.path.abspath('..') + '/data/' + fileName) as file:
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
    # Prepare data from data/weblog.csv    
    transactions = []    
    for (id,transaction) in dict.items():
        transactions.append(transaction)
    return list(transactions)



## Example of usage
# Data file syntax: userID, websiteName

# you may also want to remove whitespace characters like `\n` at the end of each line
items = []
items.append('Knowledge Base')
transactions = loadData('weblog.csv')


print("Support for Knowledge Base")
print(ap.support(items,transactions))

items.append('Support Desktop')

print("Support for Knowledge Base and Support Desktop")
print(ap.support(items,transactions))

items.append('MS Office')

print("Support for Knowledge Base,Support Desktop and MS Office")
print(ap.support(items,transactions))


print("Confidence For Knowledge Base => Support Desktop")
print(ap.confidence('Knowledge Base','Support Desktop',transactions))

print("Frequent Items sets")
pprint.pprint(ap.find_frequent_itemsets(transactions,min_frequency = 1000))