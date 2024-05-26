import unittest
from datetime import datetime

from options import get_expiration_dates


class TestOptions(unittest.TestCase):

    def test_get_expiration_dates(self):
        dates = get_expiration_dates('IBM')
        try:
            for date in dates:
                datetime.strptime(date, "%b %d, %Y")
        except ValueError:
            # Should not reach here!
            self.assertTrue(False)
