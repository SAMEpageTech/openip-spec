# OpenIP: Clip & Derivative Rights Envelopes (CRE/DRE)

Portable, machine‑readable rights & residuals for UGC and AI derivatives.

**Status:** v0.1 draft — open, royalty‑free spec.  
**Goals:** “Licnese once, monetize everywhere.”

- **CRE** covers UGC clips: ownership, consents, terms, platform policy links, payout splits.  
- **DRE** covers canon‑safe AI derivatives: ShowSpec guardrails, likeness/voice tokens, lineage, splits.

**Implementers**: start with the JSON Schemas, run the validator, and follow `CONFORMANCE.md`.  
**Trademark**: “OpenIP”, “CRE”, “DRE” are trademarks; see `TRADEMARK-POLICY.md` for badge usage.

## Getting started

1. Review `cre/` and `dre/` specs and schemas.  
2. Run the validator locally: `python -m openip_validate validate --schema cre/cre.schema.json --examples cre/examples` (see `tools/openip-validate`).  
3. Submit issues or PRs following `CONTRIBUTING.md`.
