from unittest import TestCase, main
from unittest.mock import Mock, patch, MagicMock

class TestFileutils(TestCase):

    # TEST_RM
    @patch('fileutils.os')
    def test_rm(self, mock_os):
        from fileutils import rm
        rm('SOMEPATH')
        mock_os.remove.assert_called_with('SOMEPATH')
        self.assertTrue(mock_os.flugelhorn is not None)

    # TEST_RMTRY
    @patch('fileutils.os')
    def test_rmtry(self, mock_os):
        from fileutils import rmtry
        mock_os.remove.side_effect = FileNotFoundError('nope')
        with self.assertRaises(RuntimeError) as e:
            rmtry('SOMEPATH')
        self.assertEqual(e.exception.__str__(), 'nope')

    # TEST_RMTRY_MULTI_DECORATORS
    @patch('fileutils.logging')
    @patch('fileutils.os')
    def test_rmtry_multi_decorators(self, mock_os, mock_logging):
        from fileutils import rmtry
        mock_os.remove.side_effect = FileNotFoundError('nope')
        with self.assertRaises(RuntimeError) as e:
            rmtry('SOMEPATH')
        self.assertEqual(e.exception.__str__(), 'nope')
        mock_logging.error.assert_called()
        self.assertIn('FileNotFoundError',
                      mock_logging.error.call_args.__str__())

    # TEST_OS_GETGROUPS
    @patch('fileutils.os')
    def test_os_getgroups(self, mock_os):
        from fileutils import groups
        mock_os.getgroups = MagicMock(return_value=[42, 666])
        self.assertEqual(groups(), [42, 666])

    # TEST_RMTRY_MULTI_RETURNS
    @patch('fileutils.os')
    def test_rmtry_multi_returns(self, mock_os):
        from fileutils import rmtry
        mock_os.remove = MagicMock(side_effect=(
            42,
            FileNotFoundError('nope'),
        ))
        got = rmtry('1stPathOK')
        self.assertEqual(got, None)  # Nothing returned by our func
        with self.assertRaises(RuntimeError) as e:
            rmtry('2ndPathMissing')
        self.assertEqual(e.exception.__str__(), 'nope')

# TESTFILER
class TestFiler(TestCase):
    @patch('fileutils.os')
    def test_rm(self, mock_os):
        from fileutils import Filer
        mock_filer = MagicMock(spec=Filer)
        self.assertTrue(hasattr(mock_filer, 'rm'))
        with self.assertRaises(AttributeError):
            mock_filer.create_method_we_removed('WMD')

# MAIN
if __name__ == '__main__':
    main()
