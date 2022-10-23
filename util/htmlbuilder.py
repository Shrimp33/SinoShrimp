# Inserts lines of txt into html divs
# Usage: python htmlbuilder.py <inputfile> <outputfile>
# Example: python htmlbuilder.py input.txt output.html
# Format of output.html: <div id="content{i}" class="contentline">line1</div>
# Format of input.txt: line1

import sys

def main():
    # Get input and output file paths
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    print("Input file: " + inputfile)
    print("Output file: " + outputfile)
    # Read input file
    with open(inputfile, "r", encoding='utf-8') as f:
        contents = f.read()
    # Split contents into lines
    lines = contents.splitlines()
    # Create output file
    with open(outputfile, "w", encoding='utf-8') as f:  # YOU NEED UTF-8 ENCODING HERE OR IT WILL BREAK EVERYTHING
        # Write each line to output file
        for i, line in enumerate(lines):
            f.write(f"""<div id="content{i}" class="contentline">{line}</div>
""")
    print("Done.")

if __name__ == "__main__":
    main()