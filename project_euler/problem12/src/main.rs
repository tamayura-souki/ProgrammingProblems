#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_divisor_num() {
        assert_eq!(1, divisor_num(1));
        assert_eq!(2, divisor_num(3));
        assert_eq!(4, divisor_num(6));
        assert_eq!(4, divisor_num(10));
        assert_eq!(4, divisor_num(15));
        assert_eq!(4, divisor_num(21));
        assert_eq!(6, divisor_num(28));
        assert_eq!(12, divisor_num(5050));
        assert_eq!(405, divisor_num(48024900));
    }
}

fn divisor_num(n: u64) -> u64 {
    if n == 1 {
        return 1
    }
    let mut d_count:u64 = 0;
    let mut lim:u64 = n;
    for i in 1..n {
        if lim <= i {
            break;
        }
        if n % i == 0 {
            lim = n/i;
            if lim == i {
                d_count += 1;
                break;
            }else {
                d_count += 2;
            }
        }
    }
    d_count
}

fn main() {
    let mut i:u64 = 1;
    let mut sum:u64 = 0;
    let mut dn_max = 0;
    loop {
        match sum.checked_add(i) {
            Some(x) => sum = x,
            None => {
                panic!("OverFlow");
            }
        }
        let d_n = divisor_num(sum);
        if d_n > dn_max {
            dn_max = d_n;
            println!("{}({}) has {} divisors.", sum, i, d_n);
        }
        if  d_n > 500 {
            println!("Answer is {}", sum);
            break;
        }
        i+=1;
    }
}
