##
##  Copyright (c) 2023 Chakib Ben Ziane <contact@blob42.xyz> . All rights reserved.
##
##  SPDX-License-Identifier: AGPL-3.0-or-later
##
##  This file is part of NeuronCLI.
## 
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU Affero General Public License as
##  published by the Free Software Foundation, either version 3 of the
##  License, or (at your option) any later version.
## 
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU Affero General Public License for more details.
## 
##  You should have received a copy of the GNU Affero General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
"""Strategy type definition and helper class."""

from typing import Callable, Generic, TypeVar

S = TypeVar("S")

# type for a predicate
TPredicate = Callable[[str], bool]
TParser = Callable[[str], S]

class Strategy(Generic[S]):
    def __init__(self,
                 parser: TParser[S],
                 predicate: TPredicate,
                 name: str | None = None):
        assert callable(parser), "first argument <parser> must be callable"
        self.parser = parser
        assert callable(predicate), "second argument <predicate> must be callable"
        self.predicate = predicate
        self.name = name

    def __repr__(self):
        if self.name is None:
            return f"Strategy(parser={self.parser}, predicate={self.predicate})"
        return f"Strategy[{self.name}](parser={self.parser}, predicate={self.predicate})"

    def __getitem__(self, index):
        if index == 0:
            return self.parser
        elif index == 1:
            return self.predicate
        else:
            raise IndexError("tuple index out of range")

    def __iter__(self):
        yield self.parser
        yield self.predicate
