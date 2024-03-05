# -*- coding: utf-8 -*-

from .context import manage_foi

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_absolute_truth_and_meanin2(self):
        assert True


if __name__ == '__main__':
    unittest.main()