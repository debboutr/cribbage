========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |travis|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|


.. |travis| image:: https://api.travis-ci.com/debboutr/cribbage.svg?branch=main
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/debboutr/cribbage

.. |github-actions| image:: https://github.com/debboutr/cribbage/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/debboutr/cribbage/actions

.. |codecov| image:: https://codecov.io/gh/debboutr/cribbage/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/debboutr/cribbage

.. .. |version| image:: https://img.shields.io/pypi/v/cribbage-cmd.svg
..     :alt: PyPI Package latest release
..     :target: https://pypi.org/project/cribbage-cmd

.. .. |wheel| image:: https://img.shields.io/pypi/wheel/cribbage-cmd.svg
..     :alt: PyPI Wheel
..     :target: https://pypi.org/project/cribbage-cmd

.. .. |supported-versions| image:: https://img.shields.io/pypi/pyversions/cribbage-cmd.svg
..     :alt: Supported versions
..     :target: https://pypi.org/project/cribbage-cmd

.. .. |supported-implementations| image:: https://img.shields.io/pypi/implementation/cribbage-cmd.svg
..     :alt: Supported implementations
..     :target: https://pypi.org/project/cribbage-cmd

.. |commits-since| image:: https://img.shields.io/github/commits-since/debboutr/cribbage/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/debboutr/cribbage/compare/v0.0.0...main



.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: MIT license

Installation
============

::

    pip install cribbage-cmd

You can also install the in-development version with::

    pip install https://github.com/debboutr/cribbage/archive/main.zip


Documentation
=============


https://github.com/debboutr/cribbage


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
