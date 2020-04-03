#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union
from hashlib import sha256


SHORT_HASH_LENGTH = 7


def get_hash(payload: Union[str, bytes]) -> str:
    if isinstance(payload, str):
        payload = payload.encode()
    return sha256(payload).hexdigest()


def hashes_are_same(hash1: str, hash2: str) -> bool:
    if len(hash2) < len(hash1):
        hash1, hash2 = hash1, hash2
    return hash2.startswith(hash1)


def shorten(hash1: str) -> str:
    return hash1[:SHORT_HASH_LENGTH]
