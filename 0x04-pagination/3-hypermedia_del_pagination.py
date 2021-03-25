#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''Returns a dictionary of pagination thing-a-ma-jigs'''
        # wrapper dictionary
        ret: Dict = {}
        # actual data payload
        data_payload: List[Any] = []
        # validate index range
        assert index >= 0 and index <= len(self.__dataset)
        # assign dict key values
        ret["index"] = index
        # initialize counter
        i: int = index
        # aggegate data with while loop from the inidcated page
        while len(data_payload) < page_size:
            # get line info from indexed data set, if exists
            line_no = self.__indexed_dataset.get(i)
            if line_no:
                data_payload.append(line_no)
            else:
                index += 1
            i += 1
        # assign the easy kv pairs.
        ret["next_index"] = index + page_size
        ret["page_size"] = page_size
        ret["data"] = data_payload
        return ret
