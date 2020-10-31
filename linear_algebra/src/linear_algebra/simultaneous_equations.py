import torch

def generate_probrem(dim:int=4, high:int=20):
    while True:
        a = torch.randint(-high, high, (dim,dim)).float()
        if torch.det(a) != 0.0:
            break

    x = torch.randint(-high, high, (dim, 1)).float()
    b = a.matmul(x)

    return a, x, b

def upper_triu(a:torch.Tensor):
    if(len(a) <= 1):
        return a
    a_0 = a[0]
    a_1 = a[1:]
    m = a_1.t()[0].mul(1.0/a_0[0]).unsqueeze(0).t()
    a_0 = a_0.unsqueeze(0)
    a_1 -= m.matmul(a_0)

    a_2 = upper_triu(a_1[:, 1:])
    a_1 = torch.cat((a_1[:, 0].unsqueeze(1), a_2), 1)

    return(torch.cat((a_0, a_1), 0))

def gaussian_elimination(a:torch.Tensor, b:torch.Tensor):
    a = torch.cat((a,b), 1)
    print(a)
    a = upper_triu(a)
    a = a.t()
    b = a[-1].t()
    a = a[:-1].t()
    x = torch.zeros(b.shape)
    print(a)
    print(b)
    # あとできれいに書く
    for i in reversed(range(len(b))):
        x[i] = b[i]/a[i, i]
        for k in range(i):
            b[k] -= a[k, i] * x[i]
    return x

if __name__ == "__main__":
    a, x, b = generate_probrem(3, 5)
    x_ = gaussian_elimination(a, b)
    print(f"correct x:{x}")
    print(f"my x:{x_}")