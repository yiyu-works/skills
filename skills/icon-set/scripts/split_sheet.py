#!/usr/bin/env python3
"""Split an evenly sized raster grid. Does not remove backgrounds."""
import argparse,json,re
from pathlib import Path

def split(source,names,output,rows,cols):
    from PIL import Image
    if rows<1 or cols<1:raise ValueError('Rows and columns must be positive')
    if not isinstance(names,list) or len(names)!=rows*cols or any(not isinstance(n,str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',n) for n in names):
        raise ValueError('Provide one safe lowercase name for each cell')
    if len(set(names))!=len(names):raise ValueError('Names must be unique')
    output=Path(output)
    with Image.open(source) as original:
        image=original.convert('RGBA')
        w,h=image.size
        if w%cols or h%rows:raise ValueError('Image dimensions must be divisible by grid dimensions')
        targets=[output/(n+'.png') for n in names]
        if any(p.exists() for p in targets) or (output/'manifest.json').exists():raise ValueError('Refusing to overwrite existing outputs')
        output.mkdir(parents=True,exist_ok=True)
        cw,ch=w//cols,h//rows
        for i,path in enumerate(targets):
            x,y=(i%cols)*cw,(i//cols)*ch
            image.crop((x,y,x+cw,y+ch)).save(path)
        report={'source':str(source),'rows':rows,'cols':cols,'cell_size':[cw,ch],'files':[p.name for p in targets], 'background_removed':False}
        (output/'manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        return report

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('image',type=Path);p.add_argument('names',type=Path);p.add_argument('output',type=Path);p.add_argument('--rows',type=int,required=True);p.add_argument('--cols',type=int,required=True);a=p.parse_args()
    try: print(json.dumps(split(a.image,json.loads(a.names.read_text()),a.output,a.rows,a.cols),ensure_ascii=False,indent=2))
    except (OSError,ValueError,ImportError) as e:p.error(str(e))
if __name__=='__main__':main()
