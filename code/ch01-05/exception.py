class EmptyFileError(Exception):     #1
    pass
filenames = ["myfile1", "nonExistent", "emptyFile", "myfile2"]
for file in filenames:
    try:                             #2
        f = open(file, 'r')
        line = f.readline()          #3
        if line == "":
            f.close()
            raise EmptyFileError("%s: is empty" % file)      #4
    except IOError as error:
        print("%s: could not be opened: %s" % (file, error.strerror))
    except EmptyFileError as error:
        print(error)
    else:                             #5
        print("%s: %s" % (file, f.readline()))
    finally:
        print("Done processing", file)                       #6
