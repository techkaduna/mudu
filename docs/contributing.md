# Contributing

## Contributing to **mudu**

Thank you for considering contributing to this project, it is really appreciated. We welcome contributions in the following (but not limited to) areas:

- Bug fixes
- Code improvements and optimizations
- Documentation and tutorials
- Issue reporting and feature requests

## How To Contribute

1. Fork the project repository at [github.com/techkaduna/mudu](https://github.com/techkaduna/mudu)
2. Create a new branch for your code
3. Make changes
4. Write (or update) tests where necessary — every bug fix or behavior change should come with a regression test in `test/test_suite.py` (see the `TestPhase0Regressions` class for the expected style: one test per bug, named and documented with what it guards against)
5. If your change adds or registers a new unit, run `mudu.audit_units()` against the relevant conversion table(s) as part of your own testing
6. Commit your changes with an intuitive commit message
7. Open a pull request with a brief and concise explanation of your change(s)

## Coding guideline

- Follow PEP 8 style guidelines
- Use descriptive commit messages
- Write clear NumPy/SciPy-style docstrings
- When adding a new unit or conversion factor, cite the source of the numeric value in a comment (e.g. "NIST SP 811") wherever possible

## Testing

mudu uses `pytest` (with [Hypothesis](https://hypothesis.readthedocs.io/) for property-based tests) for testing. Run `pytest test/test_suite.py -v` locally and make sure all tests pass before submitting a pull request.

Once again, thanks for helping make mudu better.