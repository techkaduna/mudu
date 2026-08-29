# Security Policy

## Scope

`mudu` is a unit-conversion and dimensional-analysis library. Its attack
surface is small; it does not execute untrusted input as code, make
network calls, read/write files, or deserialize external data — but a
scientific library used in downstream engineering/research pipelines is
still expected to have a disclosed reporting process, and correctness
defects (a wrong conversion factor, a dimension check that fails to
trigger) can have real-world consequences for anyone relying on mudu's
output, even without being a "security vulnerability" in the traditional
sense.

This policy covers both:
- **Traditional security issues** — e.g. a code path that could be
  induced to execute arbitrary code, an unbounded resource-consumption
  issue from crafted input, a supply-chain concern with a dependency.
  
- **Silent-correctness defects** — a conversion, dimension check, or
  arithmetic operation that produces a numerically wrong result without
  raising an error. Given what this library is used for, we treat these
  with the same urgency as a conventional security report.

## Supported Versions

| Version | Supported |
|---------|-----------|
| 2.0.x   | ✅ |
| 1.x     | ❌ (pre-D-Check; upgrade recommended) |

## Reporting a Vulnerability or Silent-Correctness Defect

**Please do not open a public GitHub issue for a correctness defect or
security concern until it has been triaged privately** — a public issue
describing an unpatched silent-wrong-answer bug could cause harm to
anyone using the affected version before a fix ships.

To report:

1. Open a private report via GitHub's
   [Security Advisories](https://github.com/techkaduna/mudu/security/advisories/new)
   feature for this repository, **or**
2. If that's unavailable to you, email the maintainer directly (see the
   contact listed on the [PyPI project page](https://pypi.org/project/mudu/)).

Please include:
- The version of `mudu` affected
- A minimal reproducing example
- What you expected vs. what you observed
- For correctness defects: if possible, an independent reference value
  (e.g. from NIST, `pint`, or `astropy.units`) showing the discrepancy

## What to Expect

- **Acknowledgment** within 5 business days.
- **Triage and severity assessment** within 10 business days — silent-
  correctness defects affecting a shipped conversion factor or
  dimension-safety check are treated as high severity by default.
- **Disclosure**: once a fix is released, we will publish a GitHub
  Security Advisory and a corresponding `CHANGELOG.md` entry. We follow
  coordinated disclosure — we ask reporters not to publicly disclose
  before a fix is available, and we commit to not sitting on a
  confirmed report indefinitely.

## Recognition

Reporters of confirmed issues are credited in the relevant `CHANGELOG.md`
entry and GitHub Security Advisory, unless they request otherwise.

## AI Usage Disclosure

AI assistance (Anthropic's Claude) was used during the 2.0.0 "D-Check" release. All AI-proposed changes were reviewed, refined, and approved by the maintainer before acceptance; nothing below was accepted on the AI's self-report alone.

**Code review** — Identified several silent, pre-existing defects in the pre-2.0.0 source via line-by-line review, cross-checked against standard reference values (NIST-style constants): a dimension-symbol collision merging three distinct dimensions, a copy-pasted dimension formula, a unit-name collision silently skipping a needed conversion, a mass-conversion factor off by 1000x, and an inverted length-unit conversion.

**Roadmap** — Drafted the phased "D-Check" roadmap (bug fixes, architecture, testing, CI, docs, governance) under the maintainer's direction and scope corrections.

**Source code** — Rewrote the affected modules to fix the defects above and introduce a new public extension API (`define_unit`, `register_conversion`, `audit_units`, `Linear`/`Affine`), replacing the prior private-internals-only extension path. Sandbox-tested by the AI, then independently re-verified by the maintainer in their own environment. The maintainer's own run is what confirms the fixes hold.

**Documentation** — Drafted `CHANGELOG.md`, updated examples and `.rst`/Markdown docs for the fixed API, and converted the documentation site from Sphinx to MkDocs.

**CI/tooling** — Authored `pyproject.toml` additions, a GitHub Actions workflow, pre-commit config, and this file, reconciled against the maintainer's existing setup.

**Not AI-generated or AI-validated** — The original package concept, domain purpose, and pre-existing functionality are the maintainer's own, predating this release. All correctness claims rest on the maintainer's independent review and re-execution, not on AI self-report.

*This AI Usage Disclosure is published as part of an ongoing effort toward transparency in AI-aided development of the Mudu project.*