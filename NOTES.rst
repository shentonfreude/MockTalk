=================
 Mock Talk Notes
=================


Common Patterns
===============

with ...
log invocation message

Pitfalls
========

Parameter defaults evaluated at definition, not runtime::

  def test_foo(self, something=Mock()):
      pass

