from click import group, option
from dotenv import load_dotenv
from pipeline.steps import extract, transform, load
from pipeline.clients import GitHubClient, PostgresClient


load_dotenv()


@group
def cli():
    pass


@cli.command(name='extract')
@option('--repo-owner', required=True, help="Owner of the repository")
@option('--repo-name', required=True, help="Name of the repository")
@option('--target', required=True, help="Location to dump the extract")
def extract_command(repo_owner, repo_name, target):
    """
    Extract the details of all repo issues
    """

    client = GitHubClient()
    extract(client=client, repo_owner=repo_owner, repo_name=repo_name, target=target)


@cli.command(name='load')
@option('--source', required=True, help="Location of the GitHub issues extract")
@option('--target', required=True, help="Name of the table to load the issues into")
def load_command(source, target):
    """
    Load extracted issues into a target Postgres table
    """

    client = PostgresClient()
    load(client=client, source=source, target=target)


@cli.command(name='transform')
@option('--source', required=True, help="Name of the table containing the issues")
def transform_command(source):
    """
    Run transformations on issues loaded into Postgres
    """

    client = PostgresClient()
    transform(client=client, source=source)
