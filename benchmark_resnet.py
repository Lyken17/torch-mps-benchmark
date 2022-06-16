import time
import numpy as np

import torch 
import torch.nn as nn
import torch.nn.functional as F

from torchvision import models

net = models.resnet50()
data = torch.randn(1, 3, 224, 224)


def benchmark_cpu(net, data, device="cpu", repeats=200):
    net = net.to(device)
    data = data.to(device)

    for i in range(5):
        net(data)

    start = time.time()
    for i in range(repeats):
        net(data)

    end = time.time() 
    print(f"({device}, {data.shape})  Latency {(end - start) / repeats * 1000:.2f} ms")

for bs in ( 8,):
    data = torch.randn(bs, 3, 224, 224)
    benchmark_cpu(net, data, device="cpu")
    benchmark_cpu(net, data, device="mps")