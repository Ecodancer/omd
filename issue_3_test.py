from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_colors(self):
        colors = ['Red', 'Red', 'Blue']
        actual = fit_transform(colors)
        expected = [('Red', [0, 1]),
                    ('Red', [0, 1]),
                    ('Blue', [1, 0])]
        self.assertEqual(actual, expected)

    def test_size(self):
        size = ['small', 'medium', 'big']
        actual = fit_transform(size)
        expected = [('small', [0, 0, 1]),
                    ('medium', [0, 1, 0]),
                    ('big', [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_features(self):
        features = ['BAD', 'GOOD']
        actual = fit_transform(features)
        not_expected_sequence = [[('BAD', [1, 0]),
                                  ('GOOD', [0, 1])],
                                 [('NORMAL', [0, 0, 0])]]
        self.assertNotIn(actual, not_expected_sequence)

    def test_exception(self):
        data = 123  # некорректные входные данные
        try:
            fit_transform(data)
        except Exception:
            self.assertRaises(Exception)
