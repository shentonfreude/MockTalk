#!/usr/bin/env python

import boto3
from botocore.exceptions import ClientError


class S3Bucket:
    """Basic AWS S3 CRUD as fodder for Mock tests."""

    def __init__(self, bucket):
        """Attach the client, return a bucket, raise KeyError if none."""
        self.s3 = boto3.resource('s3')
        self.bucket_name = bucket

    def read(self, key):
        """Return filehandle to key, or KeyError if nonexistent."""

        # Object() won't raise anything, even with bogus bucket or key
        obj = self.s3.Object(bucket_name=self.bucket_name, key=key)
        try:
            resp = obj.get()
        except ClientError as e:
            raise KeyError('read: bucket={} key={} : {}'.format(
                self.bucket_name, key, e))
        body_fp = resp['Body']
        return body_fp

if __name__ == '__main__':
    b = S3Bucket('BOGUS')
    fp = b.read('BADKEY')
