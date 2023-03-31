# TOOLS FOR DATE AND TIME CALCULATIONS
# ------------------------------------

# LIBRARIES AND MODULES
import datetime # Python's internal date-time library

# Funktio, joka laskee päivämäärien eron päivinä
def datediff(d1, d2):
    """Calculates the difference between two dates in days

    Args:
        d1 (str): A date in ISO format YYYY-MM-DD
        d2 (str): A date in ISO format YYYY-MM-DD

    Returns:
        int: absolute difference in days
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d") # ISO standardin mukainen merkintä, käytä tätä sovelluksissa
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    difference =  abs((d2 - d1).days)
    return difference

# Funktio, joka laskee kahden kellonajan välisen eron tunteina
def timediff(t1, t2):
    """Calculates the difference between two dates in days

    Args:
        t1 (str): time value in format hh:mm:ss
        t2 (str): time value in format hh:mm:ss

    Returns:
        float: time difference in hours
    """

    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
    # Function calculates a timedelta which supports only seconds or microseconds
    seconds = abs((t2 - t1).seconds)
    hours = seconds / 3600 # minute 60 seconds * hour 60 minutes
    return hours


# Sama funktio, mutta toisella tapaa laskettu samalla laskutuloksella
# def timediff2(t1, t2):
#     t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
#     t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
#     return abs((t2 - t1).total_seconds() / 3600)

# Testi
# kesto = timediff2('10:00:00', '14:30:00')
# print(kesto)

def datediff2(d1, d2, unit):
    """Returns difference between 2 dates in chosen unit (day, month or year)

    Args:
        d1 (str): 1 st date in ISO format (YYYY-mm-dd)
        d2 (str): 2 nd date in ISO format (YYYY-mm-dd)
        unit (str): unit to return

    Returns:
        float: difference between in desired units
    """

    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d") # ISO standardin mukainen merkintä, käytä tätä sovelluksissa
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    difference =  abs((d2 - d1).days) # Timedelta in days
    units = {'day':1, 'year': 365, 'month': 30} # Dictionary for unit dividers
    divider = units[unit] # Choose by unit argument
    value = difference / divider
    return value
    
    
    # # Tämä on sama funktio, mutta toisella tapaa laskettu samalla laskutuloksella
    # d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    # d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    # difference =  abs((d2 - d1).days)
    # if unit == "day":
    #     value = difference
    # elif unit == "year":
    #     value = difference / 365
    # return value

def timediff2(t1, t2, unit):
    """Returns difference between 2 times in chosen unit (hour or minute)

    Args:
        t1 (str): 1 st time in ISO format (hh:mm:ss)
        t2 (str): 2 nd time in ISO format (hh:mm:ss)
        unit (str): unit to return

    Returns:
        float: time difference in chosen units
    """

    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
    units = {'hour': 3600, 'minute': 60, 'second': 60}
    seconds = abs((t2 - t1).seconds)
    divider = units[unit]  # Choose divider according to unit argument
    value = seconds / divider
    return value

# Testit
if __name__ == "__main__":

    # Let´s test date difference
    date1 = "2023-03-21"
    date2 = "2023-03-17"
    ero = datediff2(date1, date2, 'day')
    print(date1, 'ja', date2, 'ero on', ero, 'päivää.')

    # Let´s test time difference
    time1 = "10:00:00"
    time2 = "14:30:00"
    kesto = timediff2(time1, time2, 'hour')
    print('ero oli', kesto, 'tuntia')

    # Let´s test time difference in minutes
    time1 = "10:00:00"
    time2 = "15:25:00"
    kesto = timediff2(time1, time2, 'minute')
    print('ero oli', kesto, 'minuuttia')
    
