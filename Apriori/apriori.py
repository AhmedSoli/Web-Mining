import itertools
import operator

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


# Calculates the confidence of the assosiation @itemsLeft => @itemsRight
# Relative to the transactions   
def confidence(itemsLeft,itemsRight,transactions):

    if isinstance(itemsLeft,str):
        itemsLeft = [itemsLeft]
    if isinstance(itemsRight,str):
        itemsRight = [itemsRight]  

    counterLeft = 0
    counterRight = 0

    for transaction in transactions:
        leftItemsPresent = True
        rightItemsPresent = True
        for itemLeft in itemsLeft:
            if itemLeft not in transaction:
                leftItemsPresent = False
                break
        if leftItemsPresent:
            counterLeft += 1
            for itemRight in itemsRight:
                if itemRight not in transaction:
                    rightItemsPresent = False
                    break
            if rightItemsPresent:
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
                print("---------------------")
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
                            itemSet = list(itemSet)
                            itemSet.append(item)
                            itemSetPerms = itertools.permutations(itemSet,iteration)
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