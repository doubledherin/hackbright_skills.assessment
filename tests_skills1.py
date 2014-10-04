import unittest

from skills1 import *

class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
        self.word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]


    def test_1_A_all_odd(self):
        self.assertEqual(all_odd(self.number_list), [-5, 15, 23, 7])

    def test_1_B_all_even(self):
        self.assertEqual(all_even(self.number_list), [6, 4, 8, 16, 42, 2])

    def test_1_C_long_words(self):
        self.assertEqual(long_words(self.word_list), ["What", "about", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "spam"])

    def test_1_D_smallest(self):
        self.assertEqual(smallest(self.number_list), -5)

    def test_1_E_largest(self):
        self.assertEqual(largest(self.number_list), 42)

    def test_1_F_halvesies(self):
        self.assertEqual(halvesies(self.number_list), [-2.5, 3.0, 2.0, 4.0, 7.5, 8.0, 11.5, 21.0, 1.0, 3.5])

    def test_1_G_word_lengths(self):
        self.assertEqual(word_lengths(self.word_list), [4, 5, 3, 4, 7, 4, 4, 5, 4, 6, 3, 4])

    def test_1_H_sum_numbers(self):
        self.assertEqual(sum_numbers(self.number_list), 118)
"""
        self.assertEqual(self.months, ['Jan', 'Feb', 42, 37, 'Nov', 'Dec'])
        self.assertEqual(self.notes, ['Do', 'Re', 42, 37, 'Ti', 'Do'])
        self.assertEqual(self.multiples, [0, 3, 42, 37, 24, 27])

    def test_1_M_delete_third_and_seventh(self):
        delete_third_and_seventh(self.months)
        delete_third_and_seventh(self.notes)
        delete_third_and_seventh(self.multiples)

        self.assertEqual(self.months, ['Jan', 'Feb', 'Apr', 'May', 'Jun', 'Aug',
                                       'Sep', 'Oct', 'Nov', 'Dec'])
        self.assertEqual(self.notes, ['Do', 'Re', 'Fa', 'So', 'La', 'Do'])
        self.assertEqual(self.multiples, [0, 3, 9, 12, 15, 21, 24, 27])

    def test_1_N_delete_middle(self):
        delete_middle(self.months)
        delete_middle(self.notes)
        delete_middle(self.multiples)

        self.assertEqual(self.months, ['Jan', 'Feb', 'Nov', 'Dec'])
        self.assertEqual(self.notes, ['Do', 'Re', 'Ti', 'Do'])
        self.assertEqual(self.multiples, [0, 3, 24, 27])

    ### Tests for Part 2 ###

    def test_2_A_custom_len(self):
        self.assertEqual(custom_len(self.months), 12)
        self.assertEqual(custom_len(self.notes), 8)
        self.assertEqual(custom_len(self.multiples), 10)

    def test_2_B_custom_append(self):
        custom_append(self.months, 'Hex')
        custom_append(self.notes, 'Re')
        custom_append(self.multiples, 30)

        self.assertEqual(self.months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
                                       'Hex'])
        self.assertEqual(self.notes, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
                                      'Do', 'Re'])
        self.assertEqual(self.multiples, [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_2_C_custom_extend(self):
        custom_extend(self.months, ['Bin', 'Tri', 'Hex'])
        custom_extend(self.notes, ['Re', 'Mi', 'Fa', 'So'])
        custom_extend(self.multiples, [30, 33, 36, 39, 42, 45])

        self.assertEqual(self.months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
                                       'Bin', 'Tri', 'Hex'])
        self.assertEqual(self.notes, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
                                      'Do', 'Re', 'Mi', 'Fa', 'So'])
        self.assertEqual(self.multiples, [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30,
                                          33, 36, 39, 42, 45])

    def test_2_D_custom_insert(self):
        custom_insert(self.months, 8, 'Hex')
        custom_insert(self.notes, len(self.notes), 'Re')
        custom_insert(self.multiples, 0, -3)

        self.assertEqual(self.months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                       'Jul', 'Aug', 'Hex', 'Sep', 'Oct', 'Nov',
                                       'Dec'])
        self.assertEqual(self.notes, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
                                      'Do', 'Re'])
        self.assertEqual(self.multiples, [-3, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_2_E_custom_remove(self):
        custom_remove(self.months, 'Jul')
        custom_remove(self.notes, 'Do')
        custom_remove(self.multiples, 27)

        self.assertEqual(self.months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                       'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        self.assertEqual(self.notes, ['Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'])
        self.assertEqual(self.multiples, [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_2_F_custom_pop(self):
        self.assertEqual(custom_pop(self.months), 'Dec')
        self.assertEqual(custom_pop(self.notes), 'Do')
        self.assertEqual(custom_pop(self.multiples), 27)

        self.assertEqual(self.months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov'])
        self.assertEqual(self.notes, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti'])
        self.assertEqual(self.multiples, [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_2_G_custom_index(self):
        self.assertEqual(custom_index(self.months, 'Jul'), 6)
        self.assertEqual(custom_index(self.notes, 'Do'), 0)
        self.assertEqual(custom_index(self.multiples, 27), 9)

    def test_2_H_custom_count(self):
        self.assertEqual(custom_count(self.months, 'Jul'), 1)
        self.assertEqual(custom_count(self.notes, 'Do'), 2)
        self.assertEqual(custom_count(self.multiples, 27), 1)

    def test_2_I_custom_reverse(self):
        custom_reverse(self.months)
        custom_reverse(self.notes)
        custom_reverse(self.multiples)

        self.assertEqual(self.months, ['Dec', 'Nov', 'Oct', 'Sep', 'Aug', 'Jul',
                                       'Jun', 'May', 'Apr', 'Mar', 'Feb', 'Jan'])
        self.assertEqual(self.notes, ['Do', 'Ti', 'La', 'So', 'Fa', 'Mi', 'Re',
                                      'Do'])
        self.assertEqual(self.multiples, [27, 24, 21, 18, 15, 12, 9, 6, 3, 0])

    def test_2_J_custom_contains(self):
        self.assertTrue(custom_contains(self.months, 'Jul'))
        self.assertTrue(custom_contains(self.notes, 'Do'))
        self.assertTrue(custom_contains(self.multiples, 27))

        self.assertFalse(custom_contains(self.months, 'Hex'))
        self.assertFalse(custom_contains(self.notes, 'Go'))
        self.assertFalse(custom_contains(self.multiples, 30))

    def test_2_K_custom_equality(self):
        self.assertTrue(custom_equality(self.months, ['Jan', 'Feb', 'Mar', 'Apr',
                                                      'May', 'Jun', 'Jul', 'Aug',
                                                      'Sep', 'Oct', 'Nov', 'Dec']))
        self.assertTrue(custom_equality(self.notes, ['Do', 'Re', 'Mi', 'Fa', 'So',
                                                     'La', 'Ti', 'Do']))
        self.assertTrue(custom_equality(self.multiples, [0, 3, 6, 9, 12, 15, 18,
                                                         21, 24, 27]))

        self.assertFalse(custom_equality(self.months, ['Jan', 'Feb', 'Mar', 'Apr',
                                                      'May', 'Jun', 'Aug', 'Sep',
                                                       'Oct', 'Nov', 'Dec']))
        self.assertFalse(custom_equality(self.notes, self.notes[::-1]))
        self.assertFalse(custom_equality(self.multiples, [0, 3, 6, 9, 12, 15, 18,
                                                         21, 24]))
"""
if __name__ == '__main__':
    unittest.main()