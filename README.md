# Skillify

Turn a repeatable task into a reusable skill for a coding agent. Skillify helps you define what the skill should produce, its limits, how an agent finds it and how to check the result.

It is a Markdown-only skill. It does not need an API key, package installation or a running service.

## Install

Start from your workspace's `AGENTS.md` and routing rules. Clone the complete package to an appropriate project directory, then expose its root once through your agent's existing skill discovery:

```sh
git clone https://github.com/sz-747/skillify-public.git skillify
```

Use the discovery folder name `skillify`, even when the repository has a different name. Copy or link the complete folder rather than its individual reference files. Store personal paths, account defaults and credentials in your workspace's private overlay, never in this repository.

Read [SKILL.md](SKILL.md) directly if your agent does not support folder discovery. Your workspace can point it at a private overlay using [this contract](docs/private-overlay.md).

## Use

Ask your agent:

> Use Skillify to turn my CSV review workflow into a reusable skill. First check for an existing match. Define its inputs, output, limits and completion checks. Keep it instruction-only unless a script removes a concrete execution gap. Do not publish or install it.

Skillify can also review a skill you already have. Its [guide](references/authoring-guide.md) explains the choices, and its [scaffold](references/skill-scaffold.md) gives an optional starting structure.

## Verify

From this checkout, with Python 3.11 or newer:

```sh
python -B -m unittest discover -s tests -v
```

The checks cover package structure, discovery metadata, bundled links and the generic overlay example. They do not prove that every agent will apply the method correctly. [Verification notes](docs/verification.md) separate checks from behavioural scenarios.

## Licence and sources

The original Skillify text and tests are available under the [MIT licence](LICENSE). [Source notes](SOURCES.md) credit the public authoring work that influenced the method. Upstream articles and repositories retain their own terms and are not included as copied or translated source files.
