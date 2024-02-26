import json
from pipeline.clients import GitHubClient, PostgresClient


def extract(client: GitHubClient, repo_owner: str, repo_name: str, target: str):
    print(f"Extracting {repo_name}/{repo_owner} to {target}")
    issues = client.get_issues(owner=repo_owner, name=repo_name)
    with open(target, 'w') as fh:
        deserialized = [json.dumps(i.raw_data) for i in issues]
        fh.writelines(deserialized)
    return deserialized


def load(client: PostgresClient, source: str, target: str):
    print(f"Loading {source} to {target}")


def transform(client: PostgresClient, source: str):
    print(f"Running transforms for {source}")
