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


def test_line_parse():
    key, value = l.line_parse("#+BEGIN: clocktable :maxlevel 3")
    assert key == "#+BEGIN:"
    assert value == "clocktable :maxlevel 3"

    key, value = l.line_parse("#+END:")
    assert key == "#+END:"
    assert value == ""

def test_identify_clock_table():

    # define test string
    s = r"""
#+BEGIN: clocktable :maxlevel 3 :scope subtree
#+CAPTION: Clock summary at [2018-03-04 Sun 18:26]
| Headline                    | Time   |      |      |
|-----------------------------+--------+------+------|
| *Total time*                | *9:05* |      |      |
|-----------------------------+--------+------+------|
| \emsp Week 1                |        | 9:05 |      |
| \emsp\emsp <2018-03-01 Thu> |        |      | 4:35 |
| \emsp\emsp <2018-03-02 Fri> |        |      | 4:30 |
#+END:
"""
    tables = l.identify_tables(s)
    assert len(tables) == 1  #
    meta, output = tables
    assert meta['#+BEGIN:'] == "clocktable :maxlevel 3 :scope subtree"
    assert meta['#+CAPTION:'] == "Clock summary at [2018-03-04 Sun 18:26]"
    assert meta['#+END:'] == ""
    assert table[0:10] == "| Headlin"
    assert table[-10:] == "  | 4:30 |"

def test_parse_clock_table():
    raise NotImplementedError
