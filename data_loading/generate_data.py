import numpy as np
import matplotlib.pyplot as plt
import os


def generate_y_data(coeff, x, error):
    return coeff[0] + np.sum(coeff[1:].reshape((1,-1)) * x, axis=1).reshape((-1,1)) + error


def generate_data(n_train=100, n_test=100, feature_dim=1, coeff=None, seed=0, error_std=0.1):
    
    np.random.seed(seed)
    
    if coeff == None:
        coeff = np.random.normal(0., 1., (feature_dim+1, 1)) 
    
    x_train = np.random.normal(0., 1., (n_train, feature_dim))
    x_test = np.random.normal(0., 1., (n_test, feature_dim))
    
    error_train = error_std * np.random.normal(0., 1., (n_train, 1))
    error_test = error_std * np.random.normal(0., 1., (n_test, 1))
    
    y_train = generate_y_data(coeff, x_train, error_train)   
    y_test = generate_y_data(coeff, x_test, error_test)
        
    return x_train, y_train, x_test, y_test, coeff