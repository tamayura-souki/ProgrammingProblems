import torch
import pytest

from linear_algebra.jacobi_solver import *

def test_jacobi_solver():
    for i in range(100):
        a, x, b = generate_probrem(10, 10)
        x_ = jacobi_solver(a, b)
        error = torch.norm(a.matmul(x_)-b)
        assert error == pytest.approx(0.0, abs=1e-3)