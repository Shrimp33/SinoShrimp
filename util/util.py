command = input("Enter a command for SinoShrimp/util.py: ")
# format text
def format(text):
    # Replace tabs with "\t"
    text = text.replace("\t", "\\t")
    return text

if command == "format":
    # Format text
    text = input("Enter path to format: ")
    with open(text, "r") as f:
        contents = f.read()
    contents = format(contents)
    # Write formatted text at the same path but with .formatted appended
    with open(text + ".formatted", "w") as f:
        f.write(contents)
    print("Formatted text.")