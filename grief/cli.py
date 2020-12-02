#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

import hashing
from local import list_cache, clean_cache, add_to_cache, validate_cache
from query import search_all, list_search_results


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option("--verbose/--quiet", default=False)
@click.pass_context
def cli(ctx, verbose):
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose

@cli.command()
@click.argument("query", nargs=-1, required=True)
@click.option("--species", default=None)
@click.option("--tool", default=None)
@click.option("--assembly", default=None)
@click.option("--contributor", default=None)
def search(query, **kwargs):#species, tool, assembly, contributor):
    results = search_all(query, skip_remote=True, **kwargs)
    list_search_results(results, query=query)

@cli.command()
@click.argument("assets", nargs=-1)
@click.option("--json", is_flag=True, default=False)
def info(assets, *, json=False):
    pass

@cli.command()
@click.argument("assets", nargs=-1)
@click.option("--cache/--no-cache", default=True)
@click.option("--overwrite/--no-overwrite", default=False)
def pull(assets, *, cache, overwrite):
    validate_cache()

@cli.command()
@click.argument("asset_or_query", nargs=-1)
@click.option("--cache/--no-cache", default=True)
@click.option("--overwrite/--no-overwrite", default=False)
@click.option(
    "--yes", is_flag=True,# callback=abort_if_false,
    expose_value=False,
    prompt="Fetch all listed assets?"
)
def get(assets_or_query, *, cache, overwrite, yes):
    results = search_all(assets_or_query)
    validate_cache()

@cli.group()
def cache():
    pass

@cache.command("list")
def cache_list():
    list_cache()

@cache.command("clean")
@click.option(
    "--yes", is_flag=True,# callback=abort_if_false,
    expose_value=False,
    prompt="Remove all listed entries?"
)
def cache_clean(*, ctx, yes):
    clean_cache(verbose=ctx["verbose"])


if __name__ == "__main__":
    cli(obj={})
