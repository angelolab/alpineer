import os
from typing import Any, List, Optional

import matplotlib.pyplot as plt
import numpy as np


def save_figure(save_dir, save_file: str, dpi: Optional[float] = 300) -> None:
    """Saves the figure in a directory.

    Args:
        save_dir (str): the name of the directory we wish to save to.
        save_file (str): The file we wish to save to
        dpi (float, optional): The pixel density of the figure. Defaults to 300.

    Raises:
        FileNotFoundError: The save directory does not exist.
        FileNotFoundError: The save file specified does not exist.
    """
    # verify save_dir exists
    if not os.path.exists(save_dir):
        raise FileNotFoundError("save_dir %s does not exist" % save_dir)

    # verify that if save_dir specified, save_file must also be specified
    if save_file is None:
        raise FileNotFoundError("save_dir specified but no save_file specified")

    plt.savefig(os.path.join(save_dir, save_file), dpi=dpi)


def create_invalid_data_str(invalid_data: List[str]) -> str:
    """Creates a easy to read string for ValueError statements.

    Args:
        invalid_data (list[str]): A list of strings containing the invalid / missing data

    Returns:
        str: Returns a formatted string for more detailed ValueError outputs.
    """
    # Holder for the error string
    err_str_data = ""

    # Adding up to 10 invalid values to the err_str_data.
    for idx, data in enumerate(invalid_data[:10], start=1):
        err_msg = "{idx:{fill}{align}{width}} {message}\n".format(
            idx=idx,
            message=data,
            fill=" ",
            align="<",
            width=12,
        )
        err_str_data += err_msg

    return err_str_data


def verify_in_list(**kwargs: Any) -> None:
    """Verify at least whether the values in the first list exist in the second.

    Args:
        **kwargs (list, list):
            Two lists, but will work for single elements as well.
            The first list specified will be tested to see
            if all its elements are contained in the second.

    Raises:
        ValueError: if not all values in the first list are found in the second
    """
    if len(kwargs) != 2:
        raise ValueError("You must provide 2 arguments to verify_in_list")

    test_list, good_values = kwargs.values()

    if not np.isin(test_list, good_values).all():
        test_list_name, good_values_name = kwargs.keys()
        test_list_name = test_list_name.replace("_", " ")
        good_values_name = good_values_name.replace("_", " ")

        # Calculate the difference between the `test_list` and the `good_values`
        difference = [str(val) for val in test_list if val not in good_values]

        # Only printing up to the first 10 invalid values.
        err_str = ("Displaying {} of {} invalid value(s) provided for list {:^}.\n").format(
            min(len(difference), 10), len(difference), test_list_name
        )

        err_str += create_invalid_data_str(difference)

        raise ValueError(err_str)

    print(f"All values in list {test_list_name} exist in list {good_values_name}")
    return


def verify_same_elements(**kwargs: Any) -> None:
    """Verify if two lists contain the same elements regardless of count

    Args:
        **kwargs (list, list): Two lists

    Raises:
        ValueError: if the two lists don't contain the same elements
    """
    if len(kwargs) != 2:
        raise ValueError("You must provide 2 arguments to verify_same_elements")

    list_one, list_two = kwargs.values()

    try:
        list_one_cast: List[Any] = list(list_one)
        list_two_cast: List[Any] = list(list_two)
    except TypeError as e:
        raise ValueError("Both arguments provided must be lists or list types") from e

    if not np.all(set(list_one_cast) == set(list_two_cast)):
        list_one_name, list_two_name = kwargs.keys()
        list_one_name = list_one_name.replace("_", " ")
        list_two_name = list_two_name.replace("_", " ")

        # Values in list one that are not in list two
        missing_vals_1 = [str(val) for val in (set(list_one_cast) - set(list_two_cast))]

        # Values in list two that are not in list one
        missing_vals_2 = [str(val) for val in (set(list_two_cast) - set(list_one_cast))]

        # Total missing values
        missing_vals_total = [str(val) for val in set(list_one_cast) ^ set(list_two_cast)]

        err_str = (
            "{} value(s) provided for list {:^} and list {:^} are not found in both lists.\n"
        ).format(len(missing_vals_total), list_one_name, list_two_name)

        # Only printing up to the first 10 invalid values for list one.
        err_str += ("{:>13} \n").format(
            "Displaying {} of {} missing value(s) for list {}\n".format(
                min(len(missing_vals_1), 10), len(missing_vals_2), list_one_name
            )
        )
        err_str += create_invalid_data_str(missing_vals_1) + "\n"

        # Only printing up to the first 10 invalid values for list two
        err_str += ("{:>13} \n").format(
            "Displaying {} of {} missing value(s) for list {}\n".format(
                min(len(missing_vals_2), 10), len(missing_vals_2), list_two_name
            )
        )
        err_str += create_invalid_data_str(missing_vals_2) + "\n"

        raise ValueError(err_str)

    print(f"List {list_one_name} and list {list_two_name} contain the same elements")
    return
