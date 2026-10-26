# Maintainer notes

- Keep `SKILL.md` as the single discoverable root. References and examples support it; they are not extra skill registrations.
- Keep the package Markdown-only unless an implementation solves a demonstrated mechanical gap.
- Describe observable outcomes, meaningful limits and honest failure states. Do not turn ordinary authoring choices into a fixed checklist.
- Run `python -B -m unittest discover -s tests -v` from this directory after editing.
- Read every changed file before release. Keep private overlays, real account settings, histories and machine paths outside the tracked tree.
- Preserve source attribution and distinguish original writing from third-party material. Do not copy an upstream translation into this package without an applicable redistribution grant.
- Change verification notes only when supported by checks actually run. Do not claim live agent discovery or downstream task success from structural tests.
