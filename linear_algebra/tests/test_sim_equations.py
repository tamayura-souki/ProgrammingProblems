import math

import torch
import pytest

from linear_algebra.simultaneous_equations import *

def test_gaussian_elimination():
    for i in range(100):
        a, x, b = generate_probrem(10, 10)
        x_ = gaussian_elimination(a, b)
        error = torch.norm(a.matmul(x_)-b)
        assert error == pytest.approx(0.0, abs=1e-3)

def test_LU_solver():
    for i in range(100):
        a, x, b = generate_probrem(10, 10)
        x_ = LU_solver(a, b)
        error = torch.norm(a.matmul(x_)-b)
        assert error == pytest.approx(0.0, abs=1e-3)


if __name__ == "__main__":
    test_LU_solver()