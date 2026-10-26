# Verification

## Offline checks

From the repository root, run:

```sh
python -B -m unittest discover -s tests -v
```

The test suite checks that the root metadata is readable, exactly one discoverable root exists, bundled Markdown links resolve, private configuration is excluded by the repository's ignore rules, and a complete fictional output example remains available.

## Behavioural review scenarios

| Request | Expected contract |
|---|---|
| Create a small instruction-only skill | Goal, scope, inputs, output and completion evidence; no unnecessary executable layer. |
| A matching capability already exists | Inspect it and extend it when sufficient. |
| Build a tool-backed skill | State runtime, working directory, interface, artifacts and meaningful error checks. |
| Required data or access is missing | Name the incomplete result without fabricating input or verification. |
| The workspace requires registration checks | Complete those checks and distinguish configuration from an observed fresh-session load. |
| A task involves live, paid or destructive operations | Stay within the current authorisation; a skill does not create permission. |
| A public package needs private settings | Document their interface and keep the real overlay out of the tracked tree. |

These are review scenarios, not claims of independent model execution. Structural tests do not establish that every model will follow the skill reliably. Fresh-session discovery and downstream task performance must be reported separately when observed.

The [CSV example](../examples/csv-review.md) provides a concrete output contract for cold-start review.

## Release preparation evidence

On 26 October 2026, all six offline checks passed on the prepared public edition. A review of its 13 tracked files with the release scanner and a private deny list reported no findings. This records the checks that ran, rather than claiming fresh-session model behaviour or a downstream authoring evaluation.
