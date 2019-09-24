from datetime import date, datetime

from django.test import TestCase
from django.utils import timezone

from ..models import Vehicle

print('inside test_Vehicle')
print(timezone.now())
# Create your tests here.
class VehicleModelTests(TestCase):
	def test_recent_model_with_year_gt_current_plus_2(self):
		"""
		model's is_recent_model() method returns False if the model year is more than 3 years in the future (not possible IRL)
		"""
		year_3_yrs_future = timezone.now().year + 3
		print(year_3_yrs_future)
		future_car = Vehicle(year=year_3_yrs_future)
		self.assertIs(future_car.is_recent_model(), False)
