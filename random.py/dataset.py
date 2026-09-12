import torch as t
import numpy as np
import os
import pandas as pd
import cv2 as cv
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
        img = t.from_numpy(cv.resize(cv.cvtColor(cv.imread(path), cv.COLOR_BGR2GRAY), (224,224)))
        label = self.labels.iloc[idx, 1]
        if self.transform:
            img = self.transform(img)
        if self.target_transform:
            label = self.target_transform(label)
        return img, label


dataloader = DataLoader(imgDataset("annotations.csv", "img/"), 3, True)
temp, label = next(iter(dataloader))

    
#print(label[0])
#cv.imshow(dataset[0][1],dataset[0][0].numpy())
cv.imshow(label[0], temp[0].numpy())
cv.waitKey(0)
cv.destroyAllWindows()
   
    
