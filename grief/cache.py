#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml
from pathlib import Path

from asset import Asset

CACHE_DIR = Path(
    os.environ.get("XDG_CACHE_HOME", "~/.cache")
).expanduser() / "grief"
if not CACHE_DIR.exists():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DB = CACHE_DIR / "db.yaml"
CACHE_DB.touch()


class CachedAsset:
    def __init__(self, sha256: str):
        self.sha256 = sha256
        self.filename = f"sha{sha256}"
        self.filepath = CACHE_DIR / self.filename

def _from_path(filepath: Path) -> CachedAsset:
    assert filename.str.startswith("sha")
    sha256 = str(filepath.stem)[3:]
    return CachedAsset(sha256)
CachedAsset.from_path = _from_path


def _get_local_files():
    files = filter(
        Path.is_file,  
        filter(lambda p: str(p).startswith("sha"), CACHE_DIR.iterdir())
    )
    for fpath in files:
        yield CachedAsset.from_path(fpath)
    

def read_cache():
    with open(CACHE_DB, "r") as buff:
        return list(yaml.load_all(buff, Loader=yaml.FullLoader))

def write_cache(cache):
    with open(CACHE_DB, "w") as buff:
        yaml.dump_all(cache, stream=buff, explicit_start=True)

def is_asset_in_cache(asset_name):
    cache = read_cache()
    for document in cache:
        print(print_fmt.format(**document))



def add_to_cache(hash_l, asset_name, **kwargs):
    cache = read_cache()
    document = dict(
        sha256=hash_l,
        sha256_short=hashing.shorten(hash_l),
        name=asset_name,
    )
    document.update(**kwargs)
    cache.append(document)
    write_cache(cache)


def remove_from_cache(hash_l):
    cache = read_cache()
    cache = list(filter(
        lambda doc: doc.get("sha256") != hash_l,
        cache
    ))
    write_cache(cache)
    validate_cache()


def validate_cache():
    cache = read_cache()
    cache_hashes = dict((doc.doc.get("sha256"), doc) for doc in cache)
    cached_files = dict((asset.sha256, asset) for asset in _get_local_files)

    for hash_l in cache_hashes - cached_files:
        remove_from_cache(hash_l)

    for hash_l in cached_files - cache_hashes:
        asset = cached_files[hash_l]
        os.remove(asset.filepath)


def list_cache():
    cache = read_cache()
    print(Asset.print_fmt.format(**dict(sha256_short="SHA256", asset_name="Asset Name", is_cached="")))
    print(Asset.print_fmt.format(**dict(sha256_short="------", asset_name="----------", is_cached="")))
    for obj in cache:
        print(obj)
    print()


def clean_cache(verbose=False):
    to_remove = _get_local_files()
    for asset in to_remove:
        print(f"rm {fname}")
        os.remove(asset.filepath)


if __name__ == "__main__":
    list_cache()
