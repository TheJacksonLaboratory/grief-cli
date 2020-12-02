#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import hashing

from local import read_cache


def search_all(queries: tuple, skip_local=False, skip_remote=False, **kwargs) -> None:
    results = {}
    for query in queries:
        if not skip_local:
            results.update(**search_local(query, **kwargs))

        if not skip_remote:
            results.update(**search_remote(query, **kwargs))
    return results



def search_local(query, **kwargs) -> dict:
    matches = {}
    cache = read_cache()
    for document in cache:
        is_match = False
        sha256 = document.sha256

        # implement matching logic here
        if hashing.hashes_are_same(query, sha256):
            is_match |= True
        # is query a hash? does it match this hash?
        # is query have spaces? then search asset name and asset description?
        # go through all kwargs

        if is_match:
            matches[sha256] = document
    return matches


def search_remote(query, **kwargs) -> dict:
    raise NotImplementedError("Haven't designed the remote server yet")

def list_search_results(results: dict, query=None) -> None:
    if not results:
        print(f"No assets found matching \'{' '.join(query) if query is not None else None}\'")
    else:
        for result in results.values():
            print(result)
