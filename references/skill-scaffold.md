# Optional skill scaffold

Use only the sections the capability needs. Replace the placeholders before delivering a finished skill. The structure below is an example, not a universal heading order.

```markdown
---
name: <lowercase-hyphen-name>
description: <Capability and the requests that should trigger it.>
---

# <Capability>

## Result and scope

<What useful result the skill produces.>
<What is excluded and which authority boundaries apply.>

## Inputs and resources

<Required inputs, permitted tools and bundled references.>
<Runtime and working directory for any executable commands.>
<What happens when input or access is missing.>

## Completion evidence

<Observable conditions for success and partial completion.>
<Meaningful automated checks or semantic review conditions.>

## Deliverable

<Exact files, location, format, fields and a representative example.>

## Suggested methods

<Optional approaches that help the agent reason about the task.>
```

Known pitfalls are optional. Add them only when a failure and correction have actually been observed.
