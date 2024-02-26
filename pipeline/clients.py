import os
import psycopg2
from typing import Optional
from github import Github
from github.Auth import Token


class GitHubClient:
    def __init__(self, token: Optional[str]=None):
        self.token = token or os.environ.get("GITHUB_TOKEN")
        self.api = Github(auth=Token(self.token))

    def get_repo(self, owner: str, name: str):
        return self.api.get_repo(f"{owner}/{name}")

    # We can also grab issues last updated since a specific timestamp, which would
    # enable a much more efficient CDC approach. But for the sake of time I'll
    # just fetch all.
    # https://docs.github.com/en/rest/reference/issues
    def get_issues(self, owner: str, name: str, direction='desc'):
        repo = self.get_repo(owner, name)
        issues = repo.get_issues(direction=direction)
        return issues


class PostgresClient:
    def __init__(self):
        self.conn = psycopg2.connect()

    def execute_stmt(self, stmt: str, vars = list()):
        cursor = self.conn.cursor()
        print(stmt, vars)
        cursor.execute(stmt, vars)
        return cursor
