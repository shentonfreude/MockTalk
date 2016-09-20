from unittest import TestCase, main
from unittest.mock import Mock, patch

from fileutils import rm

class TestFileutils(TestCase):
    @patch('fileutils.os')
    def test_with_mock(self, mock_os):
        rm('SOMEPATH')
        mock_os.remove.assert_called_with('SOMEPATH')
        self.assertTrue(mock_os.flugelhorn is not None)

if __name__ == '__main__':
    main()

