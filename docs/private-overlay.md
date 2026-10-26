# Private overlay contract

An overlay is the receiving workspace's private supplement to the public skill. It supplies installation choices and local policy without changing the portable capability.

Skillify is read by an agent; it is not a program that automatically loads a configuration file. Point to the overlay explicitly in the workspace's agent instructions or skill catalogue, and tell the agent to read it with Skillify. Never assume that writing a file makes an agent discover it.

The overlay can define:

- The destination for new skills and private working material.
- Existing catalogues and supported discovery locations.
- Required registration, validation and documentation checks.
- Private account defaults, permission limits and source records.
- Where actual credentials are stored, without copying their values into the skill.

The public package should not know those values. The workspace's authority rules still govern actions, and a reference document does not grant new permission.

Use [the fictional example](../examples/private-overlay.example.md) as a starting point. Put the real overlay outside the repository, or in an explicitly ignored path. In this package, `local/`, local setting files and the real counterpart of the example are ignored.

A fresh clone works without an overlay. For a task that requires an unknown local setting, inspect the workspace instructions first, then ask only for the missing value that changes the result. Do not guess a personal route or silently use the package author's setup.
