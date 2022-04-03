from datetime import datetime, date

def estimate(units, start_date, end_date, watt_production_capacity=0.0027):
    """
    Returns size of system

    Parameters
    ----------
    units : int
        consumed units in a give time frame
    start_date : datetime.date object
        consumption on the first day of the energy bill
    end_date : datetime.date object
        consumption on the last day of the energy bill
    watt_production_capacity : float, optional
        Rule of thumb: 1 Watt produces 0.0027 units per day (varies as per size, check for the irradiance map)
    
    Returns
    -------
    estimate : dict
        Dictionary with attributes system_size, the Watt size required,
        daily consumption, measured in kwH per day,
        yearly consumption, measured in kwH per year.˜
    
    Example
    -------
    >>> estimate(778,"2021/4/9","2022/5/3")
    {'system_size': 740.7407407407406, 'kwh_per_day': 2.0, 'kwh_per_year': 730.0}
    """
    date_format = "%Y/%m/%d"
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)
    delta_days = (end_date - start_date).days
    return {
        "system_size": units/delta_days/watt_production_capacity,
        "kwh_per_day": units/delta_days,
        "kwh_per_year": units/delta_days * 365
    }

if __name__ == "__main__":
    import doctest
    doctest.testmod()