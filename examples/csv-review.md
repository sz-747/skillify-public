# Example capability contract: CSV review

This is a fictional example for reviewing Skillify's output, not an installed skill.

## Result and boundaries

Check whether each input record has a unique `item_id` and a nonempty `title`. Read the user-specified UTF-8 CSV and write a report in the requested output directory. Do not change the input, fetch network data or infer missing field values.

## Required output

Write `review.csv` in UTF-8, with columns `item_id,status,reason` in that order. Preserve input record order and emit one output row per input record. Use `pass`, `fail` or `unknown`; every non-pass result needs a reason. For a missing identifier, write an empty `item_id` and identify the source row in the reason.

```csv
item_id,status,reason
item-001,pass,
item-002,fail,title is empty
```

## Completion and failure

Report the input count, output count and each status count. Confirm output headers and row counts. If the input cannot be read or required columns are absent, report the specific prerequisite and do not write a success report. Use normal CSV parsing so commas and quotes inside titles are handled correctly.

This example defines the result and its limits. It leaves the choice of an existing parser and inspection method to the agent.
