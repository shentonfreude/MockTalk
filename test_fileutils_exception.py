from unittest import TestCase, main
from unittest.mock import Mock, patch
from fileutils import rmtry

class TestFileutils(TestCase):
    @patch('fileutils.os')
    def test_with_mock(self, mock_os):
        mock_os.remove.side_effect = FileNotFoundError('nope')
        with self.assertRaises(RuntimeError) as e:
            rmtry('SOMEPATH')
        self.assertEqual(e.exception.__str__(), 'nope')

if __name__ == '__main__':
    main()

