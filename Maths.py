# Linear regression parameters
# theta = (X^T X)^-1 X y
# Modules
import numpy as np

# Loading data set
# X, y = np.loadtxt('ex1data3.txt', delimiter=',', unpack=True)
#
# data = np.genfromtxt('ex1data3.txt', delimiter=',')

X = np.random.rand(100 ,2)
y = np.random.rand(100, 1)
X_transpose = np.transpose(X)

theta = np.linalg.inv(X_transpose.dot(X))
theta = theta.dot(X_transpose)
theta = theta.dot(y)

print(theta)

def normalEquation(X, y):
    m = int(np.size(data[:, 1]))

    # This is the feature / parameter (2x2) vector that will
    # contain my minimized values
    theta = []

    # I create a bias_vector to add to my newly created X vector
    bias_vector = np.ones((m, 1))

    # I need to reshape my original X(m,) vector so that I can
    # manipulate it with my bias_vector; they need to share the same
    # dimensions.
    X = np.reshape(X, (m, 1))

    # I combine these two vectors together to get a (m, 2) matrix
    X = np.append(bias_vector, X, axis=1)

    # Normal Equation:
    # theta = inv(X^T * X) * X^T * y

    # For convenience I create a new, tranposed X matrix
    X_transpose = np.transpose(X)

    # Calculating theta
    theta = np.linalg.inv(X_transpose.dot(X))
    theta = theta.dot(X_transpose)
    theta = theta.dot(y)

    return theta

# p = normalEquation(y, X)
# print(p)




# https://leetcode.com/problems/rectangle-area/description/
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):

        leftBottomX = max(A, E)
        leftBottomY = max(B, F)

        rightTopX = min(C, G)
        rightTopY = min(D, H)

        overlap = max(rightTopX - leftBottomX, 0) * max(rightTopY - leftBottomY, 0)

        return abs(C - A) * abs(D - B) + abs(G - E) * abs(H - F) - overlap