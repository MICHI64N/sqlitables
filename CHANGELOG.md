# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
* Column instances now have a constraints list that is applied to its definition.

### Changed
* Renamed column method "statement" to "definition" to better fit SQLite terminology.

### Fixed
* NULL can now be inserted into a table by typing "NULL" (case-insensitive) in a string.

## [0.1.1] - 2026-05-27

### Added
* Simple installation documentation in README.md.
* The addition of GitHub Actions files to last version's CHANGELOG.md entry.

### Changed
* Updated GitHub Actions versions to upload to PyPI without errors.

### Fixed
* Added quotes around the table name statements in the `classes.Table.select()` method.

## [0.1.0] - 2026-05-25

### Added
* The following features:
    * Connect to the database ([usage](https://github.com/MICHI64N/sqlitables/blob/main/docs/usage.md#connect-to-the-database)).
    * Create a table in the database ([usage](https://github.com/MICHI64N/sqlitables/blob/main/docs/usage.md#create-a-table-in-the-database)).
    * Insert values into a table ([usage](https://github.com/MICHI64N/sqlitables/blob/main/docs/usage.md#insert-values-into-a-table)).
    * Select values from a table ([usage](https://github.com/MICHI64N/sqlitables/blob/main/docs/usage.md#select-values-from-a-table)).
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

[Unreleased]: https://github.com/MICHI64N/sqlitables/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/MICHI64N/sqlitables/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/MICHI64N/sqlitables/releases/tag/v0.1.0