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

def parse_source_file(file_content):
    """
    Function returns the errors and warnings if the R file does not follow the
    jasp R style guide

    Args:
        file_content: the R file content as string

    Return:
        dictionary:
            errors: a list containing tuples - [line_number, error_message]
            warnings: a list containing tuples - [line_number, warning_message]
    """


    # response object
    response = {}
    response["errors"] = []
    response["warnings"] = []

    return response
