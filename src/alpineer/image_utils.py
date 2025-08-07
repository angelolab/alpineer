import pathlib
from typing import Dict, Union

import imageio.v3 as iio
import numpy as np


def save_image(
    fname: Union[str, pathlib.Path], data: np.ndarray, compression_level: int = 6
) -> None:
    """
    A thin wrapper around `imageio.v3.imwrite()`.

    Args:
        fname (str): The location to save the tiff file.
        data (np.ndarray): The Numpy array to save.
        compression_level (int, optional): The compression level for imageio.v3.imwrite. Increasing
            `compress` increases memory consumption, decreases compression speed and moderately
            increases compression ratio. The range of compress is `[1,9]`. Defaults to 6.
    """
    iio.imwrite(
        uri=fname,
        image=data,
        plugin="tifffile",
        compression="zlib",
        compressionargs={"level": compression_level},
    )
