import argparse
import time
from io import StringIO
import os
import sys
from os.path import abspath
from amanda.compile import ama_compile
from amanda.error import handle_exception,throw_error
from amanda.bltins import bltin_objs

def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="source file to be executed")
    parser.add_argument("-g","--generate", help="Generate an output file", action = "store_true")
    parser.add_argument(
        "-o","--outname", type=str,
        help = "Name of the output file, Requires the -g option to take effect. Defaults to output.py."
    )
    parser.add_argument("-r","--report", help="Activates report mode and sends event messages to specified port on the local machine.", type=int)

    if len(args):
        args = parser.parse_args(args)
    else:
        args = parser.parse_args()
    try:
        with open(abspath(args.file), encoding="utf-8") as src_file:
            src = StringIO(src_file.read())
    except FileNotFoundError:
        print(f"The file '{abspath(args.file)}' was not found on this system")
        sys.exit()
    code,line_info = ama_compile(src)

    #Generate outfile
    out_file = "output.py"
    if args.generate:
        if args.outname:
            out_file = args.outname
        with open(out_file,"w") as output:
            output.write(code)
   
    pycode_obj = compile(code,out_file,"exec")
    try:
        #Run compiled python code
        exec(pycode_obj,bltin_objs)
    except Exception as e:
        ama_error = handle_exception(e,out_file,line_info)
        if not ama_error:
            raise e
        throw_error(ama_error,src)

if __name__ == "__main__":
    main()

