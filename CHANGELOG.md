# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.0.1] - 2024-05-02

### Added

- CHANGELOG.md file.
- Cache cachalot, with backend RedisCache.
- Forms for user.
- Pre-commit and settings linters for clean code.
- makefile and commands.
- drf base token auth.
- docker and docker compose (django, redis, celery, flower).
- Events app create.
- Event model, serializer, views, urls.
- Organize permission object.
- Events (CRUD).
- Send email when user register on event.
- Test coverage
- Test models for users and events
- Test views for events
- Pagination, filter and search for event list

### Changed

- admin.py, add functions for admin panel.
- add app_name for all urls.py

### Fixed

- djoser settings.
- many minor fix
