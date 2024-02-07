import torch

import torch

tnsr = torch.randn(10)

if torch.cuda.is_available():
    device = torch.device("cuda")
else: 
    device = torch.device("cpu")

tnsr = tnsr.to(device)
print("Tensor original:", tnsr)
print("Dispositivo do tensor original:", tnsr.device)

# Crie um tensor na GPU para verificar se a GPU está funcionando corretamente
test_tensor = torch.tensor([1]).to(device)
print("Test Tensor:", test_tensor)
print("Dispositivo do Test Tensor:", test_tensor.device)
