#!/usr/bin/env python3
"""
    file: 1-simple_pagination.py
    Author: Yaekob Demisse
    CreationDate: Feb 18 2023
"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def index_range(self, page, page_size):
        """
            returns a tuple of size two containing a start index and an
            end index corresponding to the range of indexes to return in
            a list for the those particular pagination parameters
        """
        return ((page * page_size - page_size), (page * page_size))

    def dataset(self) -> List[List]:
        """Cached dataset
        """

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """a function that implements  pagination on huge dataset
        """

        condtion1 = type(page) == int and page > 0
        condtion2 = type(page_size) == int and page_size > 0

        if not (condtion1 and condtion2):
            raise AssertionError

        index = self.index_range(page, page_size)

        return self.dataset()[(index[0]):(index[1])]
