from datetime import date, datetime
from django.test import TestCase
from django.utils import timezone

from .models import FuelStation, Receipt, Vehicle

# Create your tests here.
class FuelStationTest(TestCase):
    def test_case(self):
        """test desc"""
        pass

class VehicleTest(TestCase):
    def recent_model_with_year_gt_current_plus_2(self):
        """
        model's "recently manufactured" method returns true if model year within past 4 years. this tests the output if the model year is more than 2 years in the future (not possible IRL)
        """
        pass
