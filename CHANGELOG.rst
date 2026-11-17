Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.1.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

`Unreleased`_
-------------
.. note::
    Many previous features have been removed to refactor the code.
    However, the removals are temporary and will not persist to release.

Changed
^^^^^^^
* Renamed column method "statement" to property "definition" to better fit SQLite terminology.
* The docs/ folder now contains a Sphinx website.
* README and CHANGELOG now use reStructuredText to go along with the Sphinx website.
* Renamed "classes.py" to "table.py" since there are going to be more classes.

Removed
^^^^^^^
* There is no longer a list of features on the README.

`0.1.1`_ - 2026-05-27
---------------------

Added
^^^^^
* Simple installation documentation in README.md.
* The addition of GitHub Actions files to last version's CHANGELOG.md entry.

Changed
^^^^^^^
* Updated GitHub Actions versions to upload to PyPI without errors.

Fixed
^^^^^
* Added quotes around the table name statements in the `classes.Table.select() <https://github.com/MICHI64N/sqlitables/blob/v0.1.1/docs/reference.md#selectself-select-where-cursor>`_ method.

`0.1.0`_ - 2026-05-25
---------------------

Added
^^^^^
* The following features:
    * Connect to the database (`usage <https://github.com/MICHI64N/sqlitables/blob/v0.1.0/docs/usage.md#connect-to-the-database>`_).
    * Create a table in the database (`usage <https://github.com/MICHI64N/sqlitables/blob/v0.1.0/docs/usage.md#create-a-table-in-the-database>`_).
    * Insert values into a table (`usage <https://github.com/MICHI64N/sqlitables/blob/v0.1.0/docs/usage.md#insert-values-into-a-table>`_).
    * Select values from a table (`usage <https://github.com/MICHI64N/sqlitables/blob/v0.1.0/docs/usage.md#select-values-from-a-table>`_).
* Package files @ src/sqlitables/  
    * \_\_init\_\_.py
    * classes.py
    * connection.py
* Documentation @ docs/
    * reference.md
    * usage.md
* pyproject.toml
* Repository files
    * README.md
    * CHANGELOG.md
    * LICENSE
    * .gitignore
* GitHub Actions files @ .github/workflows/
    * pypi-build.yml
    * pypi-publish.yml
    * pypi-test.yml

.. _Unreleased: https://github.com/MICHI64N/sqlitables/compare/v0.1.1...HEAD
.. _0.1.1: https://github.com/MICHI64N/sqlitables/compare/v0.1.0...v0.1.1
.. _0.1.0: https://github.com/MICHI64N/sqlitables/releases/tag/v0.1.0