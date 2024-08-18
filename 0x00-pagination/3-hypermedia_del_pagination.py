#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in
                                      range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Deletion-resilient hypermedia pagination.

        Args:
            index (int): The current start index for pagination.
            page_size (int): The number of items to include on each page.

        Returns:
            Dict: A dictionary containing the index,
            next index, page size, and data.
        """
        idx_dataset = self.indexed_dataset()

        assert isinstance(index, int) and index >= 0 \
            and index < len(idx_dataset), \
            "Index must be a valid integer within the dataset range."

        i, mv, data = 0, index, []
        while i < page_size and mv < len(idx_dataset):
            value = idx_dataset.get(mv, None)
            if value:
                data.append(value)
                i += 1
            mv += 1

        next_index = mv if mv < len(idx_dataset) else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
