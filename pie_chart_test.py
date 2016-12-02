import unittest

from pie_chart import draw_pie_chart

class PieChartTest(unittest.TestCase):

	def setUp(self):
		self.history1 = [{"handling_process":"Remeasured","characteristic_id":415,\
					"measured_value":34.95,"reason":"Error in measurement"},\
					{"handling_process":"Remeasured","characteristic_id":415,\
					"measured_value":34.95,"reason":"Error in measurement"},\
					{"handling_process":"Remeasured","characteristic_id":415,\
					"measured_value":34.95,"reason":"Error in measurement"},\
					{"handling_process":"Remeasured","characteristic_id":415,\
					"measured_value":34.95,"reason":"Error in Value"},\
					{"handling_process":"Remeasured","characteristic_id":415,\
					"measured_value":34.95,"reason":"Error in Value"},
					{"handling_process":"Remeasured","characteristic_id":415,\
					"measured_value":34.95,"reason":"Error in frequency"}]

		self.history2 = [{"handling_process":"Remeasured","characteristic_id":415,\
					"measured_value":34.95,"reaso":"Error in measurement"},\
					{"handling_process":"Remeasured","characteristic_id":415,\
					"measured_value":34.95,"reason":"Error in measurement"},\
					{"handling_process":"Remeasured","characteristic_id":415,\
					"measured_value":34.95,"reason":"Error in measurement"},\
					{"handling_process":"Remeasured","characteristic_id":415,\
					"measured_value":34.95,"reason":"Error in Value"},\
					{"handling_process":"Remeasured","characteristic_id":415,\
					"measured_value":34.95,"reason":"Error in Value"},
					{"handling_process":"Remeasured","characteristic_id":415,\
					"measured_value":34.95,"reason":"Error in frequency"}]

		self.history3 = []




	def test_draw_pie_chart(self):
		self.assertEqual(draw_pie_chart(self.history1),\
			[['Error in measurement', 3], ['Error in Value', 2],\
			['Error in frequency', 1]])

	def test_empty_history(self):
		self.assertEqual(draw_pie_chart(self.history3),\
			[['History is empty', 0]])

	def test_error_in_reason_field(self):
		self.assertEqual(draw_pie_chart(self.history2),\
			[['Invalid Input', 0]])

		
if __name__ == '__main__':
	unittest.main()