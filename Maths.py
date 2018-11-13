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

# https://leetcode.com/problems/ugly-number-ii/description/
## method 1 :
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 1
        num1 = num
        output = []
        i = 0
        if n == 1:
            return 1
        else:
            while len(output) <= n:
                while num % 2 == 0:
                    num = num / 2
                while num % 3 == 0:
                    num = num / 3
                while num % 5 == 0:
                    num = num / 5
                i += 1
                if num == 1 or num == 3 or num == 5:
                    output.append(i)
                num1 += 1
                num = num1
            return output[n-1]
## method 2:
class Solution:
    # dynamic programming
    def nthUglyNumber(self, n):
        ugly = [0] * n
        nxt = ugly[0] = 1
        i2 = i3 = i5 = 0
        nxt2, nxt3, nxt5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
        for i in range(1, n):
            nxt = min(nxt2, nxt3, nxt5)
            ugly[i] = nxt
            if nxt == nxt2:
                i2 += 1
                nxt2 = ugly[i2]*2
            if nxt == nxt3:
                i3 += 1
                nxt3 = ugly[i3]*3
            if nxt == nxt5:
                i5 += 1
                nxt5 = ugly[i5]*5
