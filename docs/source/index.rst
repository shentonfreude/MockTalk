
.. For Those About To Mock slides file, created by
   hieroglyph-quickstart on Mon Sep 19 23:00:00 2016.

.. In hiero, theme='slides' makes 2nd level text fall off bottom;
   theme='single-level' works fine.

.. Even without lineno, we can only fit 70 cols of code

=========================================
 For Those About To Mock (We Salute You)
=========================================

Chris Shenton

chris@v-studios.com

@shentonfreude


Unit Tests
==========

Unit tests test portions of your code in isolation. These should
test your code, not any third-party code (e.g., libraries, system
calls)

Unit Test: single test
----------------------

.. literalinclude:: ../../unittest_twice_single.py

Unit Test: multiple tests
-------------------------

.. literalinclude:: ../../unittest_twice_multiple.py
   :emphasize-lines: 17-18


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
* raise an exceptoin
* tally calls and collect call arguments
* implement magic methods
* replicate a real class with mocked attributes

Mock considered harmful
=======================

Be careful: on a basic mock, you can ask for any attribute or method
on a mock and it will exist, even if not supported by your actual call.

Basic Mock
----------

Mock out the *module's* version of `os`. Note we can access any
attribute on the mock.

.. literalinclude:: ../../test_fileutils_basic.py
   :emphasize-lines: 7,10-11


MagicMock
---------

Mock with default-config
------------------------


Side effects: returns, exceptions, iterators
============================================


mock side_effect can return something new each time it's called, so it
could do one thing the first time, then something else the next.

Rm file first time works, second fails

References
==========

* An Introduction to Mocking in Python
  `<https://www.toptal.com/python/an-introduction-to-mocking-in-python>`_
