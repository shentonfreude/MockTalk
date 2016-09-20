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

Our sample code is in `fileutils.py`.

We're doing the most simple test discovery possible to prevent
distracting from the mocks, so::

  python test_fileutils.py

Make the docs::

  cd docs make && make slides
  open build/slides/index.html

If you don't have OSX `open` just point your browser at the file.
