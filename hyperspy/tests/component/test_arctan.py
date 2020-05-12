# -*- coding: utf-8 -*-
# Copyright 2007-2020 The HyperSpy developers
#
# This file is part of  HyperSpy.
#
#  HyperSpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#  HyperSpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with  HyperSpy.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
from numpy.testing import assert_allclose
import pytest

from hyperspy.components1d import Arctan
from hyperspy.components1d import EELSArctan
from hyperspy.signals import Signal1D


def test_function1():
    g = Arctan(minimum_at_zero=False)
    g.A.value = 10
    g.k.value = 2
    g.x0.value = 1
    assert_allclose(g.function(0), -11.07148718)
    assert_allclose(g.function(1), 0)
    assert_allclose(g.function(1e4), 10*np.pi/2,1e-4)

def test_function2():
    g = EELSArctan()
    g.A.value = 10
    g.k.value = 2
    g.x0.value = 1
    assert_allclose(g.function(0), 4.63647609)
    assert_allclose(g.function(1), 10*np.pi/2)
    assert_allclose(g.function(1e4), 10*np.pi,1e-4)

# Legacy test
def test_function3():
    g = Arctan(minimum_at_zero=True)
    g.A.value = 10
    g.k.value = 2
    g.x0.value = 1
    assert_allclose(g.function(0), 4.63647609)
    assert_allclose(g.function(1), 10*np.pi/2)
    assert_allclose(g.function(1e4), 10*np.pi,1e-4)
