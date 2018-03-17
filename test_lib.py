import orgmodeparse as l

def test_find_sections():
    test_string = """Header

* Section 1
bla bla
** Subsection 1.1
** Subsection 1.2
Text section 1.2

* Section 2
Text Section 2
* Section 3
* Section 4
*** SubSubsection"""
    sec = l.sections_split(test_string)

    assert len(sec) == 8
    assert type(sec[0]) == str
