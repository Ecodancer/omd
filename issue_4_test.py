from one_hot_encoder import fit_transform
import pytest


def test_colors():
    colors = ['Red', 'Red', 'Blue']
    expected = [('Red', [0, 1]),
                ('Red', [0, 1]),
                ('Blue', [1, 0])]
    assert fit_transform(colors) == expected


def test_size():
    size = ['small', 'medium', 'big']
    expected = [('small', [0, 0, 1]),
                ('medium', [0, 1, 0]),
                ('big', [1, 0, 0])]
    assert fit_transform(size) == expected


def test_features():
    features = ['BAD', 'GOOD']
    expected = [('BAD', [0, 1]),
                ('GOOD', [1, 0])]
    assert fit_transform(features) == expected


def test_exception():
    data = 123  # некорректные входные данные
    with pytest.raises(TypeError):
        fit_transform(data)
