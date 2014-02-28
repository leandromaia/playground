from sys import argv
import os, re
from glob import glob

def mv(src, dest):
    print "Renaming file ..."
    print 'mv "%s" "%s"' % (src, dest)
    os.rename(src, dest)

script, dir, videoExtension = argv

vid_files = sorted(glob(os.path.join(dir, '*'+videoExtension)))
sub_files = sorted(glob(os.path.join(dir, '*.srt')))

assert len(sub_files) == len(vid_files), "lists of different lengths"

for vidf, subf in zip(vid_files, sub_files):
    new_vidf = re.sub(r'\.srt$', videoExtension, subf)

    if vidf == new_vidf:        
        print '%s OK' % ( vidf, )
        continue
    print new_vidf
    mv(vidf, new_vidf)
