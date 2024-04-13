import sys
def main():
    contents = sys.stdin.read()                                    #A
    sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2]))   #B
if __name__ == "__main__":
    main()
