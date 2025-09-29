

"""# Understanding Neural Networks;;"""0

"""
»» An input layer of neurons connecting from the world
»» Some number of hidden layers of neurons
»» An output layer of neurons connecting to the world
»» A set of weights and biases between each neuron level
»» A choice of activation function for each hidden layer of neurons
»» A choice of loss function to reduce overtraining the network


Layers of Neurons

-input layer
-hidden layer
-output layer

Deep Learning gets its name from the fact that when you have multiple hidden layers, to increase depth of the neural network

Feed-Forward network: Movement information Left to Right is also known as  because data feeds in one direction.
Back Propagation: stimulates what people do when performing a task using an interative trial-and-error approach

Weights and biases

Weights : as how important each neuron is
Bias :As what the neuron uses to modify the activation of the output of the neuron(adjusting the neuron threshold up or down)

Weights affect the steepness of the activation function curve, the bias shifts the entire curve to the right or left.

The activation function: Is the mathematical function that determines whether information passses through(thus activating the neuron)
                         or is stopped by the individual neuron (thus deactivating the neuron)
                         Howver, you use the function not only as gate (open or shut)
                         But also to transform the input signal to the neuron in some useful way.

--Sigmoid function is a S.


Loss function: Compares the result of our neural network to the desired results.

Good way to avoid overtraining the network, also transmit the result of the loss function to our backpropagation channel.

333333333333333333333333333333


"""