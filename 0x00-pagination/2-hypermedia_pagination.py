#!/usr/bin/env python3

""" creating a simple pagination """

import csv
import math
from typing import List, Dict, Union, Any


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return (self.__dataset)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get pages from dataset"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        assert page_size != 0
        self.dataset()
        start, end = index_range(page, page_size)
        return (self.__dataset[start:end])

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """get hybermedia pagination"""
        data: List[List[Any]] = self.get_page(page, page_size)
        total_pages: int = round(len(self.__dataset) / page_size)

        pagination: Dict[str, Union[int, List[List[Any]], None]] = {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": None,
                "prev_page": None,
                "total_pages": total_pages,
        }
        if page > 1:
            pagination["prev_page"] = page - 1
        if page < total_pages:
            pagination["next_page"] = page + 1
        return pagination
