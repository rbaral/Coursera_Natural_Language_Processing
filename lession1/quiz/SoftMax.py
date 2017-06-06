__author__ = 'rbaral'
import numpy as np

'''
this script computes the softmax value
of a given numpy array. It returns an array
of size same as the input array. The definition
of softmax for an array y is used as:
Softmax(y_i) = (e^y_i)/sum_j(e^y_j)
'''
scores1 = np.array([1.0, 2.0 , 3.0])

scores = np.array([[1, 2, 3, 6],
                   [2, 4, 5, 6],
                   [3, 8, 7, 6]])

def softmax(x):
    #x = x*10 # if we multiply the elements by 10, the prob. gets closer to 0 or 1
    #x = x/10 # if we divide the elements by 10, the prob. gets uniformly distributed
    return np.exp(x)/sum(np.exp(x))


soft1 = softmax(scores*10)
#multiply by 10 either makes the probability near to 1 or near to 0
print soft1

#divide by 10 will make the probability nearly uniformly distributed
print softmax(scores/10)

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()

