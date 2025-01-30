from typing import List, Dict

import boto3

S3_CLIENT = boto3.client('s3')


def get_all_buckets() -> List[Dict]:
	"""get all S3 buckets in an account"""
	result = []
	response = S3_CLIENT.list_buckets()
	result.extend(response['Buckets'])
	while token := response.get('ContinuationToken'):
		response = S3_CLIENT.list_buckets(ContinuationToken=token)
		result.extend(response['Buckets'])
	return result
