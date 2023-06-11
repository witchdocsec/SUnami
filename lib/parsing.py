import argparse
def parser():
	parser=argparse.ArgumentParser(description="sunami argument parser")
	parser.add_argument("-local", choices=["1","0"], default="0")
	subparse=parser.add_subparsers(dest="command")

	genshellparser=subparse.add_parser("genshell")
	genshellparser.add_argument("--ip")
	genshellparser.add_argument("--port")
	genshellparser.add_argument("-shell", default="/bin/bash")
	genshellparser.add_argument("-protocol", default="tcp")
	genshellparser.add_argument("-listen", choices=["1","0"], default="0")

	exfilfileparser=subparse.add_parser("exfilfile")
	exfilfileparser.add_argument("--file")
	exfilfileparser.add_argument("--method", choices=["postflask","nc","pysocket"])
	exfilfileparser.add_argument("--ip")
	exfilfileparser.add_argument("--port")
	args = parser.parse_args()
	return args