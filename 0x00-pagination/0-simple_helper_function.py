#!/usr/bin/env python3

"""
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the start and end indices for a given page
    and page size.

    Args:
        page (int): The page number.
        page_size (int): The size of each page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices
    """

    start_page = (page - 1) * page_size
    end_page = start_page + page_size

    return (start_page, end_page)
