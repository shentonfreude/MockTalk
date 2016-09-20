=======================
For Those About To Mock
=======================

Slides and code for a DC Python meetup presentation on Mocks.

As the Firesign Theater said,

  A power so great it can only be used for good or evil.

Virtualenv, Install
===================

Create and activate virtualenv::

  virtualenv --python=python3 .venv3
  source .venv3/bin/activate

Install the requirements::

  pip install -r requirements.txt

If you're using Python < 3.3 you'll need to install mock.

Run Tests
=========

Our sample code is in ``fileutils.py``.

We're doing the most simple test discovery possible to prevent
distracting from the mocks, so::

  python test_fileutils.py

Make the docs
=============

Run Sphinx to make the docs. We are using the `Hieroglyph`_ to
generate HTML slides::

  cd docs make
  make slides

Then view them with OS X::

  open build/slides/index.html

or just point your browser at the file.

You can read the docs as a single flat doc by walking down to ``docs/source/index.rst``.

.. _Hieroglyph: https://github.com/nyergler/hieroglyph
