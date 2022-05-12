#!/usr/bin/env bash
#
# Copyright (C) 2022 The Event Horizon Telescope Collaboration
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

echo "Converting Stokes-I only uvfits files to txt and csv files"

for f in uvfits*/*.uvfits; do
    f=${f#uvfits}
    f=${f%.uvfits}
    p=${f%/*}

    txt${p}/dump_txt.py uvfits${f}.uvfits txt${f}.txt
    csv${p}/dump_csv.py txt${f}.txt       csv${f}.csv
done
