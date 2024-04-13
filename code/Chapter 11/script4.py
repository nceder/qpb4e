import fileinput
def main():
    for line in fileinput.input():
        if not line.startswith('##'):
            print(line, end="")
if __name__ == "__main__":
    main()
