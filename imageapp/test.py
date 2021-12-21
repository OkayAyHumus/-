import numpy as np
from PIL import Image

# import sys
# sys.path.append("../model")
# from django.shortcuts import render, redirect

# import joblib 


from torchvision import transforms


import torch
import torch.nn as nn
# from model import Net

# import torch
import torch.nn as nn
# from  . import model
from torchvision.models import resnet18 

from ..model.mymodel import Net




im = np.array(Image.open('/Users/honmayasuyuki/Desktop/IMAGEPROJECT/imageproject/media/documents/1_41hMI4W.jpg'))

print(type(im))
# <class 'numpy.ndarray'>

print(im.dtype)
# uint8

print(im.shape)
# (225, 400, 3)

transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
im = transform(im)


net =Net().cpu().eval()
net.load_state_dict(torch.load('/model/f_mnist.pt', map_location=torch.device('cpu')))
y = net(im.unsqueeze(0))
y = torch.argmax(y)