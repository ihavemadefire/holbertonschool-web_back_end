#!/usr/bin/env python3
"""
This module creates a helper function
"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    '''simple helper function'''
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
            test page length
            open dataset file
            find indices
            return their value
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()
        a = index_range(page, page_size)[0]
        b = index_range(page, page_size)[1]
        if type(self.__dataset) is not None:
            return self.__dataset[a:b]
        else:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Returns a dict of paginated data'''
        ret: dict = {}
        page_set: List[List] = self.get_page(page, page_size)
        # set value pairs
        ret["page_size"] = len(page_result)
        ret["page"] = page
        ret["data"] = page_set
        # check length, if next then next else, none
        if (page + 1) * page_size <= len(self.__dataset):
            ret["next_page"] = page + 1
        else:
            ret["next_page"] = None
        # check length, if next then next else, none
        if (page - 1) * page_size >= 1:
            ret["prev_page"] = page - 1
        else:
            ret["prev_page"] = None
        # Divide the length of the dataset by the size of pages rounded up
        ret[total_pages] = math.ceil(len(self.__dataset) / page_size)
        return ret
