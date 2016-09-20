from unittest import TestCase, main
from unittest.mock import Mock, patch
from fileutils import rm, rmtry

class TestFileutils(TestCase):

    @patch('fileutils.os')
    def test_rm(self, mock_os):
        rm('SOMEPATH')
        mock_os.remove.assert_called_with('SOMEPATH')
        self.assertTrue(mock_os.flugelhorn is not None)

    @patch('fileutils.os')
    def test_rmtry(self, mock_os):
        mock_os.remove.side_effect = FileNotFoundError('nope')
        with self.assertRaises(RuntimeError) as e:
            rmtry('SOMEPATH')
        self.assertEqual(e.exception.__str__(), 'nope')

    @patch('fileutils.logging')
    @patch('fileutils.os')
    def test_rmtry_multi_decorators(self, mock_os, mock_logging):
        mock_os.remove.side_effect = FileNotFoundError('nope')
        with self.assertRaises(RuntimeError) as e:
            rmtry('SOMEPATH')
        self.assertEqual(e.exception.__str__(), 'nope')
        mock_logging.error.assert_called()
        self.assertIn('FileNotFoundError',
                      mock_logging.error.call_args.__str__())


if __name__ == '__main__':
    main()

