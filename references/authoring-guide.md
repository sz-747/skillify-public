# Writing a capability another agent can use

## Begin with a result

A skill should make a recurring task easier to complete. Describe that result before collecting tips, tools or background. If the same outcome is already covered by a skill in the destination, improve that skill or narrow the new scope.

For a CSV reviewer, “look at the file carefully” leaves completion to the reader's imagination. A better contract is: “Write a UTF-8 report with one row per input identifier. Each row contains `item_id`, `status` and `reason`; status is `pass`, `fail` or `unknown`.” The agent still chooses how to inspect the input, but the result can be checked.

## Write for a reader without the original conversation

Name the inputs, permitted resources, output location and limits. Explain an unfamiliar term where it first matters. A reference to “the usual folder” or “the account we use” must become a workspace-supplied setting, not a guess.

Missing prerequisites deserve specific behaviour. If a repository cannot be read, report which checks are incomplete. If a tool fails, preserve a useful status or error category while removing private values. Do not substitute a plausible result to make a checklist pass.

## Keep mandatory order where it matters

Some operations depend on earlier evidence: an importer needs a validated file, and a public release needs a reviewed public tree. State those dependencies. Ordinary methods such as grouping notes, choosing search terms or dividing a report into sections can remain suggestions.

Use this test on each required instruction: what specific failure would become more likely without it? Remove instructions that only repeat the workspace's authority rules or the tool's manual. Link substantial detail so the root stays easy to load.

## Match the package to the work

A one-file method can be useful. A reference is worthwhile when the agent needs detail only for some requests. Code is worthwhile when it makes repeated parsing, validation or file generation more reliable than ad hoc agent work.

For a CLI, document working directory, runtime, arguments, output fields, output files and exit behaviour. Test success, malformed input and a meaningful recovery case. A diagram or a long README cannot replace a usable interface.

Use an independently versioned repository when dependencies, code or release cadence require one. Do not add a library, server or command merely to make an instruction skill look more complete.

## Separate method from installation

The public skill says what it does and which setting names it accepts. The receiving workspace supplies real routes, accounts and authority limits through its private overlay. An example should use fictional settings and must never silently become a working default.

The workspace decides how skills are discovered. Register one root entry, retain references inside the package and report whether discovery was merely configured or observed in a fresh session.

## Test the claim being made

Link checks establish that bundled resources exist. A schema test establishes a structural contract. Neither establishes the quality of the reasoning a future model will produce.

For a judgement skill, use a representative task or a clear before-and-after example. Record what was inspected and what remains unverified. When a real failure occurs, save its trigger, consequence and correction; do not invent a history of failures for a new package.

## Final author review

Read the package without the authoring conversation. Can you tell what to produce, which resources are available, what requires permission, and how completion is checked? If not, repair the contract. Adding more surrounding prose rarely fixes a missing boundary or an undefined output.
