from typing import Tuple

import torch

def generate_probrem(dim:int=4, high:int=20) -> Tuple[torch.Tensor]:
    while True:
        a = torch.randint(-high, high, (dim,dim)).float()
        t = a.clone().abs()
        d = t.sum(dim=0)
        d += torch.ones(d.shape, dtype=d.dtype)
        d = d.unsqueeze(0)

        while True:
            sign = torch.randint(-high, high, d.shape).sign()
            sign = sign.float()
            if sign.abs().min() != 0:
                break

        d = d.t().matmul(sign)

        for i in range(d.shape[0]):
            a[i,i] = d[i,i]

        if torch.det(a) != 0.0:
            break

    x = torch.randint(-high, high, (dim, 1)).float()
    b = a.matmul(x)

    return a, x, b

def jacobi_solver(a:torch.Tensor, b:torch.Tensor) -> torch.Tensor:
    d = a.reciprocal().diagonal(0)
    assert not any(d.isinf())
    d = d.diagflat()
    e = a.tril(diagonal=-1)
    f = a.triu(diagonal=1)

    m = -d.matmul(e+f)
    c = d.matmul(b)

    x_0 = c
    for i in range(10**5):
        x_1 = m.matmul(x_0) + c

        if (x_1-x_0).norm().abs() < 0.00001:
            break

        x_0 = x_1

    return x_1

if __name__ == "__main__":
    a, x, b = generate_probrem()
    x_ = jacobi_solver(a, b)
    print(f"a:{a}")
    print(f"b:{b}")
    print(f"correct x: {x}")
    print(f"my x: {x_}")