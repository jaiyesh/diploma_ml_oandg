def klinkenberg(kg,pm,k):
    
    """
    This klinkenberg function calculates absolute permeability for given gas permeability at a given mean pressure.
    INPUTS:
    kg=> gas permeability in lab at a given mean pressure pm
    pm => mean pressure
    k=>User initial guess for absolute perm.
    
    return:
    k=> value of absolute permeability
    
    """
    count = 0

    while (abs(6.9*k**0.64+pm*k - pm*kg)>0.0000000001):
        k = k - ((6.9*k**0.64+pm*k - pm*kg)/(4.416*(k**(-0.36))+pm))
        count=count+1

    print(f"The final value of Perm K is: {k} ")
    print(f"The number of iterations used = {count}")

    return k



