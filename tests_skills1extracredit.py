import unittest

from skills1_extracredit import *


class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
        self.word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]


    def test_1_A_f_all_odd(self):
        self.assertEqual(f_all_odd, [-5, 15, 23, 7])

    def test_1_B_f_all_even(self):
        self.assertEqual(f_all_even, [6, 4, 8, 16, 42, 2])

    def test_1_C_f_long_words(self):
        self.assertEqual(f_long_words, ["What", "about", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "spam"])

    def test_1_D_f_smallest(self):
        self.assertEqual(f_smallest, -5)
"""
    def test_1_E_largest(self):
        self.assertEqual(largest(self.number_list), 42)

    def test_1_F_halvesies(self):
        self.assertEqual(halvesies(self.number_list), [-2.5, 3.0, 2.0, 4.0, 7.5, 8.0, 11.5, 21.0, 1.0, 3.5])

    def test_1_G_word_lengths(self):
        self.assertEqual(word_lengths(self.word_list), [4, 5, 3, 4, 7, 4, 4, 5, 4, 6, 3, 4])

    def test_1_H_sum_numbers(self):
        self.assertEqual(sum_numbers(self.number_list), 118)

    def test_1_I_join_strings(self):
        self.assertEqual(join_strings(self.word_list), "WhatabouttheSpamsausagespamspambaconspamtomatoandspam")

    def test_1_J_average(self):
        self.assertEqual(average(self.number_list), 11.8)
"""
if __name__ == '__main__':
    unittest.main()