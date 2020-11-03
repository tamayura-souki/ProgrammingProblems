import torch
import pytest
from linear_algebra.simultaneous_equations import *

def test_gaussian_elimination():
    a, x, b = generate_probrem(3, 5)
    x_ = gaussian_elimination(a, b)
    epsilon = torch.norm(x-x_)
    assert epsilon == 0.0

def test_LU_solver():
    a, x, b = generate_probrem(3, 5)
    x_ = LU_solver(a, b)
    epsilon = torch.norm(x-x_)
    assert epsilon == 0.0


if __name__ == "__main__":
    test_gaussian_elimination()