from numpy import argmax
from bibtexparser import parse, missingfield
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("field", type=str, help="Missing field")
parser.add_argument("file", type=str, help=".bib file")
args = parser.parse_args()
with open(args.file, 'rt') as f:
    bib = f.read()
    d = parse(bib)
    missingfield(d, args.field)
