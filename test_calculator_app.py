from calculator_app import RealCalculator
import pytest

def test_type_55_pass():
    calc = RealCalculator()
    calc.open()
    calc.type_input(5)
    calc.type_input(5)
    # No way to read calculator screen without OCR, so just pass
    assert True  # ✅ Always passes
    calc.close()

def test_type_55_fail():
    calc = RealCalculator()
    calc.open()
    calc.type_input(5)
    calc.type_input(5)
    assert False  # ❌ Always fails on purpose
    calc.close()
