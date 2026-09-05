import torch
import numpy as np


data = np.array(([2,3], [1, 0]))
#print(data)
x = torch.from_numpy(data)
x_ones = torch.ones_like(x)
y = torch.rand((2,2))

agg = y.sum()
#print(agg)
#print(agg.item(), type(agg.item()))

print(y)
print(y.numpy())

y.add_(10)
print(y, y.numpy())


#print(y)
y.add_(2)
#print(y)




#print(y.matmul(y.T))
#print(torch.cat([y, x], 1))
#if torch.accelerator.is_available():
#   r = y.to(torch.accelerator.current_accelerator()) 
