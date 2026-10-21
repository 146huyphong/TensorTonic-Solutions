import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    P = [math.exp(-lam) * lam ** i / math.factorial(i) for i in range(0, k + 1)]
    
    return  {
        "pmf": P[k], 
        "cdf": sum(P)
    }