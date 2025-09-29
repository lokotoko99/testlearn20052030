""" Keras is an open-source neural-network library that enables fast experimentation
with neural networks, deep learning, and machine learning. Keras is an indispensable
part of TensorFlow. In 2017, Google decided to natively support Keras
as the preferred interface for TensorFlow. Keras provides the excellent and intuitive
set of abstractions and functions, whereas TensorFlow provides the efficient
underlying implementation. NumPy implements the necessary matrix math in the
TensorFlow modules."""

"""The five steps to implement a neural network in KEras with TensorFlow follow:

1. Load and format your date.

    The first step, loading your data, is trivial in our model but is often the most complex
    and difficult part of building an entire program. You have to examine your
    data (for example, an XOR gate or a database of factors affecting diabetic heart
    patients) and figure out how to map the data and the results to get to the information
    and predictions you want.


2. Define your neural network model and layers.

    In the second step, defining your network, you can see one of the primary advantages
    of Keras over other frameworks. You basically just construct a stack of the
    neural layers you want your data to flow through. Remember that TensorFlow is
    just matrices of data flowing through a neural network stack. In this step, you
    chose the configuration of your neural layer and activation functions.    


3. Compile the model.

    In the third step, you compile your model, which hooks up your Keras layer model
    with the underlying machine-specific software (the back-end) to run on your
    hardware. You also choose what you want to use for a loss function.


4. Fit and train your model.

    The real work of training your network takes place in the fourth step. You determine
    how many epochs you want the program go through. You also accumulate
    the history of what is happening through all the epochs, and use this information
    to create your graphs.

5. Evaluate the model.

    After training your model, you have to evaluate it. Evaluation refers to running
    your trained machine-learning model on other data to see how well the model
    does on data that was not included in your training set. Because we have all the
    possible values (combinations of 3 bits) as part of the training set, we aren’t doing
    that here.

"""

