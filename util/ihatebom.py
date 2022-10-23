# I just hate UTF-8 BOM

# Taken from sof https://stackoverflow.com/a/33294156
# Usage: python ihatebom.py <file>
# Example: python ihatebom.py text.txt

# Stolen code
# s = open(bom_file, mode='r', encoding='utf-8-sig').read()
# open(bom_file, mode='w', encoding='utf-8').write(s)

import sys

def main():
    # Get file path
    bom_file = sys.argv[1]
    print("File: " + bom_file)
    # Read file
    s = open(bom_file, mode='r', encoding='utf-8-sig').read()
    open(bom_file, mode='w', encoding='utf-8').write(s)
    print("Done.")

if __name__ == "__main__":
    main()