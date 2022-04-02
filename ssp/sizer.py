from datetime import datetime, date

def estimate(units, start_date, end_date):
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
    Returns
    -------
    sysetm : size
        Sysetm size
    
    >>> estimate(778,"2021/4/9","2022/5/3")
    2.0
    """
    date_format = "%Y/%m/%d"
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)
    delta_days = (end_date - start_date).days
    return units/delta_days

if __name__ == "__main__":
    import doctest
    doctest.testmod()