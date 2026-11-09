"""Package final file bytes and verify the completed archive; never execute the notebook."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT.parent / 'Trust_After_AI_Failure_Corrected.zip'
NOTEBOOK = 'Empirical_Analysis_Trust_After_AI_Failure.ipynb'
DATASET = 'data/Dataset_TrustCalibration.csv'
EXCLUDED = {'__MACOSX', '__pycache__', 'support', '.ipynb_checkpoints', '.venv'}

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def project_path(value):
    rel = PurePosixPath(value)
    if rel.is_absolute() or '..' in rel.parts or '\\' in value:
        raise ValueError(f'Nonportable manifest reference: {value}')
    path = ROOT.joinpath(*rel.parts)
    if not path.is_file() or not path.resolve().is_relative_to(ROOT):
        raise FileNotFoundError(f'Missing or external manifest reference: {value}')
    return path

def excluded(path):
    rel = path.relative_to(ROOT)
    return bool(set(rel.parts) & EXCLUDED) or any(p.startswith('._') or p=='.DS_Store' for p in rel.parts)

execution_path = ROOT/'outputs/execution_manifest.json'
execution = json.loads(execution_path.read_text())
if sha256(project_path(DATASET)) != execution['source_sha256']:
    raise ValueError('Dataset checksum differs from the recorded empirical source')
execution['data_path'] = DATASET
execution['data_path_base'] = 'project_root'
execution['notebook_path'] = NOTEBOOK
execution['notebook_sha256'] = sha256(project_path(NOTEBOOK))
for reference in execution['outputs']:
    project_path(reference)
for reference in execution.get('packaging_revision',{}).values():
    if isinstance(reference,str) and reference in ['outputs/presentation_quality_checks.json','Quality_Control_Report.md']:
        project_path(reference)
execution_path.write_text(json.dumps(execution,indent=2)+'\n')

files = sorted(p for p in ROOT.rglob('*') if p.is_file() and not excluded(p) and p.name!='package_manifest.json')
manifest = {p.relative_to(ROOT).as_posix():sha256(p) for p in files}
manifest_path = ROOT/'package_manifest.json'
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(ARCHIVE,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(files+[manifest_path]):
        z.write(p,arcname=PurePosixPath(ROOT.name)/p.relative_to(ROOT).as_posix())
with zipfile.ZipFile(ARCHIVE) as z:
    if z.testzip() is not None:
        raise RuntimeError('ZIP CRC integrity failure')
    names = z.namelist()
    prefix = ROOT.name+'/'
    embedded = json.loads(z.read(prefix+'package_manifest.json'))
    if len(names)!=len(set(names)) or set(names)!={prefix+n for n in embedded}|{prefix+'package_manifest.json'}:
        raise RuntimeError('Missing, duplicate or unmanifested ZIP members')
    for relative,expected in embedded.items():
        if hashlib.sha256(z.read(prefix+relative)).hexdigest()!=expected:
            raise RuntimeError(f'Packaged checksum mismatch: {relative}')
print(json.dumps({'archive':str(ARCHIVE),'project_files':len(names),'checksums_verified':len(embedded),'crc_test':'passed'},indent=2))
