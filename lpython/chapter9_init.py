# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:45:02 2019

@author: manoj
"""

import tensorflow as tf

def global_variables_initializer(): 
	x  = tf.Variable(3,name='f')
	y  = tf.Variable(4,name='f')
	f = x*x*y + y + 2

#sess = tf.Session()
init = tf.global_variables_initializer() 
with tf.Session() as sess:
	init.run()
	x.initializer.run()
	y.initializer.run()
	result = f.eval()
	print(result)

