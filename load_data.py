import pickle as pk

data_path=r'data/behaviordata'

with open(data_path,'rb') as f:
    data=pk.load(f)

data.shape()


