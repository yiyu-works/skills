#!/usr/bin/env python3
"""Dependency-free repository structure and resource checks."""
import ast,json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
NAMES={'readme-polish','ui-design','frontend-check','clear-writing','html-report','web-slides','web-motion','icon-set','cover-maker','video-to-article'}

def validate(root=ROOT):
    errors=[]
    folders={p.name for p in (root/'skills').iterdir() if p.is_dir()}
    if folders!=NAMES:errors.append('Expected exactly ten skill directories')
    for name in sorted(NAMES):
        folder=root/'skills'/name
        try:
            text=(folder/'SKILL.md').read_text()
            match=re.match(r'^---\n(.*?)\n---\n',text,re.S)
            if not match:raise ValueError('Missing frontmatter')
            fields=dict(re.findall(r'^(name|description): (.+)$',match[1],re.M))
            if fields.get('name')!=name:raise ValueError('Name mismatch')
            description=json.loads(fields.get('description','null'))
            if not isinstance(description,str) or not description.strip():raise ValueError('Empty description')
            for relative in re.findall(r'\]\(((?:references|assets|scripts)/[^)]+)\)',text):
                if not (folder/relative).is_file():errors.append(f'{name}: missing {relative}')
            for script in re.findall(r'\b(scripts/[a-z0-9_/-]+\.py)\b',text):
                if not (folder/script).is_file():errors.append(f'{name}: missing {script}')
            for required in ['README.md','CHANGELOG.md','agents/openai.yaml']:
                if not (folder/required).is_file():errors.append(f'{name}: missing {required}')
            for relative in [f'examples/{name}/README.md',f'evaluations/{name}/cases.md']:
                if not (root/relative).is_file():errors.append('Missing '+relative)
        except (OSError,ValueError) as e:errors.append(f'{name}: {e}')
    for path in root.rglob('*.py'):
        if '.git' not in path.parts:
            try:ast.parse(path.read_text())
            except SyntaxError as e:errors.append(f'{path}: {e}')
    for path in root.rglob('*.svg'):
        try:ET.parse(path)
        except ET.ParseError as e:errors.append(f'{path}: {e}')
    return errors
if __name__=='__main__':
    errors=validate()
    print('\n'.join(errors) if errors else 'Ten skill packages and referenced resources validated.')
    sys.exit(bool(errors))
