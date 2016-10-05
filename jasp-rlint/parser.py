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

import constants

from utils import count_chars_in_line

def parse_source_file(filepath):
    """
    Function returns the errors and warnings if the R file does not follow the
    jasp R style guide

    Args:
        filepath: the R file absolute path

    Return:
        dictionary:
            errors: a list containing tuples - [line_number, error_message]
            warnings: a list containing tuples - [line_number, warning_message]
    """

    errors = []
    warnings = []

    # open file in read mode
    file_object = open(filepath, 'r')

    # check if file open is successful
    if file_object is None:
        print("file open failed")

    # read the entire file
    file_content = file_object.readlines()

    line_number = 0
    for line in file_content:
        line_number = line_number + 1
        char_count = count_chars_in_line(line)
        line_length = char_count["length"]

        if line_length > constants.MAX_LINE_LENGTH:
            errors.append((line_number,
                            constants.ERROR_MESSAGES["gt_max_line_length"])
                        )

        number_of_tabs = char_count["tabs"]

    # response object
    response = {
        "errors": errors,
        "warnings": warnings
    }

    return response
