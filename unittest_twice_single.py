from unittest import TestCase, main

def twice(x):
    return x + x

class TestTwice(TestCase):

    def test_twice(self):
        got = twice(42)
        self.assertEqual(got, 84)
        got = twice('a')
        self.assertEqual(got, 'aa')
        with self.assertRaises(TypeError):
            twice(None)

if __name__ == '__main__':
    main()
