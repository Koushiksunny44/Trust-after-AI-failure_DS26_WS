"""Execute every notebook cell in a fresh IPython process without network sockets.

Run: python execute_notebook.py. Rich outputs and execution counts are saved.
For a conventional Jupyter UI, open the notebook and use Restart/Run All.
"""
from pathlib import Path
import json
import hashlib
import sys
import nbformat
from IPython.terminal.interactiveshell import TerminalInteractiveShell
from IPython.utils.capture import capture_output

ROOT = Path(__file__).resolve().parent
PATH = ROOT / 'Empirical_Analysis_Trust_After_AI_Failure.ipynb'
nb = nbformat.read(PATH, as_version=4)
for index, cell in enumerate(nb.cells):
    if cell.cell_type == 'code':
        try:
            compile(cell.source, f'cell_{index}', 'exec')
        except SyntaxError:
            print(f'Syntax error in cell {index}', file=sys.stderr)
            raise
import os
os.chdir(ROOT)
shell = TerminalInteractiveShell.instance()
shell.display_formatter.active_types = ['text/plain', 'text/html', 'text/markdown', 'image/png', 'image/svg+xml', 'application/json']
shell.run_line_magic('matplotlib', 'inline')
for cell in nb.cells:
    if cell.cell_type == 'code':
        cell.outputs = []
        cell.execution_count = None
try:
    for index, cell in enumerate(nb.cells):
        if cell.cell_type != 'code':
            continue
        count = shell.execution_count
        with capture_output(stdout=True, stderr=True, display=True) as captured:
            result = shell.run_cell(cell.source, store_history=True)
        cell.execution_count = count
        if captured.stdout:
            cell.outputs.append(nbformat.v4.new_output('stream', name='stdout', text=captured.stdout))
        if captured.stderr:
            cell.outputs.append(nbformat.v4.new_output('stream', name='stderr', text=captured.stderr))
        for rich in captured.outputs:
            cell.outputs.append(nbformat.v4.new_output('display_data', data=rich.data, metadata=rich.metadata))
        error = result.error_before_exec or result.error_in_exec
        if error:
            cell.outputs.append(nbformat.v4.new_output('error', ename=type(error).__name__,
                                                      evalue=str(error), traceback=[repr(error)]))
            raise RuntimeError(f'Cell {index} failed: {error}') from error
        print(f'Executed cell {index} ({count})', flush=True)
finally:
    nbformat.write(nb, PATH)
errors = [(i, o.get('ename'), o.get('evalue'))
          for i, c in enumerate(nb.cells) for o in c.get('outputs', [])
          if o.output_type == 'error']
counts = [c.execution_count for c in nb.cells if c.cell_type == 'code']
if errors or any(v is None for v in counts):
    raise RuntimeError({'errors': errors, 'execution_counts': counts})
manifest_path = ROOT / 'outputs' / 'execution_manifest.json'
manifest = json.loads(manifest_path.read_text())
manifest.update(notebook_execution='Fresh IPython process: all code cells completed without errors; rich outputs captured',
                execution_transport='In-process IPython; host denies TCP and Unix-domain kernel sockets',
                executed_code_cells=len(counts),
                notebook_sha256=hashlib.sha256(PATH.read_bytes()).hexdigest())
manifest_path.write_text(json.dumps(manifest, indent=2))
print(json.dumps({'executed_code_cells':len(counts),'errors':errors,
                  'notebook':str(PATH),'manifest':str(manifest_path)},indent=2))
