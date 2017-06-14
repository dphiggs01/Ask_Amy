from ask_amy.tests.utility import TestCaseASKAmy
from ask_amy.utilities.time_of_day import TimeOfDay
from unittest.mock import MagicMock
from unittest import mock

from datetime import datetime, date

class DatetimeWrapper(datetime):
    "A wrapper for datetime that can be mocked for testing."

    def __new__(cls, *args, **kwargs):
        return datetime.__new__(datetime, *args, **kwargs)

# @mock.patch('datetime.datetime', FakeDatetime)
# datetime.now = MagicMock(return_value=datetime.now())
# from datetime import datetime
# FakeDatetime.now = classmethod(lambda cls: datetime(2017, 7, 4, 12, 00, 00))

class TestTimeOfDay(TestCaseASKAmy):
    def setUp(self):
        pass

    def test_day_night(self):
        breakfast = datetime(2017, 7, 4, 8, 00, 00)
        back_two_hr = TimeOfDay.current_time(-2, breakfast)
        forward_one_hr = TimeOfDay.current_time(1, breakfast)
        #self.assertEquals('06:00 AM',back_two_hr)
        #self.assertEquals('09:00 AM',forward_one_hr)
        print(back_two_hr)
        print(forward_one_hr)

    def test_mealtime(self):
        time_desc=['Breakfast', 'Lunch', 'Dinner', 'Daytime', 'Nighttime']
        lunch = datetime(2017, 7, 4, 12, 00, 00)
        meal_1 = TimeOfDay.meal_time(-1,lunch)
        meal_2 = TimeOfDay.meal_time(4,lunch)
        meal_3 = TimeOfDay.meal_time(5,lunch)
        self.assertEquals(TimeOfDay.Breakfast,meal_1)
        self.assertEquals(TimeOfDay.Lunch,meal_2)
        self.assertEquals(TimeOfDay.Dinner,meal_3)
        # print(time_desc[meal_1])

    def test_day_night(self):
        time_desc=['Breakfast', 'Lunch', 'Dinner', 'Daytime', 'Nighttime']
        lunch = datetime(2017, 7, 4, 12, 00, 00)
        tod_1 = TimeOfDay.day_night(0,lunch)
        tod_2 = TimeOfDay.day_night(8,lunch)
        tod_3 = TimeOfDay.day_night(-8,lunch)
        self.assertEquals(TimeOfDay.Daytime,tod_1)
        self.assertEquals(TimeOfDay.Nighttime,tod_2)
        self.assertEquals(TimeOfDay.Nighttime,tod_3)
        # print(time_desc[tod_1])
        # print(time_desc[tod_2])

    def test_time_adj(self):
        lunch = datetime(2017, 7, 4, 12, 22, 00)
        time_adj = TimeOfDay.time_adj("01:22","PM",lunch)
        print(time_adj)
