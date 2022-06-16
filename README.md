# Benchmark M1 results

## Setup

```
# Install M1 version anaconda
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-MacOSX-arm64.sh -O anaconda.sh

bash anaconda.sh -b

pip install --pre torch torchvision --extra-index-url https://download.pytorch.org/whl/nightly/cpu
```


## Benchmark (m1 air)

* Transformer

    bs  | cpu | mps
    --- | --- | ---
    1   | 29.9ms | 114.8ms
    2   | 40.9ms | 148.6ms
    4   | 70.6ms | 179.8ms
    8   | 117.1ms | 209.3ms

* ResNet-50

    bs  | cpu | mps
    --- | --- | ---
    1   | 44.1ms | 113.3ms
    2   | 78.2ms | 130.6ms
    4   | 137.6ms | 191.8ms
    8   | 279.1ms | 295.4ms