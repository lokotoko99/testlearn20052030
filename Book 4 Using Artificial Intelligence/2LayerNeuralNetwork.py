# 2 Layer Neural Network in NumPy
import numpy as np

# X = input of our 3 input XOR gate
# set up the inputs of the neural network (right from the table)
X = np.array(([0,0,0],
              [0,0,1],
              [0,1,0], \
              [0,1,1],
              [1,0,0],
              [1,0,1],
              [1,1,0],
              [1,1,1]), dtype=float)
# y = our output of our neural network
y = np.array(([1],
              [0],
              [0],
              [0],
              [0],
              [0],
              [0],
              [1]), dtype=float)

# what value we want to predict
xPredicted = np.array(([0,0,1]), dtype=float)

X = X/np.amax(X, axis=0) # maximum of X input array
# maximum of xPredicted (our input data for the prediction)
xPredicted = xPredicted/np.amax(xPredicted, axis=0) 

# set up our Loss file for graphing

lossFile = open("SumSquaredLossList.csv", "w")

class Neural_Network (object):
  def __init__(self):
    #parameters
    self.inputLayerSize = 3  # X1,X2,X3 
    self.outputLayerSize = 1 # Y1
    self.hiddenLayerSize = 4 # Size of the hidden layer

    # build weights of each layer
    # set to random values
    # look at the interconnection diagram to make sense of this
    # 3x4 matrix for input to hidden
    self.W1 = \
            np.random.randn(self.inputLayerSize, self.hiddenLayerSize)  
    
    """W1 = np.array([
      [0.1, 0.2, 0.3, 0.4],  # weights from X1 to H1-H4
      [0.5, 0.6, 0.7, 0.8],  # weights from X2 to H1-H4
      [0.9, 1.0, 1.1, 1.2]   # weights from X3 to H1-H4
      ])"""
    # 4x1 matrix for hidden layer to output
    self.W2 = \
            np.random.randn(self.hiddenLayerSize, self.outputLayerSize) 

  def feedForward(self, X):
    # feedForward propagation through our network
    # dot product of X (input) and first set of 3x4  weights
    self.z = np.dot(X, self.W1) 

    """ First matrix shape: (8 rows, 3 columns)  > 8 x 3
        Second matrix shape: (3 rows, 4 columns) > 3 x 4
        Rule: Number of columns in first matrix (3) = Number of rows in second matrix(3) > multiplication valid.
        Result: Shape = (number of rows in first matrix, number of columns in second matrix) = (8,4)
        So, multiplying (8x3) x (3x4) = (8x4)"""

    # the activationSigmoid activation function - neural magic
    self.z2 = self.activationSigmoid(self.z) 
    """ the 8x4 matrices remains but now transformed by the activation sigmoid"""

    # dot product of hidden layer (z2) and second set of 4x1 weights
    self.z3 = np.dot(self.z2, self.W2) 
    """ 8x4 x 4x1 = 8x1 matrix"""

    # final activation function - more neural magic
    o = self.activationSigmoid(self.z3) 
    return o
    """ is a 8 x 1 matrix"""

  def backwardPropagate(self, X, y, o):
    # backward propagate through the network
    # calculate the error in output
    self.o_error = y - o 
    """ in order to subtract matrix have to have the same row and columns"""

    # apply derivative of activationSigmoid (which is basically the slope)  to error 
    self.o_delta = self.o_error*self.activationSigmoidPrime(o) 
    """ Still a 8x1 """

    # z2 error: how much our hidden layer weights contributed to output error
    self.z2_error = self.o_delta.dot(self.W2.T)  

    """ calling .dot on the matrix directly so its  a 8x1  x 1x4(transposed) becomes a 8x4  """
    

    # applying derivative of activationSigmoid to z2 error
    self.z2_delta = self.z2_error*self.activationSigmoidPrime(self.z2) 

    """Becomes a 8x4 matrix"""

    # adjusting first set (inputLayer --> hiddenLayer) weights
    self.W1 += X.T.dot(self.z2_delta) 
    # adjusting second set (hiddenLayer --> outputLayer) weights 
    self.W2 += self.z2.T.dot(self.o_delta) 

  def trainNetwork(self, X, y):
    # feed forward the loop
    o = self.feedForward(X)
    # and then back propagate the values (feedback)
    self.backwardPropagate(X, y, o)


  def activationSigmoid(self, s):
    # activation function
    # simple activationSigmoid curve as in the book
    return 1/(1+np.exp(-s))

  def activationSigmoidPrime(self, s):
    # First derivative of activationSigmoid
    # calculus time!
    return s * (1 - s)


  def saveSumSquaredLossList(self,i,error):
    lossFile.write(str(i)+","+str(error.tolist())+'\n')
    
  def saveWeights(self):
    # save this in order to reproduce our cool network
    np.savetxt("weightsLayer1.txt", self.W1, fmt="%s")
    np.savetxt("weightsLayer2.txt", self.W2, fmt="%s")

  def predictOutput(self):
    print ("Predicted XOR output data based on trained weights: ")
    print ("Expected (X1-X3): \n" + str(xPredicted))
    print ("Output (Y1): \n" + str(self.feedForward(xPredicted)))

myNeuralNetwork = Neural_Network()
trainingEpochs = 1000
#trainingEpochs = 100000

for i in range(trainingEpochs): # train myNeuralNetwork 1,000 times
  print ("Epoch # " + str(i) + "\n")
  print ("Network Input : \n" + str(X))
  print ("Expected Output of XOR Gate Neural Network: \n" + str(y))
  print ("Actual  Output from XOR Gate Neural Network: \n" + \
          str(myNeuralNetwork.feedForward(X)))
  # mean sum squared loss
  Loss = np.mean(np.square(y - myNeuralNetwork.feedForward(X))) 
  myNeuralNetwork.saveSumSquaredLossList(i,Loss)
  print ("Sum Squared Loss: \n" + str(Loss))
  print ("\n")
  myNeuralNetwork.trainNetwork(X, y)

myNeuralNetwork.saveWeights()
myNeuralNetwork.predictOutput()
