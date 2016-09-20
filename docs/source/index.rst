==============
 For Those About To Mock (We Salute You)
==============

Unit Tests
==========

Unit tests test test portions of your code in isolation. These should
test your code, not any third-party code (e.g., libraries, system
calls)

Code: create
============

We should be able to include a python file
and select with :pyobject: or :lines:

.. rv_small::

.. literalinclude:: ../../s3bucket.py
   :linenos:
   :language: python
   :lines: 34-44
   :emphasize-lines: 40

