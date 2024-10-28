#!/usr/bin/env python3

""" pagination implementation """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ zero index of page """
    start_page: int = 0
    if page > 1:
        start_page = page * 10
    end_page = start_page + page_size
    return (start_page, end_page)
