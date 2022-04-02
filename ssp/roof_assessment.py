def roof_size(system_size, sqm_per_kw_needed=7.0):
    """
    Retunrs an estimate of the required roof size for a given system size
    
    Parameters
    ----------
    system_size : float
        The size of the photovoltaic system in Watt
    sqm_per_kw_needed : float
        The required sq. m per kW need. Rule of thumb is 1 kW requires 6-8 sq. m
    
    Returns : float
        The required roof size to place the PV system
    
    Example
    -------
    >>> roof_size(3522.34)
    24.656380000000002
    """
    return system_size/1000 * sqm_per_kw_needed

if __name__ == "__main__":
    import doctest
    doctest.testmod()