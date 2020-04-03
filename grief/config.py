#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml

from pathlib import Path


CONFIG_DIR = Path(
    os.environ.get("XDG_CONFIG_HOME", "~/.config")
).expanduser() / "grief"
if not CONFIG_DIR.exists():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

CONFIG_FILE = CONFIG_DIR / "grief.yaml"
CONFIG_FILE.touch()


def load_config():
    with open(CONFIG_FILE, "r") as buff:
        yaml.load(buff)
