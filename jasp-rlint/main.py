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

def main(filename):
    """
    main function - entry to the parser/linter
    """
    complete_filepath = get_file_path(filename)

    # open file in read mode
    file_object = open(complete_filepath, 'r')

    # check if file open is successful
    if file_object is None:
        print("file open failed")

    # read the entire file
    file_content = file_object.read()

    parsed_file = parse_source_file(file_content)
    errors = parsed_file["errors"]
    warnings = parsed_file["warnings"]

    # print the warnings if present
    if len(warnings) >= 1:
        for warning in warnings:
            print(warning)

    # print the errors if present
    if len(errors) < 1:
        print "no errors in file"
    else:
        for error in errors:
            print(error)

if __name__ == '__main__':
    main('alpha.R')
