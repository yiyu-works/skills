#!/usr/bin/env python3
"""Build an offline comparison page for trusted local HTML candidates."""
import argparse, html, os
from pathlib import Path
from urllib.parse import quote

def build(output, candidates):
    output=Path(output).resolve()
    if output.exists():raise ValueError('Output already exists')
    cards=[]
    for candidate in candidates:
        candidate=Path(candidate).resolve()
        candidate.relative_to(output.parent)
        if candidate.suffix.lower() not in ('.html','.htm') or not candidate.is_file():
            raise ValueError('Candidate must be an existing HTML file')
        path=quote(os.path.relpath(candidate,output.parent).replace(os.sep,'/'),safe='/')
        title=html.escape(candidate.stem)
        cards.append(f'<article><h2>{title}</h2><a href="{path}" target="_blank" rel="noopener">打开原页面</a><iframe sandbox="allow-scripts" title="{title}" src="{path}"></iframe></article>')
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text("""<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>设计比较</title><style>body{margin:24px;background:#f4f2eb;color:#183d30;font:16px system-ui}header{display:flex;gap:16px;align-items:center;flex-wrap:wrap}.grid{display:flex;gap:24px;overflow:auto;padding-bottom:24px}article{flex:none;width:720px}h2{font-size:20px}iframe{display:block;width:100%;height:760px;border:1px solid #aaa;background:white;margin-top:12px}button,a{font:inherit}button{padding:8px 16px}button[aria-pressed=true]{background:#183d30;color:white}</style><header><h1>设计比较</h1><button data-width="720" aria-pressed="true">桌面预览</button><button data-width="390" aria-pressed="false">手机预览</button></header><p>隔离预览用于比较布局；完整行为请打开原页面。</p><main class="grid">"""+''.join(cards)+"""</main><script>document.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('article').forEach(a=>a.style.width=b.dataset.width+'px');document.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)))}))</script></html>""",encoding='utf-8')
    return output

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True,type=Path);p.add_argument('candidates',nargs='+',type=Path);a=p.parse_args()
    try:print(build(a.output,a.candidates))
    except (ValueError,OSError) as e:p.error(str(e))
if __name__=='__main__':main()
