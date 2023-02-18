#!/usr/bin/env python3
"""
    file: 0-simple_helper_function.py
    Author: Yaekob Demisse
    CreationDate: Feb 18 2023
"""


def index_range(page, page_size):
    """
        returns a tuple of size two containing a start index and an
        end index corresponding to the range of indexes to return in
        a list for the those particular pagination parameters
    """
    return ((page * page_size - page_size), (page * page_size))