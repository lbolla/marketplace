# Marketplace

Inside a virtualenv, install dependencies and app with:

    $> make develop

Run app with:

    $> make run

It uses SQLite in-memory database, pre-populated with test data.

## Dependencies

Deps are managed via `pip-tools`. Bump them with:

    $> make deps
