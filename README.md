PROJECT— TRUST AFTER AI FAILURE
Kaggle notebook starter package

Files:
- Project_7_Trust_After_AI_Failure_Kaggle.ipynb

How to use:
1. Download the .ipynb file or upload it to a Kaggle Notebook.
2. In Kaggle, choose Notebook settings > Accelerator > GPU if you want a GPU-enabled runtime.
3. Run all cells from top to bottom.
4. The default mode creates synthetic demonstration data so the analysis pipeline can be tested.
5. For approved participant data, upload the anonymized CSV, set USE_REAL_DATA = True, and set REAL_DATA_PATH to the CSV file or its containing folder.
6. The notebook saves PDF figures and CSV tables, then creates a ZIP archive in /kaggle/working.

Important:
- Synthetic data are not participant observations and must not be used as empirical findings.
- The notebook is an analysis pipeline and demonstration, not a deployed participant-facing experiment.
- Obtain ethics approval, informed consent, and a design-specific power justification before recruitment.
- GPU acceleration is not expected to materially speed up the statistical models in this project.
