#
# Copyright (C) 2016 University of Amsterdam
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

def get_file_path(filename):
    """
    Returns the absolute path of the filename

    Args:
        filename: the R file to be parsed

    Return:
        string - which is the absolute file path
    """

    filepath = _get_absolute_file_path() + '/' + filename

    return filepath

def _get_absolute_file_path():
    """

    """
    # FIXME: get the absolute file path; currently hardcoded
    return ".."

def count_chars_in_line(line):
    """
    counts the characters and tabs in the given line

    Args:
        line: the current line being parsed (as string)

    Return:
        dictionary:
            tabs: number of tabs at the beginning of the line
            length: line length
    """

    line_length = len(line)

    # ignore the last newline character
    if line[line_length - 1] == '\n':
        line_length = line_length - 1

    # count number of tabs
    tabs = 0
    index = 0
    while line[index] == '\t':
        index = index + 1
        tabs = tabs + 1

    response = {
        "tabs": tabs,
        "length": line_length
    }

    return response
