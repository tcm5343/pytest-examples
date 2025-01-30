from importlib import reload
from unittest.mock import patch

from botocore.exceptions import NoCredentialsError
import boto3
import pytest

from s3 import get_all_buckets
import s3 as s3_module


@pytest.fixture()
def mock_boto3_client():
	with patch.object(boto3, 'client') as mock:
		reload(s3_module)
		yield mock
	reload(s3_module)  # revert module to avoid test contamination


def test_get_all_objects_when_uses_token(mock_boto3_client):
	bucket1 = {'Name': 'some-bucket-name'}
	bucket2 = {'Name': 'some-other-bucket-name'}
	expected = [bucket1, bucket2]
	mock_boto3_client.return_value.list_buckets.side_effect = [
		{'Buckets': [bucket1], 'ContinuationToken': 'some-token'},
		{'Buckets': [bucket2]},
	]
	actual = get_all_buckets()

	assert actual == expected
	assert isinstance(actual, list)
	assert mock_boto3_client.return_value.list_buckets.call_count == 2
	mock_boto3_client.return_value.list_buckets.assert_called_with(ContinuationToken='some-token')


def test_get_all_objects_when_no_buckets(mock_boto3_client):
	mock_boto3_client.return_value.list_buckets.return_value = {'Buckets': []}
	assert get_all_buckets() == []
	mock_boto3_client.return_value.list_buckets.assert_called_once()


def test_get_all_objects_raises_when_not_mocked():
	"""if mock_boto3_client didn't reload on tear down, this test would fail"""
	with pytest.raises(NoCredentialsError):
		get_all_buckets()
