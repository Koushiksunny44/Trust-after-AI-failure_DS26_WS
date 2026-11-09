# Trust After AI Failure

## A Reproducibility and Measurement-Sensitivity Analysis of Behavioural Reliance in Human–AI Interaction

Open `Empirical_Analysis_Trust_After_AI_Failure.ipynb` in JupyterLab, Jupyter Notebook, VS Code or another compatible reader. The delivered notebook contains executed outputs. Unzip this complete project before rerunning it.

## Dataset and attribution

The empirical dataset used in this project is:

**The Transparency Paradox: Decoupling Perceived and Behavioral Trust through Trust Calibration in Human-AI Interaction**

- **Authors:** Luoman Ouyang, Jungjoo Jahng, and Suhan Woo
- **Source:** [Mendeley Data](https://doi.org/10.17632/5w56cp2ftr.1)
- **Version:** 1
- **Licence:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

The original CSV, `Dataset_TrustCalibration.csv`, is included in `data/`. The dataset is redistributed under its stated CC BY 4.0 licence. Analytical copies and derived outputs are documented separately; the original source data is preserved unchanged.

## Run from top to bottom

Use Python 3.12 or newer and a fresh virtual environment:

```bash
python -m venv .venv
# Activate .venv using your operating system's usual command.
python -m pip install -r requirements.txt
python -m ipykernel install --user --name trust-research --display-name "Trust After AI Failure"
```

Launch Jupyter in this project directory, choose the environment just installed, and use Restart Kernel and Run All. If your notebook application is not installed, install JupyterLab separately. No internet access is used by the analysis itself. The original empirical CSV is bundled at `data/Dataset_TrustCalibration.csv`. If using the notebook alone, place the actual CSV beside it or set `TRUST_CSV` to its exact location. Conflicting file versions cause an error rather than arbitrary selection.

An additional socket-free execution option is:

```bash
python execute_notebook.py
python package_project.py
```

The execution command reruns every code cell and replaces the notebook's saved outputs. **Do not run it merely to repair or verify this archive.** The attached notebook was successfully executed locally according to the project author. For this archive repair, its saved execution counts and outputs were inspected, and the entire notebook file was preserved byte-for-byte. No analysis was rerun.

The packaging command does not execute or rewrite the notebook, figures, tables or source dataset. It normalizes the execution-manifest dataset path to `data/Dataset_TrustCalibration.csv`, interpreted relative to the project root (the directory containing this README), and records the current notebook checksum. It verifies referenced files, excludes macOS metadata and temporary support files, regenerates `package_manifest.json` from the final bytes, and reads the completed ZIP back to validate every checksum and its CRC integrity.

To rebuild only the archive, run:

```bash
python package_project.py
```

The archive contains 56 project files. The package manifest hashes the other 55 files and deliberately excludes itself to avoid a circular checksum. All execution-manifest output paths are relative to the same project root. Original local runtime versions and execution timestamp are retained as provenance; the repair is not a new execution. `outputs/presentation_quality_checks.json` is an earlier presentation-review record, not a certification of later local reruns; the current packaging checks are described in `Quality_Control_Report.md`.

## Files

- The notebook contains the full analysis, documentation and generated interpretation.
- `Methodology_and_Analytical_Decisions.md` explains the estimands, assumptions and blocked analyses.
- `Data_Quality_and_Reproducibility_Report.md` records observed validation results and checks.
- `outputs/tables/` contains auditable CSV results and record/source-line locators.
- `outputs/figures/` contains eight figures in PNG and vector PDF formats.
- `outputs/Research_Findings_and_Interpretation.md` contains the code-generated results narrative.
- `outputs/execution_manifest.json` retains local runtime dependencies and sample counts, and records portable paths, notebook integrity and the scope of saved-output inspection.
- `outputs/mixed_model_status.json` records alternative-model diagnostics and warnings.
- `requirements.txt` pins the tested package versions. These are environment records, not claims that older compatible versions cannot work.
- `sources_and_scope.md` identifies sources, attribution and outstanding evidence.
- `Change_Log.md` records the naming and presentation changes and the scientific content preserved.
- `Quality_Control_Report.md` records execution, numerical comparisons and unresolved research matters.
- `outputs/presentation_quality_checks.json` contains historical presentation-preservation checks; see the current quality-control report for archive-repair checks.

Re-execution overwrites derived outputs, not the source CSV. Outputs are written beneath the current working directory. The command-line helper sets that directory to the project root.

## Interpretation limits

`record_id` means a CSV row ordinal. It is not a verified participant ID. Condition codes are not treatment-labelled. No synthetic data, questionnaire composites, accuracy measures or invented ground truth are used. The duplicate pair is retained in the primary analysis and excluded only in a labelled sensitivity analysis. No published WoA value is overwritten.

This project is ready to inspect as an executed empirical audit. It does not resolve professor acceptance, participant uniqueness, numeric treatment mapping, questionnaire scoring, original-file discrepancies or missing stimulus truth. It is not a publication-readiness certification.
