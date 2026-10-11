import importlib.util
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def module(skill,script):
    path=ROOT/'skills'/skill/'scripts'/script
    spec=importlib.util.spec_from_file_location(skill.replace('-','_')+'_'+script.replace('.','_'),path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

class Links(unittest.TestCase):
    def test_relative_encoded_fragment_missing_and_escape(self):
        check=module('readme-polish','check_links.py').check
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'a b.md').write_text('ok')
            readme=p/'README.md';readme.write_text('[valid](a%20b.md#heading)\n[x](missing.md)\n[x](../outside.md)\n[remote](https://example.com)\n```md\n[x](code-only.md)\n```')
            problems=check(readme,p)
            self.assertEqual([x['reason'] for x in problems],['missing local path','outside repository'])

class Compare(unittest.TestCase):
    def test_escaping_containment_and_overwrite(self):
        build=module('ui-design','compare.py').build
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);source=p/'a & b.html';source.write_text('<h1>A</h1>')
            out=p/'compare.html';build(out,[source]);text=out.read_text()
            self.assertIn('a &amp; b',text);self.assertIn('a%20%26%20b.html',text)
            self.assertIn('sandbox="allow-scripts"',text)
            with self.assertRaises(ValueError):build(out,[source])
            with self.assertRaises(ValueError):build(p/'nested'/'compare.html',[source])

class Subtitles(unittest.TestCase):
    def test_srt_and_vtt_match(self):
        parse=module('video-to-article','parse_subtitles.py').parse
        inputs=ROOT/'examples/video-to-article/input'
        srt=parse((inputs/'demo.srt').read_text());vtt=parse((inputs/'demo.vtt').read_text())
        self.assertEqual(srt,vtt);self.assertEqual(srt[1]['end'],4.5)
    def test_multiline_bom_settings_and_entities(self):
        parse=module('video-to-article','parse_subtitles.py').parse
        result=parse('\ufeffWEBVTT\n\nNOTE omitted\nthis is a note\n\ncue-a\n01:02.125 --> 01:04.000 align:start\n<b>A &amp; B</b>\nnext line')
        self.assertEqual(result,[{'start':62.125,'end':64.0,'text':'A & B next line'}])
    def test_invalid_timestamps_and_reverse_cues(self):
        parse=module('video-to-article','parse_subtitles.py').parse
        for text in ['1\n00:00:62,000 --> 00:01:03,000\nA','1\n00:00:03,000 --> 00:00:02,000\nA','not subtitles','1\n00:00:03,000 --> 00:00:04,000\nA\n\n2\n00:00:01,000 --> 00:00:02,000\nB']:
            with self.assertRaises(ValueError):parse(text)

class Icons(unittest.TestCase):
    def test_pixels_names_grid_and_no_overwrite(self):
        from PIL import Image
        split=module('icon-set','split_sheet.py').split
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);source=p/'sheet.png';image=Image.new('RGBA',(40,20),(255,0,0,255))
            image.paste((0,0,255,128),(20,0,40,20));image.save(source)
            report=split(source,['red','blue'],p/'out',1,2)
            self.assertEqual(report['cell_size'],[20,20])
            with Image.open(p/'out/blue.png') as cell:self.assertEqual(cell.getpixel((5,5)),(0,0,255,128))
            with self.assertRaises(ValueError):split(source,['red','blue'],p/'out',1,2)
            for names,rows,cols in [(['../bad','ok'],1,2),(['same','same'],1,2),(['one'],1,2),(['a','b','c'],1,3)]:
                with self.assertRaises(ValueError):split(source,names,p/'bad',rows,cols)

class Frames(unittest.TestCase):
    @unittest.skipUnless(shutil.which('ffmpeg'),'FFmpeg unavailable')
    def test_real_frame_invalid_time_and_overwrite(self):
        from PIL import Image
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);video=p/'source.mkv'
            subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-f','lavfi','-i','color=c=red:s=64x48:r=5:d=1','-c:v','ffv1',str(video)],check=True,timeout=30)
            for name in ['cover-maker','video-to-article']:
                extract=module(name,'extract_frame.py').extract
                out=p/(name+'.png');extract(video,.2,out)
                with Image.open(out) as image:self.assertEqual(image.size,(64,48))
                with self.assertRaises(ValueError):extract(video,.2,out)
                for time in [-1,float('nan'),float('inf'),10]:
                    with self.assertRaises(ValueError):extract(video,time,p/(name+'-invalid.png'))

if __name__=='__main__':unittest.main()
