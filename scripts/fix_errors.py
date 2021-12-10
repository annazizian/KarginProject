import re
from pathlib import Path
from argparse import ArgumentParser


def parse_args(*argument_array):
    parser = ArgumentParser(
        description='Find and fix common errors in data files')
    parser.add_argument('--data-dir', help='Directory of script files')
    return parser.parse_args(*argument_array)


def main(args):
    pf, pr = r'time: "(\d+)[։:](\d+)[:։]', r'time: "\1:\2:'

    p = Path(args.data_dir)
    for path in p.rglob('*.yaml'):
        with path.open() as rfile:
            txt = rfile.read()
        repl = re.sub(pf, pr, txt)
        if repl == txt:
            print('Same for', path)
            continue
        print('Fixing', path)
        with path.open('w') as wfile:
            wfile.write(repl)

    for path in p.rglob('*.yaml'):
        with path.open() as rfile:
            txt = rfile.read()
        errors = re.findall(r"\d+:\d+:\d+[։:]", txt)
        if errors:
            print('ERROR!!! ', path, errors)


if __name__ == '__main__':
    args = parse_args()
    main(args)
