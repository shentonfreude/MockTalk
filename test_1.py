import pytest
from unittest.mock import Mock


def test_init():
    from main import S3Bucket
    b = S3Bucket('a')
    assert b.bucket_name == 'a'

# If boto can't get find AWS (e.g., AWS_PROFILE not set, working)
# it raises NoCredentialsError; you should mock real AWS calls anyway!


def test_read_found_key():
    from main import S3Bucket
    b = S3Bucket('b')
    from io import BytesIO
    b._get_object = Mock()
    b._get_object().get = Mock(return_value={'Body': BytesIO(b'foo')})
    res = b.read('k')
    assert res == b'foo'


def test_read_no_such_key():
    from main import S3Bucket
    b = S3Bucket('b')
    b._get_object = Mock(side_effect=KeyError('nope'))
    with pytest.raises(KeyError) as e:
        b.read('k')
    assert 'nope' in str(e)
