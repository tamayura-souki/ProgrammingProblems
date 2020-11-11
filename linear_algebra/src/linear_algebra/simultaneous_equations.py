from typing import Tuple

import torch

def generate_probrem(dim:int=4, high:int=20) -> Tuple[torch.Tensor]:
    while True:
        a = torch.randint(-high, high, (dim,dim)).float()
        if torch.det(a) != 0.0:
            break

    x = torch.randint(-high, high, (dim, 1)).float()
    b = a.matmul(x)

    return a, x, b

def pivot_matrix(i:int, k:int, n:int) -> torch.Tensor:
    pivot = torch.eye(n)
    if i == k:
        return pivot
    pivot[i, k] = 1.0
    pivot[k, i] = 1.0
    pivot[i, i] = 0.0
    pivot[k, k] = 0.0
    return pivot

def swap_row(row_0:int, row_1:int, a:torch.Tensor) -> torch.Tensor:
    assert len(a.shape) == 2
    pivot = pivot_matrix(row_0, row_1, a.shape[0])
    pivot = pivot.to(a.dtype)
    return pivot.matmul(a)

def LU_decomposition(
    a:torch.Tensor, idx:torch.Tensor=None
    ) -> Tuple[torch.Tensor]:

    m_0 = torch.zeros(a[0].shape)
    m_0[..., 0] = 1
    if(len(a) <= 1):
        return a, m_0.unsqueeze(0), idx

    if idx is None:
        idx = torch.arange(0, a.shape[0], dtype=torch.int64).unsqueeze(0)
        idx = idx.t()

    _, max_idx = torch.max(a.t(), 1)
    max_idx = max_idx[0]
    a = swap_row(0, max_idx, a)
    idx = swap_row(0, max_idx, idx)

    a_0 = a[0]
    a_1 = a[1:]
    m_1 = a_1.t()[0].mul(1.0/a_0[0]).unsqueeze(0).t()

    a_0 = a_0.unsqueeze(0)
    a_1 -= m_1.matmul(a_0)

    a_2, m_2, idx_2 = LU_decomposition(a_1[:, 1:], idx=idx[1:])
    a_1 = torch.cat((a_1[:, 0].unsqueeze(1), a_2), 1)
    m_1 = torch.cat((m_1, m_2), 1)

    a = torch.cat((a_0, a_1), 0)
    m_0 = m_0.unsqueeze(0)
    m = torch.cat((m_0, m_1), 0)
    idx = torch.cat((idx[0:1], idx_2), 0)

    return a, m, idx

def forward_substitution(
    a:torch.Tensor, b:torch.Tensor, reverse=False
    ) -> torch.Tensor:
    x = torch.zeros(b.shape)
    indices = list(range(len(b)))
    N = len(indices)
    indices = indices if not reverse else reversed(indices)
    k_range = (lambda t: range(t)) if reverse \
        else (lambda t: range(t, N))
    for i in indices:
        x[i] = b[i]/a[i, i]
        for k in k_range(i):
            b[k] -= a[k, i] * x[i]

    return x

def gaussian_elimination(
    a:torch.Tensor, b:torch.Tensor
    ) -> torch.Tensor:
    a = torch.cat((a,b), 1)
    a, m, _ = LU_decomposition(a)
    a = a.t()
    b = a[-1].t()
    a = a[:-1].t()

    x = forward_substitution(a, b, True)
    return x.unsqueeze(0).t()

def LU_solver(a:torch.Tensor, b:torch.Tensor) -> torch.Tensor:
    a, m, _ = LU_decomposition(a)
    y = forward_substitution(m, b)
    x = forward_substitution(a, y, True)
    return x

if __name__ == "__main__":
    a, x, b = generate_probrem(3, 5)
    x_ = gaussian_elimination(a, b)
    print(f"correct x:{x}")
    print(f"my x:{x_}")