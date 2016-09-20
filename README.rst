=======================
For Those About To Mock
=======================

Slides and code for a DC Python meetup presentation

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

Our sample code is in :file:`fileutils.py`.

We're doing the most simple test discovery possible to prevent
distracting from the mocks, so::

  python test_fileutils.py

Make the docs
=============

Run Sphinx to make the docs; we're using the `Hieroglyph`_ slide package::

  cd docs make && make slides

Then view them; with OS X::

  open build/slides/index.html

or just point your browser at the file.

.. _Hieroglyph: https://github.com/nyergler/hieroglyph
