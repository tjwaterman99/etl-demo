import random
import os
from dotenv import load_dotenv
from pytest import fixture, TempdirFactory
from pipeline.clients import GitHubClient, PostgresClient


load_dotenv()


@fixture
def github_client():
    token = os.environ['GITHUB_TOKEN']
    client = GitHubClient(token=token)
    return client


@fixture
def postgres_client():
    client = PostgresClient()
    return client


@fixture(scope='session')
def target_dir(tmpdir_factory: TempdirFactory):
    target =  tmpdir_factory.mktemp('target')
    return target


@fixture(scope='session')
def target_table():
    num = round(random.random() * 1e6)
    return f"test_issues_{num}"