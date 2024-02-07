
#tipos de tensores

import torch
import numpy as np 

lista = [[1,2,3],[4,5,6]]

#tipo float 32
tnsInt = torch.Tensor(lista)
print(tnsInt.dtype)
print(tnsInt)

#tipo float 32

tsnFloat = torch.FloatTensor(lista)
print(tsnFloat.dtype)
print(tsnFloat)

#tipo float 64
tnsFloat64 = torch.DoubleTensor(lista)
print(tnsFloat64.dtype)
print(tnsFloat64)

#tipo inrteiro 
tnsInt = torch.LongTensor(lista)
print(tnsInt.dtype)
print(tnsInt)


#from numpy 

arr = np.random.rand(3,4)
tnsNp = torch.from_numpy(arr)
print(tnsNp)

#tensor para array 

tnsRand = torch.randn(3,3)
arrTns = tnsRand.data.numpy()
print(arrTns)

