# Quality Control Report

## Archive repair scope

The supplied ZIP had 55 recorded SHA-256 checksums, 32 mismatches and no missing manifest-listed files. These were stale checksums relative to the supplied locally executed files; they do not by themselves establish scientific corruption. Removed 61 macOS metadata entries (`__MACOSX` and AppleDouble). No analysis was rerun.

## Verification results

| Check | Result |
| --- | --- |
| Final archive | 56 project files; ZIP CRC integrity passed |
| Package manifest | All 55 listed SHA-256 values match the exact packaged bytes |
| Manifest coverage | Every project file except the manifest itself is hashed; no missing, duplicate or extra members |
| Manifest references | Dataset, notebook, output and report references exist inside the project |
| Dataset path | `data/Dataset_TrustCalibration.csv`, relative to the project root |
| Notebook preservation | Entire supplied notebook, including all saved outputs, unchanged byte-for-byte |
| Saved execution record | 13 code cells have execution counts; zero saved error outputs |
| Scientific file preservation | All 23 table CSVs, 16 PNG/PDF figure files, model summaries, results narrative and source data unchanged byte-for-byte |
| Dependencies | Supplied requirements retained; pinned versions agree with the local runtime manifest |
| macOS metadata | No `__MACOSX`, AppleDouble or `.DS_Store` entries remain |

Dataset SHA-256: `0ffa5341b5dec771d2e11169ff3bceb4c43306a83677f32d2f81d3a997ef696d`.

Preserved notebook SHA-256: `31e0a996fabd586fc1fe74170bf16435030c0fbbe5a04f6cb9ffbf58fc9d0c79`.

Only `README.md`, `Quality_Control_Report.md`, `outputs/execution_manifest.json`, `package_project.py` and `package_manifest.json` were changed. The packaging utility now excludes macOS metadata, uses portable paths, hashes final files and verifies the completed ZIP. Original local runtime information and execution time remain recorded. The manifest excludes its own checksum to avoid circularity.

## Execution evidence and unresolved matters

Successful local execution was reported by the project author. This repair independently inspected saved notebook structure, execution counts and outputs; it did **not** independently rerun the notebook. Absolute machine paths inside preserved saved notebook outputs are historical records, not package lookup paths, and were left untouched to preserve the notebook exactly. A future analysis rerun may regenerate an absolute path in the notebook-generated execution manifest; running `package_project.py` afterwards normalizes the packaged manifest.

`outputs/presentation_quality_checks.json` is retained as a historical presentation-review record, not evidence that later locally regenerated files equal an older build. The checks above compare this repaired package with the **attached ZIP**.

No unresolved packaging defect was detected by these checks. Existing scientific limitations remain: unverified unique participants and numeric condition mapping; unresolved questionnaire mapping/scoring/timing/PT5 export status; missing complete stimulus ages/identifiers; the source paper's error-round inconsistency and interpretability discrepancy; incomplete original-analysis provenance; and undocumented professor acceptance/ethics determinations. Non-significant results are not evidence of equivalence, and no publication-readiness certification is made.
