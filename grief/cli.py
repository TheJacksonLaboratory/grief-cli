#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option("--verbose/--quiet", default=False)
@click.pass_context
def cli(ctx, verbose):
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose

@cli.command()
@click.argument("query", nargs=-1)
@click.option("--species", default=None)
@click.option("--tool", default=None)
@click.option("--assembly", default=None)
@click.option("--contributor", default=None)
def search(query, *, species, tool, assembly, contributor):
    print(query)

@cli.command()
@click.argument("asset", nargs=-1)
@click.option("--json", is_flag=True, default=False)
def info(assets, *, json=False):
    pass

@cli.command()
@click.argument("asset", nargs=-1)
@click.option("--cache/--no-cache", default=True)
@click.option("--overwrite/--no-overwrite", default=False)
def pull(assets, *, cache, overwrite):
    pass

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
    pass

@cli.group()
def cache():
    pass

@cache.command("list")
def cache_list():
    pass

@cache.command("clean")
@click.option(
    "--yes", is_flag=True,# callback=abort_if_false,
    expose_value=False,
    prompt="Remove all listed entries?"
)
def cache_clean(*, yes):
    pass


if __name__ == "__main__":
    cli(obj={})
