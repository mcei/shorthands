from ..shorthands. import eq_, ok_, not_, fail

from string import ascii_lowercase
# import unittest
# unittest.TestCase.assertIsInstance()

eq_(1, 1)
not_(False)
ok_(6 == 6)

if isinstance(ascii_lowercase, str):
    fail("ascii_lowercase is not str")
