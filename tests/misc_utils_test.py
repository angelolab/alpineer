import pytest

from tmi.misc_utils import create_invalid_data_str, verify_in_list, verify_same_elements


def test_verify_in_list() -> None:
    """Tests that the function `misc_utils::verify_in_list`
    behaves properly.
    """
    with pytest.raises(ValueError):
        # not passing two lists to verify_in_list
        verify_in_list(one=["not_enough"])

    with pytest.raises(ValueError):
        # value is not contained in a list of acceptable values
        verify_in_list(one="hello", two=["goodbye", "hello world"])

    with pytest.raises(ValueError):
        # not every element in a list is equal to an value
        verify_in_list(one=["goodbye", "goodbye", "hello"], two="goodbye")

    with pytest.raises(ValueError):
        # one list is not completely contained in another
        verify_in_list(one=["hello", "world"], two=["hello", "goodbye"])


def test_verify_same_elements() -> None:
    """Tests that the function `misc_utils::verify_same_elements`
    behaves properly.
    """
    with pytest.raises(ValueError):
        # not passing two lists to verify_same_elements
        verify_same_elements(one=["not_enough"])

    with pytest.raises(ValueError):
        # not passing in items that can be cast to list for either one or two
        verify_same_elements(one=1, two=2)

    with pytest.raises(ValueError):
        # the two lists provided do not contain the same elements
        verify_same_elements(one=["elem1", "elem2", "elem2"], two=["elem2", "elem2", "elem4"])


def test_create_invalid_data_str() -> None:
    """Tests that the function `misc_utils::create_invalid_data_str`
    behaves properly.
    """
    invalid_data = ["data_" + str(i) for i in range(20)]

    # Test to make sure the case of 10 invalid values creates a proper string.
    invalid_data_str1 = create_invalid_data_str(invalid_data=invalid_data[:10])
    for data in invalid_data[:10]:
        assert invalid_data_str1.find(data) != -1

    # Test to make sure cases of less than 10 invalid values creates a proper string.
    invalid_data_str2 = create_invalid_data_str(invalid_data=invalid_data[:3])
    for data in invalid_data[:3]:
        assert invalid_data_str2.find(data) != -1

    # Test to make sure cases of more than 10 invalid values creates a proper string
    # capping out at 10 values.
    invalid_data_str3 = create_invalid_data_str(invalid_data=invalid_data)
    for data in invalid_data[:10]:
        assert invalid_data_str3.find(data) != -1
