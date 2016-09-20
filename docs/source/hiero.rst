
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

.. with 'slides' the Second-level header is pushed down, so text falls off bottom
   but it's ok with single-level

Unit Tests
==========

Unit tests test portions of your code in isolation. These should
test your code, not any third-party code (e.g., libraries, system
calls)



create
======

.. literalinclude:: ../../s3bucket.py
   :lines: 36-44

Mocking out 3rd party calls
===========================

Sometimes code calls libraries or services or makes changes (e.g.,
database, file storage, cloud calls) that you don't want to.  You can
substitute these calls with "mocks" so you can test your code without
invoking the 3rd party code.

unittest.mock
=============

We used to write our own fake implementations for every service, but
Michael Foord's "mock" library provides a generic framework with tons
of features.

* you can make the mock return anything, or raise an exceptoin
* you can count invocations and collect call arguments

Mock considered harmful
=======================

Why not mock? be careful: you can ask for any attribute or method on a
mock and it will exist, even if not supported by your actual call --
use default-spec.

Second Level
------------

something here

.. literalinclude:: ../../s3bucket.py
   :lines: 36-44


Second Level 2
--------------

more second level stuff WHY IS THIS NOT SEEN?

Third Level 1
~~~~~~~~~~~~~

Third floor, same rendering as 2nd

.. literalinclude:: ../../s3bucket.py
   :lines: 36-44


Third 2
~~~~~~~

Third floor some more


Side effects: returns, exceptions, iterators
============================================


mock side_effect can return something new each time it's called, so it
could do one thing the first time, then something else the next.



