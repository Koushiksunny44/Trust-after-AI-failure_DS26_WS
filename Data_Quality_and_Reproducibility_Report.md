# Data Quality and Reproducibility Report

Source checksum: `0ffa5341b5dec771d2e11169ff3bceb4c43306a83677f32d2f81d3a997ef696d`.

Observed shape: (412, 50). Numeric codes: {0: 206, 1: 206}. No participant ID; 1 extra exact duplicate row(s), retained in primary analysis. Duplicate source locators: [{'record_id': 40, 'csv_line': 41}, {'record_id': 41, 'csv_line': 42}].

## Source column quality

| column | raw_dtype | blank | division_error | nonblank_unique |
| --- | --- | --- | --- | --- |
| Condition | str | 0 | 0 | 2 |
| Q1_1 | str | 0 | 0 | 2 |
| Q1_2 | str | 0 | 0 | 5 |
| Q1_3 | str | 0 | 0 | 4 |
| Q1_4 | str | 0 | 0 | 2 |
| Q2_1 | str | 0 | 0 | 6 |
| Q2_2 | str | 0 | 0 | 6 |
| Q2_3 | str | 0 | 0 | 7 |
| Q2_4 | str | 0 | 0 | 6 |
| Q2_5 | str | 0 | 0 | 7 |
| Q2_6 | str | 0 | 0 | 6 |
| Q2_7 | str | 0 | 0 | 7 |
| Q2_8 | str | 0 | 0 | 7 |
| Q2_9 | str | 0 | 0 | 7 |
| Q2_10 | str | 0 | 0 | 6 |
| Q2_11 | str | 0 | 0 | 7 |
| Q2_12 | str | 0 | 0 | 7 |
| Q2_13 | str | 0 | 0 | 7 |
| Q2_14 | str | 0 | 0 | 7 |
| Q2_15 | str | 0 | 0 | 7 |
| Q2_16 | str | 0 | 0 | 7 |
| Q2_17 | str | 0 | 0 | 7 |
| Q2_18 | str | 0 | 0 | 7 |
| R1_I | str | 0 | 0 | 23 |
| R1_A | str | 0 | 0 | 1 |
| R1_F | str | 0 | 0 | 17 |
| Q4_1 | str | 0 | 0 | 6 |
| Q4_2 | str | 0 | 0 | 7 |
| Q4_3 | str | 0 | 0 | 7 |
| R2_I | str | 0 | 0 | 32 |
| R2_A | str | 0 | 0 | 1 |
| R2_F | str | 0 | 0 | 24 |
| R3_I | str | 0 | 0 | 31 |
| R3_A | str | 0 | 0 | 1 |
| R3_F | str | 0 | 0 | 22 |
| Q6_1 | str | 0 | 0 | 7 |
| Q6_2 | str | 0 | 0 | 7 |
| Q6_3 | str | 0 | 0 | 7 |
| Q6_4 | str | 0 | 0 | 7 |
| Q6_5 | str | 0 | 0 | 7 |
| R4_I | str | 0 | 0 | 36 |
| R4_A | str | 0 | 0 | 1 |
| R4_F | str | 0 | 0 | 26 |
| WoA_R1 | str | 1 | 9 | 39 |
| WoA_R2 | str | 1 | 2 | 83 |
| WoA_R3 | str | 1 | 6 | 64 |
| WoA_R4 | str | 0 | 4 | 69 |
| Unnamed: 47 | str | 412 | 0 | 0 |
| Unnamed: 48 | str | 412 | 0 | 0 |
| WoA_R1.1 | str | 212 | 0 | 81 |

## WoA audit

| condition | round | records | undefined | published_numeric | recalculated_finite | comparable | disagreements | complement_matches | outside_0_1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 206 | 9 | 197 | 197 | 197 | 0 | 27 | 1 |
| 0 | 2 | 206 | 2 | 204 | 204 | 204 | 0 | 8 | 7 |
| 0 | 3 | 206 | 6 | 200 | 200 | 200 | 0 | 16 | 12 |
| 0 | 4 | 206 | 4 | 202 | 202 | 202 | 173 | 201 | 18 |
| 1 | 1 | 206 | 7 | 205 | 199 | 199 | 0 | 22 | 1 |
| 1 | 2 | 206 | 3 | 205 | 203 | 203 | 0 | 15 | 8 |
| 1 | 3 | 206 | 7 | 205 | 199 | 199 | 0 | 21 | 11 |
| 1 | 4 | 206 | 4 | 206 | 202 | 202 | 0 | 35 | 21 |

## Interpretation

Blank cells, division-error strings and numeric zeros at zero denominators differ. Undefined ratios are missing by the original paper rule. Published values are retained separately. Empty unnamed columns and feedback text are excluded only from the numeric analytical view. No complete stimulus ground truth, explicit participant identifier or numeric condition codebook exists in the supplied file. Questionnaire values are within 1–7, but scoring/administration/export coding remain unresolved. See discrepancy tables for exact source-line references.

## Integrity checks

| check | passed |
| --- | --- |
| raw_dataframe_preserved | True |
| source_file_checksum_unchanged | True |
| four_rounds_per_source_record | True |
| all_undefined_ratios_missing | True |
| formula_reconstructs_final_judgments | True |
| finite_unclipped_ratios_retained | True |
| complete_case_count_matches_observed_filter | True |
| primary_matches_direct_cell_mean_contrasts | True |
| holm_probabilities_valid | True |
| primary_sample_count_matches_table | True |