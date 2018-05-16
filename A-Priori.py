import itertools
# Calculates the support of an item in a list of transactions as described by Apriori
# @items: List of items as ["itemOne","itemTwo",...]
# @transactions: List of transaction. Each transaction is a list storing the name of the items as string [["itemOne","itemTwo",..],["itemThree","itemTwo",..],....]
def support(items,transactions):
    if not isinstance(items,(list,)):
        items = [items]
    counter = 0
    present = False
    for transaction in transactions:
        present = True
        for item in items:
            if item not in transaction:
                present = False
        if present:
            counter += 1
    return (counter/len(transactions))

# Calculates the confidence of an item in a list of transactions as described by Apriori
# @itemLeft => @itemRight       
def confidence(itemLeft,itemRight,transactions):
    counterLeft = 0
    counterRight = 0
    for transaction in transactions:
        if itemLeft in transaction:
            counterLeft += 1
            if itemRight in transaction:
                counterRight += 1
    return (counterRight / counterLeft)


# Finds all itemsets which have a support higher than minimum_support
# Return a dictionary with the set and support
def find_frequent_itemsets(transactions,minimum_support):
    # find all items 
    items = set()
    for transaction in transactions:
        for item in transaction:
            items.add(item)     
    # Remove all items which don't meet the min sup
    dict = {}
    itemSets = list(items)
    stop = False

    iteration = 2
    while(not stop):
        updatedItemSets = []
        for itemSet in itemSets:
            sup = support(itemSet,transactions)
            print(sup)
            if sup >= minimum_support:
                updatedItemSets.append(itemSet)
                dict.update({itemSet:sup})

        print(updatedItemSets)

        if len(updatedItemSets) > 0:
            itemSets = list(itertools.combinations(list(updatedItemSets),iteration))
            print(itemSets)
        else:
            stop = True

        iteration += 1

    return dict
            

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
transactions = loadData()


print("Support for Knowledge Base")
print(support(items,transactions))

items.append('Support Desktop')

print("Support for Knowledge Base and Support Desktop")
print(support(items,transactions))

items.append('MS Office')

print("Support for Knowledge Base,Support Desktop and MS Office")
print(support(items,transactions))


print("Confidence For Knowledge Base => Support Desktop")
print(confidence('Knowledge Base','Support Desktop',transactions))

print("Frequent Items sets")
print(find_frequent_itemsets(transactions,0.1))