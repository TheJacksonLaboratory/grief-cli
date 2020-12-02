#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashing


class Asset:
    print_fmt = f"{{sha256_short:<{hashing.SHORT_HASH_LENGTH+1}}}  {{asset_name}}  {{is_cached}}"

    def __init__(self, asset_name, asset_uri, **kwargs):
        """
        minimal metadata required:
        - asset_name
        - asset_uri
        """
        self.name = asset_name
        self.uri = asset_uri
        self.sha256 = hashing.get_hash(asset_uri)
        self.sha256_short = hashing.shorten(self.sha256)
        self.local_filename = f"sha{self.sha256}"
        self.local_path = None
        self.is_cached = False

    def __repr__(self) -> None:
        print(self.print_fmt.format(self.__dict__))

    def __eq__(self, other: Asset) -> bool:
        return hashing.hashes_are_same(self.sha256, other.sha256)
