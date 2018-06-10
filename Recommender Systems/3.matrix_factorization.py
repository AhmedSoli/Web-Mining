from recommender import *
import pprint

matrix = numpy.loadtxt(open("../data/utility_matrix.csv", "rb"), delimiter=",").astype('float')
nMatrix = normalise(matrix)

(P,Q) = factorization(matrix,0.0002,5)
(NP,NQ) = factorization(nMatrix,0.0002,5)

matrix = predict(matrix,P,Q)
print(matrix)