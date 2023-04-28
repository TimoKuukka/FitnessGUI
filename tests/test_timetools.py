# TESTS FOR TIMETOOLS.PY


# import sys
# sys.path.append('../timetools')



# # IMPORT MODULES TO BE TESTED
import timetools


# UNIT TESTS

# Tests datediff function
def test_datediff():
    assert timetools.datediff('2023-04-28', '2023-04-10') == 18
    assert timetools.datediff('2023-04-10', '2023-04-28') == 18

# Tests timediff function calculates correct and absolute value
def test_timediff():
    assert timetools.timediff('11:30:00', '12:00:00') == 0.5
    assert timetools.timediff('10:00:00', '14:30:00') == 4.5

    # Test same diff with hours, minutes and seconds
    assert round(timetools.timediff('11:30:15', '10:10:05')), 4 == 1.3361
    


# # Tests datediff2 function calculates correct and absote value
# def test_datediff2():
#     assert timetools.datediff('2020-05-01', '2020-05-10') == 10
#     assert timetools.datediff('2020-05-10', '2020-05-01') == 10



