#!/usr/bin/env python3
"""Parse SRT/VTT captions to JSON seconds and text; does not transcribe."""
import argparse,html,json,re
from pathlib import Path
STAMP=r'(?:\d{2,}:)?\d{2}:\d{2}[,.]\d{3}'

def seconds(s):
    parts=s.replace(',','.').split(':')
    if len(parts)==2:parts.insert(0,'0')
    h,m,sec=int(parts[0]),int(parts[1]),float(parts[2])
    if m>=60 or sec>=60:raise ValueError('Invalid timestamp: '+s)
    return h*3600+m*60+sec

def parse(text):
    text=text.lstrip('\ufeff').replace('\r\n','\n').replace('\r','\n')
    cues=[]
    for block in re.split(r'\n\s*\n',text.strip()):
        lines=block.splitlines()
        if not lines or lines[0].startswith(('WEBVTT','NOTE','STYLE','REGION')):continue
        pos=next((i for i,l in enumerate(lines) if '-->' in l),None)
        if pos is None:continue
        match=re.fullmatch(r'\s*('+STAMP+r')\s*-->\s*('+STAMP+r')(?:\s+[^\n]*)?\s*',lines[pos])
        if not match:raise ValueError('Invalid timing line: '+lines[pos])
        start,end=map(seconds,match.groups())
        if end<=start:raise ValueError('Cue end must follow start')
        content=' '.join(lines[pos+1:])
        content=html.unescape(re.sub(r'<[^>]*>','',content)).strip()
        if content:cues.append({'start':start,'end':end,'text':content})
    if not cues:raise ValueError('No subtitle cues found')
    if any(cues[i]['start']<cues[i-1]['start'] for i in range(1,len(cues))):raise ValueError('Cues must be ordered by start time')
    return cues

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('subtitles',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
    try:
        result=json.dumps(parse(a.subtitles.read_text(encoding='utf-8-sig')),ensure_ascii=False,indent=2)+'\n'
        if a.output:
            a.output.parent.mkdir(parents=True,exist_ok=True)
            with a.output.open('x',encoding='utf-8') as f:f.write(result)
        else:print(result,end='')
    except (OSError,ValueError) as e:p.error(str(e))
if __name__=='__main__':main()
