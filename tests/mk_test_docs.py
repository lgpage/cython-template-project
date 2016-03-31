#!/usr/bin/env python
# encoding: utf-8
# filename: mk_test_docs.py

import os

FILE_HEADER = """\
#!/usr/bin/env python
# encoding: utf-8
# filename: test_docs.py
# !!! THIS FILE WAS AUTOMATICALLY GENERATED... DO NOT EDIT !!!

import doctest

"""


def main():
    extensions = []
    excude_files = ['__init__.so']
    for root, _, files in os.walk('proj'):
        for file_ in files:
            if file_ in excude_files:
                continue

            file_ = os.path.join(root, file_)
            filepath, ext = os.path.splitext(file_)
            if ext == '.so':
                path, filename = os.path.split(filepath)
                extensions.append( (path.replace('/', '.'), filename) )

    file_ = os.path.join(os.path.abspath('tests'), 'test_docs.txt')
    with open(file_, 'r') as fobj:
        stub = fobj.read()

    file_ = os.path.join(os.path.abspath('tests'), 'test_docs.py')
    if os.path.exists(file_):
        os.remove(file_)

    with open(file_, 'a') as fobj:
        fobj.write(FILE_HEADER)
        for path, module in extensions:
            fmtr = {'import_path': path, 'module_name': module}
            fobj.write("\n")
            fobj.write(stub.format(**fmtr))


if __name__ == "__main__":
    main()
