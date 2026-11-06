import torch

def to_float_tensor(values):
    # values = torch.tensor(values)
    # input = values.to(dtype=torch.float32)
    # return input

    return torch.tensor(values, dtype=torch.float32)