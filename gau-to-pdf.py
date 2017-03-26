import glob, os
import fnmatch

from PyPDF2 import PdfFileMerger, PdfFileReader

# dirpath = raw_input()
dirpath='./'
outdir=dirpath+'/pdf/'
print "Converting *.gau files to .swf..."
for filename in glob.iglob(os.path.join(dirpath, '*.gau')):
    os.rename(filename, filename[:-4] + '.swf')
print "Conversion complete..."

if not os.path.exists(outdir):
    os.makedirs(outdir)

print "Converting to .swf files to .pdf"
for i in xrange(len(fnmatch.filter(os.listdir(dirpath), '*.swf'))):
    os.system("./gfx2gfx %s.swf -o pdf/page_%s.pdf" % (i+1,i+1))

merger = PdfFileMerger()
for filename in glob.iglob(os.path.join(outdir, '*.pdf')):
    merger.append(PdfFileReader(file(filename, 'rb')))

merger.write("document-output.pdf")
