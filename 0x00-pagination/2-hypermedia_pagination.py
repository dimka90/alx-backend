#!/usr/bin/env python3

"""
This script defines a function to calculate the start and end indices
for paginating a dataset.
"""
import csv
import math
from typing import Tuple, List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the appropriate page of the dataset.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            List[List]: The paginated dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)

        dataset_length = len(self.dataset())

        if start_index >= dataset_length:
            return []
        return self.dataset()[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary containing hypermedia information for the dataset.

        Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

        Returns:
        dict: A dictionary containing hypermedia information.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.get_page(page, page_size)
        dataset_length = len(self.dataset())
        # Total number of pages
        total_pages = math.ceil(dataset_length/page_size)
        current_page = page
        if total_pages > current_page:
            next_page = current_page + 1
        else:
            next_page = None
        if current_page > 1:
            previous_page = current_page - 1
        else:
            previous_page = None
        data_set = self.dataset()
        return {
            "page_size": len(data),
            "page": current_page,
            "data": data,
            "next_page": next_page,
            "prev_page": previous_page,
            "total_pages": total_pages
            }
