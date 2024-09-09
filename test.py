#!/usr/bin/env python

# Copyright 2018-2020 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import nbconvert

with open("assignment4.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)


with open("assignment4.py", "w") as f:
    f.write(python_file)

from assignment4 import *

class TestSolution(unittest.TestCase):

    def test_pentadiagonal(self):

        assert pentadiagonal(2, 3) == [[2, -1, -1, 0, 0, 0],
                                      [-1, 2, 0, -1, 0, 0],
                                      [-1, 0, 3, -1, -1, 0],
                                      [0, -1, -1, 3, 0, -1],
                                      [0, 0, -1, 0, 2, -1],
                                      [0, 0, 0, -1, -1, 2]]

if __name__ == '__main__':
    unittest.main()
