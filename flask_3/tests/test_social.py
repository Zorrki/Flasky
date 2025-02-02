import unittest
from social_age import get_social_status

class TestSocialStatus(unittest.TestCase):

    def test_if_can_get_child_status(self):
        age = 3
        expected_res = 'ребенок'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res, 'Not matched')

if __name__ == '__main__':
    unittest.main()