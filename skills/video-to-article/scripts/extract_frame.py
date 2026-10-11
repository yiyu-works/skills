#!/usr/bin/env python3
"""Extract one local video frame without overwriting an existing output."""
import argparse, math, shutil, subprocess, tempfile
from pathlib import Path

def extract(video,seconds,output):
    video=Path(video).resolve();output=Path(output).resolve()
    if not math.isfinite(seconds) or seconds<0:raise ValueError('Time must be finite and nonnegative')
    if not video.is_file():raise ValueError('Video does not exist')
    if output.exists():raise ValueError('Output already exists')
    if output.suffix.lower() not in ('.png','.jpg','.jpeg'):raise ValueError('Output must be PNG or JPEG')
    ffmpeg=shutil.which('ffmpeg')
    if not ffmpeg:raise ValueError('FFmpeg is required')
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='yiyu-frame-') as tmp:
        frame=Path(tmp)/('frame'+output.suffix.lower())
        subprocess.run([ffmpeg,'-hide_banner','-loglevel','error','-nostdin','-i',str(video),'-ss',str(seconds),'-frames:v','1',str(frame)],check=True,timeout=120)
        if not frame.is_file() or frame.stat().st_size==0:raise ValueError('No frame at that timestamp')
        with output.open('xb') as out,frame.open('rb') as source:shutil.copyfileobj(source,out)
    return output

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('video',type=Path);p.add_argument('seconds',type=float);p.add_argument('output',type=Path);a=p.parse_args()
    try:print(extract(a.video,a.seconds,a.output))
    except (ValueError,OSError,subprocess.SubprocessError) as e:p.error(str(e))
if __name__=='__main__':main()
