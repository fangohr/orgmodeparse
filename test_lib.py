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
    for i in range(len(sec)):
        assert type(sec[i]) == str


def test_find_sections2():
    test_string = """no section
"""
    sec = l.sections_split(test_string)

    assert len(sec) == 1
    assert sec[0] == "no section"
    assert type(sec[0]) == str

def test_find_sections3():
    test_string = """* One section
"""
    sec = l.sections_split(test_string)

    assert len(sec) == 1
    assert sec[0] == "* One section"
    assert type(sec[0]) == str
    print(sec)

def test_find_sections_empty():
    assert l.sections_split("") == []
