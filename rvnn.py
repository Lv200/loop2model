# -*- coding: utf-8 -*-

import tensorflow as tf
from pandas import DataFrame, Series
import numpy as np
import pandas as pd
from util import *

class Config(object):
	lr = 0.01


class RvNN_Model():

	def __init__(self, config):
		self.config = config
		self.load_data()

	def load_data(self):
		"""load train/test dataset"""
		loops = pd.read_csv('./dataset/train_loop.csv', header = 0, low_memory = False)
		loops.columns = ['loop_infos', 'sym_shapes', 'tree_kids', 'sym_params']		
		loop_infos = dtypeTransform(loops['loop_infos'], float)
		sym_shapes = dtypeTransform(loops['sym_shapes'], float)
		tree_kids = dtypeTransform(loops['tree_kids'], int)
		sym_params = dtypeTransform(loops['sym_params'], float)
		#print sym_params

	def inference(self, tree):
		"""For a given tree build the RvNN models computation graph up to where it may be used for inference"""
		pass


	def add_model_vars(self):
		pass


	def add_model(self):
		pass


	def loss(self, logits, labels):
		pass


	def training(self, loss):
		train_op = None
		optimizer = tf.train.GradientDesecentOptimizer(self.config.lr)
		train_op = optimizer.minimize(loss)
		return train_op


	def predictions(self, y):
		preditions = None

		return predictions

	def predict(self):
		pass

	
	def run_epoch(self):
		step = 0

	
	def train(self):
		pass
		

def test_RvNN():
	config = Config()
	model = RvNN_Model(config)


if __name__ == "__main__":
	test_RvNN()
		
