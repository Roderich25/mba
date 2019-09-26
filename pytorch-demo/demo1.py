import torch
import torchvision
from torchvision import transforms, datasets
import matplotlib.pyplot as plt
from collections import Counter, OrderedDict

train = datasets.MNIST("", train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))
test = datasets.MNIST("", train=False, download=True, transform=transforms.Compose([transforms.ToTensor()]))

trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)

for data in trainset:
    print(data)
    break

x, y = data[0][0], data[1][0]

print(y)
print(x.shape)

plt.imshow(x.view(28, 28))
plt.show()

counter_list = []
for data in trainset:
    _, Y = data
    for y in Y:
        counter_list.append(int(y))

counter_dict = Counter(counter_list)
total = sum(counter_dict.values())
print(OrderedDict(sorted(counter_dict.items())))

for i in counter_dict:
    print(f"{i}: {counter_dict[i]/total*100}")
