def mod_binary(g, k, n):
    """
    Algolrithm for calcurating powers with binary method.
    the same as pow(g,k,p) in python.
    parameters
    ----------
    g : int
        base
    k : int
        exponents
    n : int
        mod

    Returns
    ----------
    y : int
        g^k mod p
    """

    y = 1
    num = len(bin(k)[2:])
    bin_k = bin(k)[2:]
    counter = 0
    for i in range(num):
        counter += 1
        if bin_k[i] == '1':
            y = (y**2 % n) * g % n
        else:
            y = y**2 % n
    print(f'{counter=}')
    return y
