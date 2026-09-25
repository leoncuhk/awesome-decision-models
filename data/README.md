# Data contract

- `catalog.json`: source register and bilingual resource entries. `source_revision` pins a source, not weights. `review_depth` is `content_reviewed`, `abstract_reviewed` or `metadata_only`.
- `evaluations.json`: claim-level performance records, including protocol, reporter provenance, metrics, caveats and artifact status. Fractions use [0,1], not percentages. Unknown versions/dates are `null`.
- `watchlist.json`: explicit change-detection endpoints. It is not an exhaustive bibliography or an automatic claim-verification system.

All files use UTF-8 JSON and `schema_version: 1`. `scripts/validate.py` enforces the current contract without third-party packages. `scripts/render.py` generates both READMEs and the model/evidence/source documents. Editorial methodology and selection guidance remain hand-written.

Do not turn missing information into a zero, “none,” verified license or assumed model version. For a real reproduction, use `evidence_type: reproduced_here`, `reproduced_here: true`, and a `reproduction` object with evaluator, environment, command and an accessible artifact path; retain all ordinary protocol fields.
