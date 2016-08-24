import pytest
from unittest.mock import Mock

from s3bucket import S3Bucket


def test_init():
    b = S3Bucket('b')
    assert b.bucket_name == 'b'


def test__get_object():
    b = S3Bucket('b')
    b.s3 = Mock()
    mock_object = Mock()  # Why do I need this new var? GOTHCHA section
    b.s3.Object = mock_object
    o = b._get_object('k')
    assert isinstance(o, Mock)
    b.s3.Object.assert_called_with(bucket_name='b', key='k')

# If boto can't get find AWS (e.g., AWS_PROFILE not set, working)
# it raises NoCredentialsError; you should mock real AWS calls anyway!


def test_read_found_key():
    b = S3Bucket('b')
    from io import BytesIO
    mock_get = Mock(return_value={'Body': BytesIO(b'foo')})
    b._get_object = Mock()
    b._get_object().get = mock_get
    res = b.read('k')
    assert res == b'foo'
    assert b._get_object.called_with('k')
    assert mock_get.called_with('k')


def test_read_no_such_key():
    b = S3Bucket('b')
    b._get_object = Mock(side_effect=KeyError('nope'))
    with pytest.raises(KeyError) as e:
        b.read('k')
    assert 'nope' in str(e)

# def mock_search(self):
#     class MockSearchQuerySet(SearchQuerySet):
#         def __iter__(self):
#             return iter(["foo", "bar", "baz"])
#     return MockSearchQuerySet()
#
# # SearchForm here refers to the imported class reference in myapp,
# # not where the SearchForm class itself is imported from
# @mock.patch('myapp.SearchForm.search', mock_search)
# def test_new_watchlist_activities(self):
#     # get_search_results runs a search and iterates over the result
#     self.assertEqual(len(myapp.get_search_results(q="fish")), 3)
