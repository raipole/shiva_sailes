import torch
from PIL.ImageOps import scale
from numba.cuda import target
from torch import nn,device
from torch.utils.data import Dataset,DataLoader
from torchvision import datasets
from torchvision.datasets import FashionMNIST
from torchvision.transforms import v2
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
import numpy as np


import os

os.environ["http_proxy"] = "http://shikas101%40bioconacademy.com:ibabuser@proxy.ibab.ac.in:3128"


class NeuralNetwork(nn.Module):

    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(in_features=28*28,out_features=512)
        self.relu1 = nn.ReLU()
        self.linear2 = nn.Linear(in_features=512,out_features=256)
        self.relu2 = nn.ReLU()
        self.linear3 = nn.Linear(in_features=256,out_features=128)
        self.relu3 = nn.ReLU()
        self.linear4 = nn.Linear(in_features=128,out_features=10)


    def forward(self, x):
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.relu1(x)
        x = self.linear2(x)
        x = self.relu2(x)
        x = self.linear3(x)
        x = self.relu3(x)
        logits = self.linear4(x)
        out=logits
        return out

def data_loader():

    train_dataset = datasets.FashionMNIST(root='./data',train=True,download=True,transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]))

    test_dataset=datasets.FashionMNIST(root='./data',train=True,download=False,transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]))



    return train_dataset,test_dataset



def train(mydataloader,model,loss_fn,optimizer,epochs,device,test_dataset):

    size=len(mydataloader.dataset)
    for epoch in range(epochs):
        model.train()
        for batch,(X,y) in enumerate(mydataloader):
            X,y=X.to(device),y.to(device)

            pred=model(X)
            loss=loss_fn(pred,y)

            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

            if batch%100==0:
                loss,corrent=loss.item(),(batch+1)*len(X)

                print('train loss:',loss)
                print('train corrent:',corrent)
    loss_score=[]
    for X,y in test_dataset:
        pred=model(X)
        loss=loss_fn(pred,y)
        loss=loss.item()
        loss_score.append(loss)
        print('Avarage test loss:',np.mean(loss_score))
        # acc=accuracy_score(y,pred)
        # print('accuracy:',acc)
        # loss_score.append(loss)
        loss,accuracy=model.evaluate(X,y)
        #
        print('loss:',loss)
        print('accuracy:',accuracy)
        #

        # print('test accuracy:',acc)

        #

        # print('test loss:',loss)
        # print('test accuracy:',accuracy)




def main():

    train_dataset,test_dataset=data_loader()

    train_data=DataLoader(train_dataset,batch_size=32,shuffle=True)
    test_data=DataLoader(test_dataset,batch_size=32,shuffle=True)

    # print('train shape:',train_data.shape)
    # print('test shape:',test_data.shape)

    device = torch.accelerator.current_accelerator().type if torch.cuda.is_available() else 'cpu'

    model = NeuralNetwork().to(device)

    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(),lr=0.001)



    print('device:',device)




    train(train_data,model,loss_fn,optimizer,epochs=5,device=device,test_dataset=test_data)



if __name__ == '__main__':
    main()
