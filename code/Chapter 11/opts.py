from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("indent", type=int, help="indent for report")  
    parser.add_argument("input_file", help="read data from this file")  #1
    parser.add_argument("-f", "--file", dest="filename",             #2
                  help="write report to FILE", metavar="FILE")
    parser.add_argument("-x", "--xray", 
                  help="specify xray strength factor")
    parser.add_argument("-q", "--quiet",
                  action="store_false", dest="verbose", default=True, #3
                  help="don't print status messages to stdout")

    args = parser.parse_args()

    print("arguments:", args)
if __name__ == "__main__":
    main()
