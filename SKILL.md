---
name: skillify
license: MIT
description: Create or rewrite reusable agent skills as portable folders or independent repositories. Use when writing a new skill, capturing a repeatable capability, or reviewing a skill's outcomes, boundaries, components, and verification.
---

# Skillify

## Goal and scope

Produce a reusable skill that a new agent can understand, find and verify without the conversation that created it. Improve a matching existing skill when that is enough; do not create a competing capability by accident.

This is an authoring and review skill. It does not grant permission to install software, move existing skills, create repositories, publish content, contact people or use paid services. Follow the user's request and the destination workspace's own authority rules.

## Before choosing a location

Read the destination's agent instructions, skill catalogue and any applicable local overlay. The workspace must identify its own overlay; this package does not assume a personal directory, account or machine. An overlay can set destinations, discovery locations, source-recording rules and required checks. See [the overlay contract](docs/private-overlay.md).

Identify the nearest existing capability and decide whether to extend it or create a new one. Use a folder for a small instruction-only skill. Give a tool, independently maintained package or distinct release lifecycle its own repository only when that scope is requested or otherwise authorised.

## Required result

The finished skill must answer these questions in its own words:

- What useful result does it produce, and when should an agent use it?
- What inputs, tools and references may it use? What lies outside its scope?
- What observable evidence distinguishes completion from a partial attempt?
- What exactly must be delivered, in which format and location?
- What happens when input, access, a dependency or verification is missing?

Write a capability contract, not a transcript of how the author happened to solve one task. Leave ordinary reasoning to the agent. Require an order only when a later operation needs an earlier result or a boundary depends on it.

Use [the authoring guide](references/authoring-guide.md) for examples and trade-offs. [The scaffold](references/skill-scaffold.md) is an optional starting point, not a mandatory sequence of headings.

## Packaging and discovery

For a new portable folder, use one root `SKILL.md` with a lowercase, hyphenated `name` and a description that states the capability and its trigger. Install it under that discovery name. Keep supporting references internal; do not register every helper as a separate skill.

Use relative links for bundled material. A dependency outside the package needs an explicit public installation contract or a documented workspace-supplied interface. A private sibling directory is not a portable dependency.

Add components because they are useful:

- `README.md` explains installation, ordinary use and limits to people.
- `AGENTS.md` gives maintainers the relevant edit and validation rules.
- `references/` holds detail the root can load when needed.
- Examples show a complete result or a representative input/output pair.
- Scripts and tests handle repeated mechanical work where existing tools leave a real gap.
- A dependency manifest and lockfile belong with actual runtime dependencies.
- Requirements, design and working notes belong with capabilities substantial enough to need continuity.

Avoid empty directories and a custom executable layer for an instruction-only method. Use [the source notes](SOURCES.md) to distinguish the original material in this package from its influences.

## Privacy and configuration

Public instructions describe generic behaviour, setting names and fictional examples. Personal routes, account defaults, aliases, credentials, permission limits and user data belong in a private overlay outside the public tree or in a deliberately ignored local file.

Do not invent real settings or silently substitute the author's environment. A missing required value must name the setting and explain which result cannot be produced. Keep useful error status and context while removing credentials and private payloads.

## Verification and acceptance

Complete only the checks that provide evidence for the requested capability:

1. A reader with no source conversation can identify the goal, boundaries, inputs, deliverables and completion conditions.
2. The package contains its root entry point and every bundled resource it links to. Commands state their working directory, runtime, inputs, outputs and failure behaviour.
3. The discovery entry is configured exactly once. Complete the destination's required registration and lifecycle checks. Distinguish configured discovery from an actual fresh-session load.
4. Mechanical claims have a script, test or reproducible inspection where useful. Semantic claims have explicit review conditions or a representative task with observable results.
5. Missing input or tool access produces an honest partial or blocked result. No data, test output or successful execution is fabricated.
6. Live, account-dependent, hardware, destructive and paid tests stay within the current authorisation. Offline checks are the default where possible.
7. Each paragraph earns its place: remove repeated policy, background and process that do not improve the chance of producing the stated result.

Record only failures that actually occurred as known pitfalls. A new capability can have no history. Proposed failure cases belong in scenarios until observed.

## Delivery

Return the finished folder or authorised repository, whether an existing capability was extended, and a concise list of added components. Report the discovery method, checks actually run, their results and any remaining limitation.

A structurally valid skill is not proof that agents execute it reliably. Describe an untested skill as a draft rather than claiming runtime success. For this package's own checks and scenarios, see [verification](docs/verification.md).
