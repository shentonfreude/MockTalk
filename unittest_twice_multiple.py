from unittest import TestCase, main

def twice(x):
    return x + x

class TestTwice(TestCase):

    def test_number(self):
        got = twice(42)
        self.assertEqual(got, 84)

    def test_alpha(self):
        got = twice('a')
        self.assertEqual(got, 'aa')

    def test_bad_input(self):
        with self.assertRaises(TypeError):
            twice(None)

if __name__ == '__main__':
    main()
