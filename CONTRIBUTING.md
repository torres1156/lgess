# Contributing

Thank you for your interest in improving LG ESS Local.

## Reporting Issues

Please include:

- Home Assistant version
- LG ESS firmware version
- Integration version
- Error logs
- Steps to reproduce the issue

## Pull Requests

Please ensure that:

- Code follows Home Assistant development guidelines.
- New functionality includes tests whenever possible.
- Existing functionality is not broken.
- Documentation is updated if required.

## Development

Repository layout:

```
custom_components/
└── lgess/
```

Tests:

```
tests/
```

Run before committing:

```bash
python -m pytest
```

## Coding Style

- Follow PEP 8.
- Use type hints.
- Keep functions focused.
- Prefer dataclasses where appropriate.
- Avoid unnecessary dependencies.

## Versioning

This project follows Semantic Versioning.

Example:

- 0.2.0 → new functionality
- 0.2.1 → bug fixes
- 0.3.0 → larger feature additions

## License

By contributing, you agree that your contributions are released under the MIT License.
