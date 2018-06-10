from recommender import *

matrix = numpy.loadtxt(open("../data/utility_matrix.csv", "rb"), delimiter=",").astype('float')
nMatrix = normalise(matrix)

combinations = list(itertools.combinations(range(0,len(matrix)), 2))

jaccardDict,cosDict,pearsonDict = [{}] * 3


for combination in combinations:
    jaccardDict.update({combination : (
        jaccard(matrix[combination[0]],matrix[combination[1]]),jaccard(nMatrix[combination[0]],nMatrix[combination[1]])
    )})
    cosDict.update({combination : (
        cos(matrix[combination[0]],matrix[combination[1]]),cos(nMatrix[combination[0]],nMatrix[combination[1]])
    )})
    pearsonDict.update({combination : (
        pearson(matrix[combination[0]],matrix[combination[1]]),pearson(nMatrix[combination[0]],nMatrix[combination[1]])
    )})

## ("(UserID,UserID) : (matrix,normalisedMatrix)")
print("-------------------------------------------------------------------------------")
print("-------------------------- Jaccard Distance -----------------------------------")
print("-------------------------------------------------------------------------------")
print(jaccardDict)
print("-------------------------------------------------------------------------------")
print("-------------------------- Cosine Similarity ----------------------------------")
print("-------------------------------------------------------------------------------")
print(cosDict)
print("-------------------------------------------------------------------------------")
print("-------------------------- Pearson Similarity ---------------------------------")
print("-------------------------------------------------------------------------------")
print(pearsonDict)