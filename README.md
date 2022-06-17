# Benchmark M1 results

## Setup

```
# Install M1 version anaconda
wget https://repo.anaconda.com/archive/Anaconda3-2022.05-MacOSX-arm64.sh -O anaconda.sh

bash anaconda.sh -b

pip install --pre torch torchvision --extra-index-url https://download.pytorch.org/whl/nightly/cpu
```


## Inference Benchmark (M1 Air)

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

## Training Benchmark (M1 Air)

* Transformer (need to reduce the feat_sizes otherwise OOM)

    bs  | cpu | mps
    --- | --- | ---
    1   | 77.2ms | Error
    2   | 98.2ms | Error
    4   | 162.5ms | Error
    8   | 248.6ms | Error

* ResNet-50 (need to reduce the num_classes otherwise OOM)

    bs  | cpu | mps
    --- | --- | ---
    1   | 124.2ms | Error
    2   | 234.0ms | Error
    4   | 469.1ms | Error
    8   | 866.7ms | Error