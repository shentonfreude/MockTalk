=================
 Mock Talk Notes
=================

TODO: how to break into slides?

Why Mock?
=========

Don't save to actual production storage -- databases, search engines, etc.

Don't connect to production services (authorization, cloud infrastructure)

Run Continuous Intgration tests that only exercises your code, not 3rd party.

Common Patterns
===============

with ...
log invocation message

Pitfalls
========

Parameter defaults evaluated at definition, not runtime::

  def test_foo(self, something=Mock()):
      pass

INTRO TEXT
==========

because of the wonders of duck typing we can substitute any object at
runtime for another object that supports the same operations. This
means we can swap out production classes with mock objects that record
how they are used.

Built into 3.3, else pip install

But shouldn't method implementation be transparent?
---------------------------------------------------

Well, yes, but...

Mock, MagicMock, autospec
=========================

I've always used plain `Mock` due to some problems we've had early-on
using auto_spec, but most docs recommend using auto_spec.

Mock: accepts any calls with any arguments, and access to any attributes.

MagicMock: as above, but also allows mocking the object's magic
methods, e.g.: __str__ [can it mock attribute access so we can get
s3.bucket() auto_spec: implements mocks on implementation details of
the mocked object, so if the object changes, your mock will to -- this
can reveal tests that will break when your code changes, a good thing.


Why would you want to mock
==========================

Backend unavailable, slow, or persistent/destructive

* Remote APIs: services, authentication, etc
* Expensive calculations
* System calls: file access, create/delete (avoid using test /tmp files), sockets
* Disk, database, cloud storage

Mock evaluation
---------------

* assert_called_with(...)


Applying Mocks
--------------

@patch
with ...
mock.create_autospec(...)


Mock module context
-------------------

Mock where it is used, not where it came from; e.g., if your_module.py has::

  import boto3
  s3 = boto3.resource('s3')

then you'd mock in the scope of your function::

  from mock import patch
  @patch('your_module.boto3.resource')
  def test_s3_something(self, mock_resource):
      pass

Mock stacking order
-------------------

You can mock multiple modules, but order is inside-to-outside; in
your_module.py::

  import boto3
  from boto3 import client
  s3_resource = boto3.resource('s3')
  s3_client = client('s3')

In test_module.py::

   from mock import patch
   @patch('your_module.client')
   @patch('your_module.boto3')
   def test_s3_something(self, mock_boto3, mock_client):
       pass

Mock behaviors
--------------

* return_value
* side_effect: exception, return values (e.g. iterator)
* assert_called_with

Patterns We've Found Useful
===========================

Context manager for expected exceptions allows pdb

Mock logs and check message body: could be multiple log messages based
on logic flow so test the content of the emitted logs.



References
==========

Mock - Mocking and Testing Library (1.0.1)
http://www.voidspace.org.uk/python/mock/

Getting Started with Mock (1.0.1)
http://www.voidspace.org.uk/python/mock/getting-started.html

Mocking External APIs in Python
https://realpython.com/blog/python/testing-third-party-apis-with-mocks/

Python 201: An Intro to Mock
https://dzone.com/articles/python-201-an-intro-to-mock

An Introduction to Mocking in Python
https://www.toptal.com/python/an-introduction-to-mocking-in-python

Unit-Testing With unittest.mock.patch()
https://blog.petrzemek.net/2014/06/21/unit-testing-with-unittest-mock-patch/

An Introduction to Mocking in Python
https://www.toptal.com/python/an-introduction-to-mocking-in-python
