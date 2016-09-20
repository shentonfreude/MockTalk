
.. For Those About To Mock slides file, created by
   hieroglyph-quickstart on Mon Sep 19 23:00:00 2016.

.. In hiero, theme='slides' makes 2nd level text fall off bottom;
   theme='single-level' works fine.

.. Even without lineno, we can only fit 70 cols of code

=========================================
 For Those About To Mock (We Salute You)
=========================================

Chris Shenton

@shentonfreude

chris@v-studios.com

https://github.com/shentonfreude/Presentation-For_Those_About_To_Mock

Unit Tests
==========

Unit tests test portions of your code in isolation. These should
test your code, not any third-party code (e.g., libraries, system
calls)

Unit Test: single test of multiple features
-------------------------------------------

.. literalinclude:: ../../unittest_twice_single.py

.. note::
 * Most folks have a setUp() and tearDown() to keep tests isolated.

Unit Test: separate tests of multiple features
----------------------------------------------

.. literalinclude:: ../../unittest_twice_multiple.py

.. note::
 * I prefer the isolation these individual tests provide, combined
   with setUp() and tearDown()

Mocking out 3rd party calls
===========================

Sometimes code calls libraries or services or makes changes that you
don't want to invoke in your tests, e.g.:

* database
* file storage
* cloud APIs

You can substitute these calls with "mocks" so you can test your code
without invoking the 3rd party code.

unittest.mock
=============

We used to write our own fake implementations for every service, but
Michael Foord's "mock" library provides a generic framework with tons
of features. Mocks can

* return anything, even an iterable
* raise an exception
* tally calls and collect call arguments
* implement magic methods
* replicate a real class with mocked attributes

unittest.mock is built into Python-3.3, else "pip install" it

Mock considered helpful
-----------------------

Benefits:

* Don't save to actual production storage -- databases, search engines, etc.
* Don't connect to production services (authorization, cloud infrastructure)
* Run Continuous Intgration tests that can't reach 3rd party services


Mock considered harmful?
------------------------

Be careful: on a basic mock, you can ask for any attribute or method
on a mock and it will exist, even if not supported by your actual call::

  >>> skynet = MagicMock()
  >>> if skynet.is_self_aware():
  ...   print('OMG, we are all gonna die')
  ...
  OMG, we are all gonna die

Basing the mock on an object will help::

  >>> skynet = MagicMock(spec=list)
  >>> skynet.is_self_aware()
  AttributeError: Mock object has no attribute 'is_self_aware'

Mocks: Decorators, Basic, Exceptions, Returns, Magic
====================================================

Next we show Mocks in various shapes:

* Basic mock, using a decorator
* Raising an exception when called, to invoke our handler
* Providing a return value to the caller
* MagicMocks with getter/setters
* Returnin a different object when called each time, including an exception
* Basing a Mock on an existing object to avoid false positives

Basic Mock
----------

Mock out the *module's* version of `os`. Note we can access any
attribute on the mock, even it it does not exist!

.. literalinclude:: ../../fileutils.py
   :lines: 1-5

.. literalinclude:: ../../test_fileutils.py
   :start-after: TEST_RM
   :end-before: TEST_RMTRY
   :emphasize-lines: 1-2,5

.. note::
   * Mock the item where it's used, not where it came from


Basic Mock with Exception Side Effect
-------------------------------------

Test exception handling by setting a side effect; we can check
exception message to ensure we've got the correct handler. We use
`with` context so we can easily use `pdb`.

.. literalinclude:: ../../fileutils.py
   :lines: 7-12

.. literalinclude:: ../../test_fileutils.py
   :start-after: TEST_RMTRY
   :end-before: TEST_RMTRY_MULTI_DECORATORS
   :emphasize-lines: 4-6

.. note::
   * There are other ways to set a mock including `patch` context
     manager and adding a mock to a class instance under test.

Basic Mock: Decorator order is "inside-out"
-------------------------------------------

List stacked decorators inside-out.

.. literalinclude:: ../../fileutils.py
   :lines: 7-12

.. literalinclude:: ../../test_fileutils.py
   :start-after: TEST_RMTRY_MULTI_DECORATORS
   :end-before: TEST_OS_GETGROUPS
   :emphasize-lines: 1-3

.. note::
   * We can also look at the logging message to make sure we're
     triggering the correct code.

MagicMock
---------

TFM says: "In most of these examples the Mock and MagicMock classes are
interchangeable. As the MagicMock is the more capable class it makes a
sensible one to use by default."

>>> my_dict = {'a': 1, 'b': 2, 'c': 3}
>>> def getitem(name):
...      return my_dict[name]
...
>>> def setitem(name, val):
...     my_dict[name] = val
...
>>> mock = MagicMock()
>>> mock.__getitem__.side_effect = getitem
>>> mock.__setitem__.side_effect = setitem

We'll use MagicMocks in the subsequent examples. To be honest, I
haven't leveraged these yet.

Return Value
------------

The Mock can return a value, with any structure we like.

.. literalinclude:: ../../fileutils.py
   :lines: 14-15

.. literalinclude:: ../../test_fileutils.py
   :start-after: TEST_OS_GETGROUPS
   :end-before: TEST_RMTRY_MULTI_RETURNS
   :emphasize-lines: 4-5



Different Returns, Exception as Side Effect
-------------------------------------------

Return different things including causing an exception; each
time our Mock is called, the next item in the iterator is returned.

.. literalinclude:: ../../test_fileutils.py
   :start-after: TEST_RMTRY_MULTI_RETURNS
   :end-before: TESTFILER
   :emphasize-lines: 4-5, 8-9


Mock Based on Existing Object
-----------------------------

You can create a Mock based on the `spec` (call signature) of an
existing object, so that if the object changes, tests referring to
no-long-extant attributes will fail as they should.

.. literalinclude:: ../../fileutils.py
   :lines: 18-22

.. literalinclude:: ../../test_fileutils.py
   :start-after: TESTFILER
   :end-before: MAIN
   :emphasize-lines: 6-9



Common Patterns We've Fallen Into
=================================

* creating webapp sessions with authenticated fake user objects
* checking log/exception message content to ensure we're triggering the desired code
* `with` exception handling to allow `pdb` into the function under test
* check mock_thing.assert_called_with(...)

That's a gotcha question
========================

Parameter defaults evaluated at definition, not runtime::

  def test_foo(self, something=Mock()):
      # some setup and tests...

Here `something` will get set to a specific value, and changes to it
will be seen by every other user of that object, even in separate
tests. Instead do::

  def test_foo(self, something=None):
      if something is None::
          something = Mock()
      # some setup and tests...


References 1
============

* Python 3 unittest.mock
  `<https://docs.python.org/3/library/unittest.mock-examples.html>`_

* Mock 1.0.1 documentation (Foord's older docs, some good narrative)
  `<http://www.voidspace.org.uk/python/mock/#>`_

* Foord's intro to unit testing includes mocks
  `<http://www.voidspace.org.uk/python/articles/introduction-to-unittest.shtml#duck-typing-and-mock-objects>`_

* An Introduction to Mocking in Python (solid tutorial)
  `<https://www.toptal.com/python/an-introduction-to-mocking-in-python>`_

References 2
============

* Python 201: An Intro to Mock (short and sweet)
  `<https://dzone.com/articles/python-201-an-intro-to-mock>`_

* Python Unit Testing with Mock (quick example of mocking Twitter)
  `<http://www.insomnihack.com/?p=194>`_

* Mocking External APIs in Python (from 2016, very deep, good stuff)
  `<https://realpython.com/blog/python/testing-third-party-apis-with-mocks/>`_

