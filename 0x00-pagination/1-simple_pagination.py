#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer
arguments page and page_size.

The function should return a tuple of size two containing a
start index and an end index corresponding to the range of
indexes to return in a list for those particular pagination
parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""

from typing import Tuple, List
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for the items on the specified page.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and the end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset if it hasn't been loaded yet."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of lists containing the data
            for the requested page.
        """
        assert type(page) is int and page > 0, "Page number\
        must be a positive integer."
        assert type(page_size) is int and page_size > 0, "Page size\
        must be a positive integer."

        data = self.dataset()
        start, end = index_range(page, page_size)

        return data[start:end]
