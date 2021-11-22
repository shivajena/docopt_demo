# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> [<arg_op>] --arg2=<arg2> [--arg3=<arg3>]
Options:
<arg>             Takes any value (this is a required positional argument)
[<arg_op>]        Takes any value (this is an optional positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
""" 

from docopt import docopt
opt = docopt(__doc__)
def main(var):
    print(var)
    print(type(var))
    print(var["<arg_op>"])
    
if __name__ == "__main__":
    main(opt)
