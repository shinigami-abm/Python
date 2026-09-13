import torch as t
import numpy as np
import cv2 as cv
import os
import pandas as pd
from torch.utils.data import Dataset
from torch.utils.data import DataLoader


class imgDataset (Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self , idx):
        path = os.path.join(self.img_dir, self.labels.iloc[idx, 0]) 
        img = t.from_numpy(cv.resize(cv.cvtColor(cv.imread(path), cv.COLOR_BGR2GRAY), (224,224))).float() /255.0
        label = self.labels.iloc[idx, 1]
        if self.transform:
            img = self.transform(img)
        if self.target_transform:
            label = self.target_transform(label)
        return img, label

device = "cuda" if t.cuda.is_available() else "cpu"

class NN(t.nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = t.nn.Flatten()
        self.Linear_relu_stack = t.nn.Sequential(
                t.nn.Linear(224*224, 512),
                t.nn.ReLU(),
                t.nn.Linear(512,512),
                t.nn.ReLU(),
                t.nn.Linear(512, 3),
                )
    def forward(self, x):
        x = self.flatten(x)
        return self.Linear_relu_stack(x)

model = NN().to(device)
dataloader = DataLoader(imgDataset("annotations.csv", "img/"), 3, True)

lr = 1e-3
bsize = 3
epochs = 11

loss_fn = t.nn.CrossEntropyLoss()
optim = t.optim.SGD(model.parameters(), lr=lr)

def train(dataloader, model, loss_fn, optim):
    size= len(dataloader.dataset)
    model.train()
    for batch, (x,y) in enumerate(dataloader):
        pr = model(x)
        loss = loss_fn(pr, y)

        loss.backward()
        optim.step()
        optim.zero_grad()

        if batch % 100 == 0:
            loss, current = loss.item(), batch*bsize+len(x)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

def test(dataloader, model, loss_fn):

    model.eval()
    size= len(dataloader.dataset)
    nbatch = len(dataloader)
    tloss, correct = 0,0

    with t.no_grad():
        for x,y in dataloader:
            pr = model(x)
            tloss += loss_fn(pr, y).item()
            correct += (pr.argmax(1) == y).type(t.float).sum().item()
    tloss /= nbatch
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {tloss:>8f} \n")

for i in range(epochs):
    print(f"Epoch {i+1}\n -----------------------------")
    train(dataloader, model, loss_fn, optim)
    test(dataloader, model, loss_fn)
print("\n\n Done!")    



    
#print(label[0])
#cv.imshow(dataset[0][1],dataset[0][0].numpy())
#cv.imshow(label[0], temp[0].numpy())
#cv.waitKey(0)
#cv.destroyAllWindows()
