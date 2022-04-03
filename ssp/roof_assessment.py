def roof_size(system_size, area_of_obstruction=0, fire_safety_setback=0,
              available_area=9999999, sqm_per_kw_needed=7.0):
    """
    Returns an estimate of the required roof size for a given photovoltaic
    system size. If the parameter `available_area` is supplied this method
    checks if the size of the area is big enough, otherwise an error
    is thrown. Also the maximum constructible area will be returned.
    
    Parameters
    ----------
    system_size : float
        The size of the photovoltaic system in Watt.
    area_of_obstruction : float
        The area of obstruction, e.g. due to chimneys, defaults to 0.
    fire_safety_seatback : float
        The area of fire safety, measured in sq. m, defaults to 0.
    available_area : float
        The size of the roof, defaults to 9999999.
    sqm_per_kw_needed : float
        The required sq. m per kW need. Rule of thumb is 1 kW requires
        6-8 sq. m., defaults to 7.
    
    Returns
    -------
    recommended_area : float
    maximum_constructible_area : float

    
    Example
    -------
    >>> roof_size(3522.34, 4,(4*1.25*2), 53)
    {'recommended_area': 38.65638, 'maximum_constructible_area': 39.0}
    
    >>> roof_size(3522.34, 4,(4*1.25*2), 21)
    Traceback (most recent call last):
    Exception: The roof of 21 sq. m. is too small to install the recmomended size of 38.65638sq. m., since the maximum contructible area is 7.0.
    """
    recommended_area = (system_size/1000 * sqm_per_kw_needed) + area_of_obstruction + fire_safety_setback
    maximum_constructible_area = available_area - area_of_obstruction - fire_safety_setback
    try:
        assert maximum_constructible_area > recommended_area
    except AssertionError:
        raise Exception("The roof of " + str(available_area) + " sq. m. is too \
small to install the recmomended size of " + str(recommended_area) + "sq. m., \
since the maximum contructible area is " + str(maximum_constructible_area) + ".\
")
    return {
        "recommended_area": recommended_area,
        "maximum_constructible_area": maximum_constructible_area
    }

if __name__ == "__main__":
    import doctest
    doctest.testmod()