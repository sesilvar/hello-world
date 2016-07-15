import sys
def process_file(reader):
    '''open, read, and print a file.'''
    for line in reader:
        line = line.strip()
        print line

if __name__ == "__main__":
    input_file=open(sys.argv[1],"r")
    process_file(input_file)
    input_file.close()
