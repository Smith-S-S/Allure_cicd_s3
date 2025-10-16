import allure
from calculator_app import RealCalculator
import pytest

def test_type_55_pass():
    calc = RealCalculator()
    calc.open()
    try:
        calc.type_input(5)
        calc.type_input(100)  # This should raise ValueError
        assert False, "Expected ValueError not raised for input 100"
    except ValueError as e:
        print(f"Caught expected exception: {e}")
        raise
    finally:
        calc.close()
        # Attach the execution video to Allure report
        allure.attach.file(
            "test_run_video.mp4",
            name="Execution Video",
            attachment_type=allure.attachment_type.MP4
        )
