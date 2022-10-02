import re
superscriptlaw = lambda text: re.sub(r"\^([0-9]+)", r"<sup>\1</sup>", text)
tabslaw = lambda text: text.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")

def rule(text, rb):
    for law in rb:
        text = law(text)
    return text
def main(inP, rb):
    # Read the input file
    datat = []
    with open(inP, 'r') as f:
        datat = f.readlines()
    # Replace the rules
    for i, line in enumerate(datat):
        datat[i] =  f"<div id=\"contentl{i}\" class=\"contentline\"> {rule(line, rb)} </div>\n"
    # Write the output file
    with open(inP + ".html", 'w') as f:
        f.writelines(datat)
if __name__ == "__main__":
    # Read the rules
    rules = [superscriptlaw, tabslaw]
    # Read the input file
    inP = input("Enter the path to the input file: ")
    # Run the main function
    main(inP, rules)