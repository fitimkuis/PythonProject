#!/usr/bin/env python3

# pytest -m a marking.py
# pytest -m b marking.py

import pytest

@pytest.mark.a
def test_a1():

    assert (1) == (1)

@pytest.mark.a
def test_a2():

    assert (1, 2) == (1, 2)

@pytest.mark.a
def test_a3():

    assert (1, 2, 3) == (1, 2, 3)

@pytest.mark.b
def test_b1():

    assert "falcon" == "fal" + "con"

@pytest.mark.b
def test_b2():

    assert "falcon" == f"fal{'con'}"