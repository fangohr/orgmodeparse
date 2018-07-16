#
def sections_split(string):
    """Given string 'string', return a list of strings for every new
    section, subsection, subsubsection, etc
    """
    sections = []
    this = []
    for line in string.splitlines():
        if len(line) > 0 and line[0] == '*':
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

    # if first element is empty string, remove
    if sections[0] == '':
        sections.pop(0)

    return sections

def line_parse(s):
        """ Given "#+BEGIN: clocktable :maxlevel 3", return
        "#+BEGIN:" und "clocktable :maxlevel 3"
        """
        # has this a keyword?
        assert s[0] == "#"
        assert ":" in s
        bits = s.split(":")
        return bits[0] + ":", (":".join(bits[1:])).lstrip()


def identify_tables(s):
    """Returns list of (meta, table) items.
    Meta is a dictionary, table a string.
    Dictionary may look like this:


    [to be completed]
    """


    def new():
        return {}, ""
    tables = []


    state = "normal text"  # alternative is "in table"

    # iterate through given string
    for line in s.splitlines():
        if line[0:8] == "#+BEGIN:":
            assert state == "normal text", "Table in table?"
            state = "in table"
            meta, table = new()
            key, value = line_parse(line)
            meta[key] = value
        elif line[0:6] == "#+END:":
            assert state == "in table"
            state = "normal text"
            key, value = line_parse(line)
            meta[key] = value
            table += line
            tables.append(meta, table)
        else:
            if state == "in table":
                table += line
            elif state == "normal text":
                pass  # ignore line
            else:
                raise NotImplementedError("Internal error")
    if state == "in table":
        raise ValueError("We seem to stop in the middle of a table (#+END missing)")
    return tables
