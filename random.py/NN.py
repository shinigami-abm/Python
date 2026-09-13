import torch as t 
import numpy as np
import cv2 as cv
import os
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

device = "cuda" if t.cuda.is_available() else "cpu"

class NN(t.nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = t.nn.Flatten()
        self.Linear_relu_stack = t.nn.Sequential(
                t.nn.Linear(28*28, 512),
                t.nn.ReLU(),
                t.nn.Linear(512,512),
                t.nn.ReLU(),
                t.nn.Linear(512, 10),
                )
    def forward(self, x):
        x = self.flatten(x)
        return self.Linear_relu_stack(x)

model = NN().to(device)
#print(model)

x = t.rand(1, 28, 28, device=device)
#print(x)
logits = model(x)
pred = t.nn.Softmax(dim=1)(logits)
y_pred= pred.argmax(1)
print(y_pred)
