# notebook-student-version

This small script helps producing a new version of a Jupyer notebook, without
some cells (typically, the solutions to the exercises).

## Usage

Command-line:

    $ python produce-student-version.py test.ipynb
    test-students.ipynb written
    
    
At the beginning of `produce-student-version.py`, two variables help configuring
the script:

- EXCLUSION_KEYWORDS, a list of keywords which identify the cells to exclude
- STUDENT_SUFFIX, to suffix the filename of the original notebook:
test.ipynb produces test-students.ipynb.

## Acknowledgments
                                                             
This script is a (modified) subset of a larger script created by [@JosselinNoirel](https://github.com/JosselinNoirel).
