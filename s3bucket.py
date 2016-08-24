#!/usr/bin/env python

import boto3
from botocore.exceptions import ClientError


class S3Bucket:
    """Basic AWS S3 CRUD as fodder for Mock tests."""

    def __init__(self, bucket):
        """Attach the client, return a bucket, raise KeyError if none."""
        self.s3 = boto3.resource('s3')
        self.bucket_name = bucket

    def _get_object(self, key):
        """Return the S3 Object at the key.

        Object() won't raise anything, even with bogus bucket or key
        so we can't detect bad bucket or key here.
        """
        return self.s3.Object(bucket_name=self.bucket_name, key=key)

    # CRUD: create read update delete

    def create(self, key, content):
        """Write the content (str or readble); KeyError if key exists."""

    def read(self, key):
        """Return contents at key; KeyError if nonexistent."""
        obj = self._get_object(key)
        try:
            resp = obj.get(key)
        except ClientError as e:
            raise KeyError('read: bucket={} key={} : {}'.format(
                self.bucket_name, key, e))
        return resp['Body'].read()

    def update(self, key, contents):
        """Replace contents (str or readable); KeyError if nonexistent."""

    def delete(self, key):
        """Delete the object at key, raises KeyError if nonexistent."""

if __name__ == '__main__':
    b = S3Bucket('NOBUCKET')
    res = b.read('NOKEY')
    b = S3Bucket('avail-public.dev.nasawestprime.com')
    res = b.read('video/022315_Crawler 25th Anniversary_h.264/collection.json')
    print(res)
