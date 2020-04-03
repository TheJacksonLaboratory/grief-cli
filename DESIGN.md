## Available commands

command: `search`
subcommands: None
required-args: query-string
optional-args:
    - `--species`
    - `--tool`
    - `--assembly`
    - `--contributor`
action:
    - query remote server for assets matching query-string and optional-args
    - query local cache for assets matching query-string and optional-args
returns:
    - asset-name, asset-hash, local indicator of assets matching query

command: `info`
subcommands: None
required-args: asset-name or asset-hash (or more than one)
optional-args:
    - `--json`
action:
    - print all available metadata for specified asset
    - `if --json` print all available metadata for specified asset in JSON
returns:
    - None

command: `pull`
subcommands: None
required-args: asset-name or asset-hash (or more than one)
optional-args:
    - `--no-cache`
    - `--force`
action:
    - download specified asset to cache if not in cache or (if `--no-cache`) current directory
    - download specified asset to cache even if exists locally (if `--force`)
returns:
    - None

command: `get`
subcommands: None
required-args: asset-name or asset-hash (or more than one)
optional-args:
    - `-y/--yes`
    - `--no-cache`
    - `--force`
    - `--all`
action: 
    - perform `search`
    - `pull` resulting matches
    - return local path to resulting assets
returns:
    - local path to specified genomic assets

command: `cache`
subcommands: `list`, `clean`
required-args:
optional-args:
returns:
    - 


## Configuration and state storage

Configuration files:
-   written in YAML
-   located in `$XDG_CONFIG_HOME`


## Data and cache storage

`$XDG_CACHE_HOME`


