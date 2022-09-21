import tensorflow as tf
import tensorflow_addons as tfa

class Encoder(tf.keras.layers.Layer):
    def __init__(self):

        super().__init__()
        # Add initialization code here, including the layers that will be used in call(). e.g.,
        # layer1 = tf.keras.layers.BuiltInLayer(...)
        # layer2 = MyCustomLayer(...)
        self.embedding = tf.keras.layers.Embedding()
        self.attention = tf.keras.layers.Attention(1000)
        self.maxOut = tfa.layers.Maxout(500)
        self.biRNN = tf.keras.layers.Bidirectional(tf.keras.layers.SimpleRNN(1000,
                                                                             kernel_initializer=tf.keras.initializers.RandomNormal(
                                                                                 mean=0.0,
                                                                                 stddev=0.001,
                                                                                 seed=None),
                                                                             bias_initializer='zeros'))
    def call(self,input):

        # Add the code for the model call here (process the input and return the output). e.g.,
        # x = layer1(input)
        # output = layer2(x)

        return output
class Decoder(tf.keras.layers.Layer):
    def __init__(self):
        super().__init__()
    def call(self, input):