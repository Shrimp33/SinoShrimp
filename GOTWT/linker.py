# Linker for implanting html into a template
# Usage python linker.py <inputfile> <outputfile>
# Example python linker.py input.html output.html

TEMPLATE = r"GOTWT\base.ref.html" # Path of template file

import sys

def rule(template, dump):  # Rules, just add more rules here
    # First time of dump is title
    title = open(dump, "r", encoding='utf-8').read().splitlines()[0].strip()
    # Strip html tags
    # print(title.find(">"),title[title.find("<") + 1:].find("<"))
    name = title[title.find(">") + 1:title[title.find("<") + 1:].find("<")].strip()
    # print(name)
    # Get # of chapter
    index = name[name.find("Chapther") + 9: name.find(":")].strip()
    # Others are content
    content = open(dump, "r", encoding='utf-8').read().splitlines()[1:]
    # Replace title
    template = template.replace("{{ChapterName}}", title)
    # Replace name
    template = template.replace("{{ChapterNameNoTags}}", name)
    # Replace index
    template = template.replace("{{index}}", index)
    # Replace content
    template = template.replace("{{ChapterText}}", "".join(content))
    return template

def main():
    # Get input and output file paths
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    # print("Input file: " + inputfile)
    # print("Output file: " + outputfile)
    # Read Template
    template = open(TEMPLATE, "r", encoding='utf-8').read()
    # Remove lines that start with // from template
    template = "".join([line for line in template.splitlines(True) if not line.strip().startswith("//")])
    # Rule
    template = rule(template, inputfile)
    # Write to output file
    with open(outputfile, "w", encoding='utf-8') as f:
        f.write(template)
    print("Done.")

if __name__ == "__main__":
    main()
