import numpy
import itertools

# Calculates the jaccard similarity between two given vectors 
def jaccard(A,B):
    dividend, divisor = [0] * 2
    
    for iteration in range(0,len(A)):
        if A[iteration] != 0 and B[iteration] != 0:
            divisor += 1
            if A[iteration] == B[iteration]:
                dividend += 1
    
    if divisor == 0:
        return 0
    return dividend / divisor

# Calculates the cos similarity between two given vectors 
def cos(A,B):
    dividend, divisorA, divisorB = [0] * 3
    
    for iteration in range(0,len(A)):
        dividend += A[iteration] * B[iteration]
        divisorA += A[iteration] ** 2
        divisorB += B[iteration] ** 2
        
    if divisorA * divisorB == 0:
        return 0
    return dividend / (divisorA * divisorB)

# Calculates the pearson similarity between two given vectors
def pearson(A,B):
    dividend, divisorA, divisorB = [0] * 3
    meanOfA = sum(A)/len(A)
    meanOfB = sum(B)/len(B)
    
    for iteration in range(0,len(A)):
        if(A[iteration] != 0 and B[iteration] != 0):
            dividend+= (A[iteration] - meanOfA) * (B[iteration] - meanOfB)
            divisorA+= (A[iteration] - meanOfA)**2
            divisorB+= (B[iteration] - meanOfB)**2
            
    if divisorA * divisorB == 0:
        return 0
    return dividend / (divisorA**(0.5) * divisorB)

# Normalises a matrix of ratings by substracting the average
def normalise(M):
    N = M.copy()
    for entry in N:
        average = sum(entry) / len([e for e in entry if e != 0])
        for iteration in range(0,len(entry)):
            if entry[iteration] != 0:
                entry[iteration] -= average
    return N

# Calculates the mean average deviation between two vectors
def meanAverageDeviation(predictions,ratings):
    sum = 0
    if(len(predictions) == len(ratings)):
        for iteration in range(0,len(predictions)):
            sum += predictions[iteration] - ratings[iteration] 
    return sum/len(predictions)

def predict(R,P,Q):
    Q = Q.transpose()
    for i in range(0,len(R)):
        for x in range(0,len(R[i])):
            if R[i][x] == 0:
                R[i][x] = sum(P[i]) * sum(Q[x])
    return R

def factorization(R,learningRate,numberOfLatentFeatures):

    numberOfUsers = len(R)
    numberOfItems = len(R[0])

    P = numpy.ones((numberOfUsers,numberOfLatentFeatures))
    Q = numpy.ones((numberOfLatentFeatures,numberOfItems))

    for i in range(0,numberOfUsers):
        for k in range(0,numberOfLatentFeatures):
            for j in range(0,numberOfItems):
                P[i][k] += learningRate * dLdP(R,P,Q,i,k,j)
                Q[k][j] += learningRate * dLdQ(R,P,Q,i,k,j)

    return (P,Q)


def dLdP(R,P,Q,i,k,j):
    return  -2 * (R[i][j] - sumPQ(P,Q,i,j,k)) * Q[k][j]


def dLdQ(R,P,Q,i,k,j):
    return -2 * (R[i][j] - sumPQ(P,Q,i,j,k)) * P[i][k]

def sumPQ(P,Q,i,j,k):
    sum = 0
    for k2 in range(0,k):
        sum += P[i][k2] * Q[k2][j]
    return sum    

    



# Calculates the root mean square error between two vectors
# The difference between this and the meanAverageDeviation is that
# wrong predictions with huge error are penatilised
def rootMeanSquareError(predictions,ratings):
    sum = 0
    if(len(predictions) == len(ratings)):
        for iteration in range(0,len(predictions)):
            sum += (predictions[iteration] - ratings[iteration])**2
    return sum**(0.5)/len(predictions)