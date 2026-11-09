# Research Methodology and Analytical Decisions

This is an executed secondary-data reproducibility audit of the supplied empirical CSV. The original catalogue intervention study is not implemented. Professor acceptance of the revised scope is not documented.

## Record linkage and preprocessing

CSV row ordinals are analytical record keys, not fabricated participant identities. Four rounds are linked only within their existing source row. Independent records are an inferential assumption; unique participants cannot be certified. All raw strings and original files are preserved. Exact duplicates are retained in the primary analysis, with exclusion sensitivity. No imputation, clipping, synthetic replacement data or accuracy proxy is used.

## Estimands and methods

The primary outcome is paper-defined signed WoA=(F-I)/(A-I), missing when A=I. The primary model uses eight saturated numeric-condition-by-round means, with record-clustered sandwich covariance, finite-cluster correction and t/F inference. Three code-1-minus-code-0 differences in changes (R3-R1, R4-R1, R4-R3) form one Holm-adjusted family. Pointwise 95% intervals and raw WoA-unit effects are reported. This is an available-observation mean-profile estimand, not necessarily an average paired change.

Secondary pair-complete Welch tests report differences in within-record change, Welch degrees of freedom, intervals and Hedges g. Their multiplicity family is separate and secondary. Within-code round contrasts have a separate secondary six-test Holm family. A stratified record bootstrap provides mean/median uncertainty. A random-intercept-by-record model is an alternative covariance specification using Powell optimization; convergence, covariance diagnostics and warnings are explicitly recorded. Invalid fits are not treated as evidence.

Sensitivity comparisons isolate exported numeric values, denominator masking, formula recalculation, four-round complete cases, later exact-duplicate removal and absolute advice gaps of at least two years. Small-gap exclusion changes the sample and is not a validated cutoff. No out-of-range finite WoA is excluded merely for being outside 0–1. Residual, ratio-gap and leave-one-record influence diagnostics are exported.

## Blocked analyses and scope

Condition treatment labels, validated questionnaire composites and moderators, and accuracy are blocked. Raw questionnaire responses are shown by column without assuming item wording or score direction. PT5 reversal is documented in Appendix A, but its exported status and column mapping remain unresolved. The figure's single example age is insufficient ground truth for four stimuli. Round changes confound time, stimulus and error history. Missingness is structural, and neither complete-case nor available-observation inference removes that selection limitation.

## Sources

Ouyang, Jahng & Woo (2026), DOI 10.1080/10447318.2026.2705163, printed pp. 6–9 (design, formula, missingness), 10–13 (published analyses), Appendix A p. 19 (questionnaire). Dataset DOI 10.17632/5w56cp2ftr.1, V1, CC BY 4.0: attribute original authors; independently derived analytical columns are modifications, not author corrections. Graf (2025), DOI 10.1016/j.chb.2025.108736, pp. 4–7 and 10–11. UE catalogue: Project 7 and common checkpoints. The preceding research-design audit is documented in the project conversation; a separate audit attachment was not supplied.

## Academic review boundary

This project documents reproducibility and sensitivity, not independent confirmation, new intervention evidence or publication readiness. Required clarifications: numeric codebook, questionnaire scoring/timing/export syntax, original analysis input/code, complete stimulus key/ages, error-round discrepancy, and ethics/reuse documentation. No messages to authors were sent.
