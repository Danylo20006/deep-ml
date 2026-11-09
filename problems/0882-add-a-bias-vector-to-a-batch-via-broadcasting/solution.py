import torch

def add_bias(x: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    c = torch.tensor([])

    c = x + b

    return c  
    