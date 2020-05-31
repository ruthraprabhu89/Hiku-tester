import hiker
import unittest


class TestHiker(unittest.TestCase):

	def test_check_if_number_of_lines_is_not_equal_to_three(self):
		'''simple example to start you off'''
		tester = hiker.Hiker()
		with self.assertRaises(ValueError):
			tester_string = "happy purple frog/eating bugs in the marshes"
			tester.haiku(tester_string)
		with self.assertRaises(ValueError):
			tester_string = "happy purple frog/eating bugs in the marshes/get indigestion/extra line for test"
			tester.haiku(tester_string)

	def test_if_contains_uppercase(self):
		tester = hiker.Hiker()
		with self.assertRaises(ValueError):
			tester_string = "happy purple frog/eating bugs in the marshes/GEt indigestion"
			tester.haiku(tester_string)

	def test_if_contains_specialchar(self):
		tester = hiker.Hiker()
		with self.assertRaises(ValueError):
			tester_string = "happy purple frog/eating bugs in the$ marshes/get indigestion"
			tester.haiku(tester_string)

	def test_if_contains_numbers(self):
		tester = hiker.Hiker()
		with self.assertRaises(ValueError):
			tester_string = "happy purple frog/eating bugs in the5 marshes6/get indigestion"
			tester.haiku(tester_string)

	def test_input_greater_than_200_characters(self):
		tester = hiker.Hiker()
		with self.assertRaises(ValueError):
			tester_string = "happy purple froghappy purple froghappy purple froghappy purple frog/eeeeating bugs in the marsheeeeseeeeating bugs in the marsheeees/get indigeeeestionget indigeeeestionget indigeeeestionget indigeeeestion"
			tester.haiku(tester_string)

	def test_input_more_than_two_contiguous_vowels(self):
		tester = hiker.Hiker()
		tester_string = "happy purple frog/eeeeeeating bugs in the marsheeeeees/get indigeeeeestion"
		self.assertEqual(tester.haiku(tester_string), (5,7,5,'Yes'))

	def test_input_multiple_whitespace(self):
		tester = hiker.Hiker()
		tester_string = "happy purple frog/eating   bugs in the   marshes/get   indigestion"
		self.assertEqual(tester.haiku(tester_string), (5,7,5,'Yes'))

	def test_input_has_no_vowels(self):
		tester = hiker.Hiker()
		tester_string = "bbbb bbbb bbbb/ccc ccc ccc/ddd ddd ddd"
		self.assertEqual(tester.haiku(tester_string), (3,3,3,'No'))


if __name__ == '__main__':
	unittest.main()  # pragma: no cover