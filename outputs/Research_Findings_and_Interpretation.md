# Research Findings and Interpretation

Actual empirical file: `Dataset_TrustCalibration.csv`, SHA256 `0ffa5341b5dec771d2e11169ff3bceb4c43306a83677f32d2f81d3a997ef696d`. Observed 412 records and 50 columns; no synthetic observations. Numeric codes: {0: 206, 1: 206}.

The primary model used 412 record clusters and 1606 finite round observations. The four-round complete-case sample contains 370 records. These are record counts, not independently verified unique people.

## RQ1: measurement sensitivity

Code 0, Round 4 has 173 disagreements among 202 comparable values; 201 match the complement of the paper formula. On these same records the published mean is 0.6282, versus 0.3768 independently derived. This is inconsistent with the stated formula, but its production cause is unknown.

R3-R1: denominator-masked published estimate -0.0531; derived estimate -0.0531. The estimated direction is unchanged. These estimates compare code-1 change minus code-0 change.

R4-R1: denominator-masked published estimate -0.2916; derived estimate -0.0402. The estimated direction is unchanged. These estimates compare code-1 change minus code-0 change.

R4-R3: denominator-masked published estimate -0.2385; derived estimate 0.0128. The estimated direction reverses. These estimates compare code-1 change minus code-0 change.

## RQ2: consistently derived reliance trajectories

Condition 0 derived means by round: R1=0.5209, R2=0.3983, R3=0.2767, R4=0.3768. These are available-observation summaries, not paired changes.

Condition 1 derived means by round: R1=0.6174, R2=0.4186, R3=0.3201, R4=0.4330. These are available-observation summaries, not paired changes.

R3-R1: difference in changes -0.0531 WoA units, pointwise 95% CI [-0.1572, 0.0510], t(411)=-1.002, raw p=0.3169, Holm p=0.9507. This does not meet the .05 Holm criterion; it is not proof of no difference.

R4-R1: difference in changes -0.0402 WoA units, pointwise 95% CI [-0.1882, 0.1077], t(411)=-0.535, raw p=0.5932, Holm p=1. This does not meet the .05 Holm criterion; it is not proof of no difference.

R4-R3: difference in changes 0.0128 WoA units, pointwise 95% CI [-0.1406, 0.1663], t(411)=0.164, raw p=0.8696, Holm p=1. This does not meet the .05 Holm criterion; it is not proof of no difference.

These are available-observation mean-profile differences, conditional on independent records and the missingness pattern. The primary uncertainty intervals are not simultaneous. The secondary pair-complete Welch table instead compares average within-record changes, reporting Hedges g for the change distributions.

Within-code round changes are reported in a secondary six-test Holm family in within_code_round_contrasts.csv. The omnibus interaction is secondary and is not used to select the planned contrasts.

## Robustness

derived_complete: R3-R1: -0.0261 (Holm p=1); R4-R1: 0.0275 (Holm p=1); R4-R3: 0.0536 (Holm p=1).

derived_duplicate_excluded: R3-R1: -0.0525 (Holm p=0.9715); R4-R1: -0.0407 (Holm p=1); R4-R3: 0.0118 (Holm p=1).

derived_gap_at_least_2: R3-R1: -0.0457 (Holm p=0.8993); R4-R1: -0.0596 (Holm p=0.8993); R4-R3: -0.0139 (Holm p=0.8993).

The greatest absolute leave-one-record-out shift across primary contrasts was 0.0279 WoA units. Bootstrap intervals and median contrasts are exported. Random-intercept sensitivity status: converged and covariance checks passed. Model warnings are retained in mixed_model_status.json.

## RQ3 and RQ4

Not tested. Composite scoring, item mappings, administration timing and PT5 export reversal are unresolved. Raw-item plots are descriptions of recorded responses only. No moderation power claim is made for an unestimated, unvalidated composite model.

## Comparison with earlier research

Ouyang et al. (2026), printed pp. 11–13, reported a condition-by-round interaction and greater baseline reliance in Round 4. Our numeric-code comparison cannot be treatment-labelled. The exported late-round pattern is materially sensitive to the paper-defined formula. This is a reproducibility concern, not proof that the original authors used this exact erroneous export or that their entire analysis is false. Their complete-case count is reproduced, but their analysis input and scoring syntax are unavailable.

Graf (2025), pp. 7–11, found dynamic self-reported trust responses to system errors. Our outcome is judgment revision, not Graf's repeated trust instrument. Neither study justifies substituting a trust score for behavior. This notebook cannot estimate the catalogue's three disclosure interventions.

## Contribution, limits and next evidence

The contribution is a transparent sensitivity audit using real data. Statistical procedures cannot resolve unverified participant uniqueness, condition mapping, item scoring, source-version discrepancies, stimulus-round confounding or missing ground truth. Unmodelled repeat participation across nonidentical rows could invalidate record-level standard errors. The duplicate sensitivity cannot exclude that possibility. Undefined WoA is structural; available-observation and complete-case analyses target selected samples. No causal error effect, appropriate-reliance benefit, trust recovery, confirmed theoretical novelty or publication readiness is claimed.

Obtain the numeric condition key, questionnaire/scoring/export syntax, original analysis dataset and code, stimulus identifiers and actual ages, error-round clarification, and relevant ethics/reuse information. Formal professor acceptance of the revised scope remains undocumented. This notebook can be academically reviewed for its executed numerical audit; blocked substantive claims require additional evidence.