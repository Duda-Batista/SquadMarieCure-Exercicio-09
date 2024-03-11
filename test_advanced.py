import pytest

def convert_str_to_bool(input_str):
    return input_str.strip().lower() in ['yes', 'y', '1', 'true']

@pytest.mark.parametrize("test_input", ["YES", "yes", "Y", "y", "1", "True"])
def test_convert_str_to_bool_true(test_input):
    assert convert_str_to_bool(test_input) == True

@pytest.mark.parametrize("test_input", ["NO", "no", "N", "n", "0", "False"])
def test_convert_str_to_bool_false(test_input):
    assert convert_str_to_bool(test_input) == False

def test_file_handling(tmp_path):
    test_file = tmp_path / "testfile"
    test_file.write_text("1")

    with open(test_file, "r") as file:
        content = file.read()
    
    assert content == "1"
