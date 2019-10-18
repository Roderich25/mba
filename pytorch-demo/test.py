import torch

x = torch.Tensor([5, 3])
y = torch.Tensor([2, 1])
print(x*y)

z = torch.zeros([2, 5])
print(z)
print(z.shape)

r = torch.rand([2, 5])
print(r)
r = r.view([1, 10])
print(r)

