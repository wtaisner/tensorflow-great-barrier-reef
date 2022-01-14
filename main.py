import numpy as np

# see if venv is correctly installed
import torch
x = torch.rand(5, 3)
print(x)
print(torch.cuda.is_available())

file = np.load('data/example_test.npy')
print(file.shape, type(file))
