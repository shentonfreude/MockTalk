.. revealjs:: Unit Tests

 Unit tests test test portions of your code in isolation. These should
 test your code, not any third-party code (e.g., libraries, system
 calls)

.. revealjs:: create

 We should be able to include a python file
 and select with :pyobject: or :lines:

 .. literalinclude:: ../../s3bucket.py
    :linenos:
    :language: python
    :lines: 34-44
    :emphasize-lines: 40

.. revealjs:: Mocking out 3rd party calls

   Sometimes code calls libraries or services or makes changes (e.g.,
   database, file storage, cloud calls) that you don't want to.  You can
   substitute these calls with "mocks" so you can test your code without
   invoking the 3rd party code.

.. revealjs:: unittest.mock

   We used to write our own fake implementations for every service, but
   Michael Foord's "mock" library provides a generic framework with tons
   of features.

   * you can make the mock return anything, or raise an exceptoin
   * you can count invocations and collect call arguments

.. revealjs:: Mock considered harmful

   Why not mock? be careful: you can ask for any attribute or method on a
   mock and it will exist, even if not supported by your actual call --
   use default-spec.

    .. revealjs:: Second Level

       something here

    .. revealjs:: Second Level 2

       more second level stuff

         .. revealjs:: Third Level 1

            Third floor

         .. revealjs:: Third 2

            Third floor some more


.. revealjs:: Side effects: returns, exceptions, iterators

   mock side_effect can return something new each time it's called, so it
   could do one thing the first time, then something else the next.



