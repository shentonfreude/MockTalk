===========
 Mock Talk
===========

Slides and code for a DC Python meetup presentation

Virtualenv, Install
===================

Create and activate virtualenv::

  virtualenv --python=python3 .venv3
  source .venv3/bin/activate

Install the requirements::

  pip install -r requirements

Run Tests
=========

We're using `py.test` to make our tests less boiler-plate-y. Run 'em::

  pytest

