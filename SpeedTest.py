import itertools
import operator
import pprint

# Calculates the support of an item in a list of transactions as described by Apriori
# @items: List of items as ["itemOne","itemTwo",...]
# @transactions: List of transaction. Each transaction is a list storing the name of the items as string [["itemOne","itemTwo",..],["itemThree","itemTwo",..],....]
def support(items,transactions):
    if isinstance(items, str):
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
    if counterLeft == 0:
        return 0
    else:
        return (counterRight / counterLeft)





# Finds all itemsets which have a support higher than minimum_support
# Return a dictionary with the set and support
## General Idea:
## 1. Create list of all elements present in the transactions
## 2. Filter all items from the list which have a lower support than the min_sup
## Set n to 2
## 3. Create a list of all possible combinations of size n of the remaining elements 
## 4. Filter all combinations which have a lower support than the min_sup
## 5. Create a list of all elements in the remaining combinations
## 6. If list is not empty Go to step 3
## 7. stop
def find_frequent_itemsets(transactions,min_support = 0,min_frequency = 0):
    print(min_frequency)
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
        filteredItemSets = []
        # Set containing all remaining elements
        itemsLeft = set()
        # Iterate over all remaining sets with size i
        # Calculate sup. 
        # If higher than min_sup add to filteredItemSets & add item to itemsLeft
        transactions_size = len(transactions)

        for itemSet in itemSets:
            sup = support(itemSet,transactions)
            if sup >= min_support and ((sup * transactions_size) >= min_frequency):
                print(itemSet)
                print(sup)
                print(sup*transactions_size)
                print("---------------")
                filteredItemSets.append(itemSet)
                dict.update({itemSet:sup*transactions_size})
                for item in itemSet:
                    itemsLeft.add(item)

        # Now you have a list of all remaning elements
        # And a list of all sets of size i which are permutations of the elements in the itemsLeft set
        # and have a higher support than min_sup

        if len(filteredItemSets) > 0:
            if iteration == 2:
                itemSets = list(itertools.combinations(list(filteredItemSets),iteration))
         
            if iteration >= 3:
                # Preparing a list for all possible permutations of the remaining items
                # When the score reaches 3: The permutation should be considered for the next iteration
                tupelScores = {}
                perms = itertools.permutations(list(itemsLeft),iteration)
                for perm in perms:
                    tupelScores.update({perm:0})
                # Initialising empty itemSets
                itemSets = []

                # We loop over the set with sets of size iteration -  1
                for itemSet in filteredItemSets:   
                    for item in itemsLeft:
                        if item not in itemSet:
                            itemSetPerms = itertools.permutations(list(itemsLeft),iteration)
                            for itemSetPerm in itemSetPerms:
                                tupelScores[itemSetPerm] += 1
                                if tupelScores[itemSetPerm] == iteration:
                                    itemSets.append(itemSetPerm)
                                    break


                if len(itemSet) == 0:
                    stop = True

        else:
            stop = True

        iteration += 1

    return sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

            

def loadData(fileName):
    with open('data/' + fileName) as file:
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
transactions = loadData('weblog.csv')

print("Frequent Items sets")
pprint.pprint(find_frequent_itemsets(transactions,min_frequency = 1000))


