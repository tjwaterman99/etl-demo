import os
from dotenv import load_dotenv
from pytest import fixture, TempdirFactory
from pipeline.clients import GitHubClient


load_dotenv()


@fixture
def github_client():
    token = os.environ['GITHUB_TOKEN']
    client = GitHubClient(token=token)
    return client


@fixture(scope='session')
def target_dir(tmpdir_factory: TempdirFactory):
    target =  tmpdir_factory.mktemp('target')
    return target