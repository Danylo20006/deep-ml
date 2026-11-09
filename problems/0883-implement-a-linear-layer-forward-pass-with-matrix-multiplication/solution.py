import torch

def linear_forward(x: torch.Tensor, W: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    W = W.transpose(0,1)

    output = torch.tensor([])
    output = x @ W + b

    return output