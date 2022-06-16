import time
import numpy as np

import torch 
import torch.nn as nn
import torch.nn.functional as F

from torchvision import models

net = nn.Transformer() # models.resnet50()



def benchmark_cpu(net, data, target, device="cpu", repeats=200):
    net = net.to(device)
    data = data.to(device)
    target = target.to(device)

    for i in range(5):
        net(data, target)

    start = time.time()
    for i in range(repeats):
        net(data, target)

    end = time.time() 
    print(f"({device}, {data.shape})  Latency {(end - start) / repeats * 1000:.2f} ms")

for bs in (1, 2, 4, 8):
    data = torch.randn(bs, 32, 512)
    target = torch.randn(bs, 32, 512)
    benchmark_cpu(net, data, target, device="cpu")
    benchmark_cpu(net, data, target, device="mps")