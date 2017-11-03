import numpy as np
import tensorflow as tf


class Config(object):
	lr = 0.01


class RvNN_Model():

	def __init__(self, config):
		self.config = config
		self.load_data()

	def load_data(self):
		"""load train/test dataset"""


	def inference(self, tree):
		"""For a given tree build the RvNN models computation graph up to where it may be used for inference"""


	def add_model_vars(self):


	def add_model(self):


	def loss(self, logits, labels):


	def training(self, loss):
		train_op = None
		optimizer = tf.train.GradientDesecentOptimizer(self.config.lr)
		train_op = optimizer.minimize(loss)
		return train_op


	def predictions(self, y):
		preditions = None

		return predictions

	def predict(self):

	
	def run_epoch(self):
		step = 0

	
	def train(self):
		

def test_RvNN():
	config = Config()
	model = RvNN_Model(config)


if __name__ == "__main__"
	test_RvNN()
		
