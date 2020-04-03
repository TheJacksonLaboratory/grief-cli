#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml
from pathlib import Path

import hashing

CACHE_DIR = Path(
    os.environ.get("XDG_CACHE_HOME", "~/.cache")
).expanduser() / "grief"
if not CACHE_DIR.exists():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DB = CACHE_DIR / "db.yaml"
CACHE_DB.touch()


def read_cache():
    with open(CACHE_DB, "r") as buff:
        return list(yaml.load_all(buff, Loader=yaml.FullLoader))

def write_cache(cache):
    with open(CACHE_DB, "w") as buff:
        yaml.dump_all(cache, stream=buff, explicit_start=True)


def add_to_cache(hash_l, asset):
    cache = read_cache()
    document = dict(
        sha256=hash_l,
        sha256_short=hashing.shorten(hash_l),
        name=asset,
    )
    cache.append(document)
    write_cache(cache)


def list_cache():
    cache = read_cache()
    print_fmt = f"{{sha256_short:<{hashing.SHORT_HASH_LENGTH+1}}}  {{asset_name}}"
    print(print_fmt.format(**dict(sha256_short="SHA256", asset_name="Asset Name")))
    print(print_fmt.format(**dict(sha256_short="------", asset_name="----------")))
    for document in cache:
        print(print_fmt.format(**document))
    print()

    

def clean_cache(verbose=False):
    to_remove = filter(
        Path.is_file,  
        filter(lambda p: str(p).startswith("sha"), CACHE_DIR.iterdir())
    )
    for fname in to_remove:
        print(f"rm {fname}")
        os.remove(fname)

