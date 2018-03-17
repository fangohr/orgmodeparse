#
def sections_split(string):
    """Given string 'string', return a list of strings for every new
    section, subsection, subsubsection, etc
    """
    sections = []
    this = []
    for line in string.split():
        if line[0] == '*':
            # new section starts
            ## save old section
            if this is not []:
                sections.append("\n".join(this))
            ## start new section
            this = []
            this.append(line)
        else:
            this.append(line)
    # add last section
    if this is not []:
        sections.append("\n".join(this))
    return sections
