from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import ModelFile


from torchvision import transforms
from PIL import Image

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

import sys
sys.path.append('../')
from model.mymodel import Net

transform = transforms.Compose([
                                transforms.ToTensor(),
                                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])



def classify(request):
    if request.method == 'POST':
        img = ModelFile.objects.all()
        # img = img[0]
        img_name = request.FILES['image']
        image_url = 'media/documents/{}'.format(img_name)
   

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            im = np.array(Image.open(image_url))

            # print(type(im))
           

            # print(im.dtype)
 
            im = transform(im)


            net =Net().cpu().eval()
            net.load_state_dict(torch.load('/Users/honmayasuyuki/Desktop/IMAGEPROJECT/imageproject/model/f_mnist.pt', map_location=torch.device('cpu')))
            y = net(im.unsqueeze(0))
            y_proba = F.softmax(y, dim=-1)
            y_proba = y.sort(dim=1, descending=True)
            y_proba_p = round(y_proba[0][0][0].item(),1)
            y_result = torch.argmax(y)

            
            return render(request,'imageapp/classify.html',{'y_result':y_result,'y_proba_p':y_proba_p , 'image_url':image_url})

    else:
        form = ImageForm()
        return render(request, 'imageapp/index.html', {'form':form})

# round(y_proba[0][0][0].item(),1)