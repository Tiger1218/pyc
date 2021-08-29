import py_compile,argparse
parse = argparse.ArgumentParser(description="PY FILE NAME")
parse.add_argument('FILE_NAME' , type=str , help="Plz input the filename")
args = parse.parse_args()
FILE_NAME = args.FILE_NAME
py_compile.compile(FILE_NAME , FILE_NAME + 'c')