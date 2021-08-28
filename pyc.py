import dis,marshal,argparse
parse = argparse.ArgumentParser(description="PYC FILE NAME")
parse.add_argument('FILE_NAME' , type=str , help="Plz input the filename")
args = parse.parse_args()
FILE_NAME = args.FILE_NAME
f = open(FILE_NAME , "rb").read()[16:]
dis.dis(marshal.loads(f))