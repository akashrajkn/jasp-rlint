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
    return "./Resources"
