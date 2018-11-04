import unittest


class CheckPoint(unittest.TestCase):
    # assertEqual(a, b)  判断a == b
    # assertNotEqual(a, b)  判断a！=b
    # assertIs(a, b)   a is b
    # assertIsNot(a, b)   a is not b
    # assertIsNone(x)   x is None
    # assertIsNotNone(x)   x is not None
    # assertIn(a, b)   a in b
    # assertNotIn(a, b)   a not in b
    # assertIsInstance(a, b)   isinstance(a, b)
    # assertNotIsInstance(a, b)   not isinstance(a, b)

    def __init__(self):
        super().__init__()
        self._flag = 0

    def equal(self, a, e, m):
        try:
            self.assertEqual(a, e)
        except:
            self._flag += 1
            print(m)

    def notEqual(self, a, e, m):
        try:
            self.assertNotEqual(a, e, m)
        except:
            self._flag += 1
            print(m)

    def isIs(self, a, e, m):
        try:
            self.assertIs(a, e, m)
        except:
            self._flag += 1
            print(m)

    def isNot(self, a, e, m):
        try:
            self.assertIsNot(a, e, m)
        except:
            self._flag += 1
            print(m)

    def isNone(self, a, e, m):
        try:
            self.assertIsNone(a, e, m)
        except:
            self._flag += 1
            print(m)

    def notNone(self, a, e, m):
        try:
            self.assertIsNotNone(a, e, m)
        except:
            self._flag += 1
            print(m)

    def isIn(self, a, e, m):
        try:
            self.assertIn(a, e, m)
        except:
            self._flag += 1
            print(m)

    def notIn(self, a, e, m):
        try:
            self.assertNotIn(a, e, m)
        except:
            self._flag += 1
            print(m)

    def isInstance(self, a, e, m):
        try:
            self.assertIsInstance(a, e, m)
        except:
            self._flag += 1
            print(m)

    def notInstance(self, a, e, m):
        try:
            self.assertNotIsInstance(a, e, m)
        except:
            self._flag += 1
            print(m)

    def less(self, a, e, m):
        try:
            self.assertLess(a, e, m)
        except:
            self._flag += 1
            print(m)

    def lessEqual(self, a, e, m):
        try:
            self.assertLessEqual(a, e, m)
        except:
            self._flag += 1
            print(m)

    def greater(self, a, e, m):
        try:
            self.assertGreater(a, e, m)
        except:
            self._flag += 1
            print(m)

    def greaterEqual(self, a, e, m):
        try:
            self.assertGreaterEqual(a, e, m)
        except:
            self._flag += 1
            print(m)

    def result(self, message):
        if self._flag > 0:
            self.assertTrue(False)
        else:
            self.assertTrue(True, message)
            print(message)

    def false(self, message):
        try:
            self.assertTrue(False, message)
        except:
            self._flag += 1
            print(message)