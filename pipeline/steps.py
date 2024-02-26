import json
from psycopg2 import extras as postgres_helpers
from pipeline.clients import GitHubClient, PostgresClient
from pipeline.sql import init_stmt, insert_issue_stmt, parse_issue_details_stmt, flatten_issue_details_stmt


def extract(client: GitHubClient, repo_owner: str, repo_name: str, target: str):
    print(f"Extracting {repo_name}/{repo_owner} to {target}")
    issues = client.get_issues(owner=repo_owner, name=repo_name)
    with open(target, 'w') as fh:
        deserialized = [json.dumps(i.raw_data) for i in issues]
        fh.writelines(deserialized)
    return deserialized


def load(client: PostgresClient, source: str, target: str):
    print(f"Loading {source} to {target}")
    f_init_stmt = init_stmt.format(table_name=target)
    f_insert_stmt = insert_issue_stmt.format(table_name=target)
    client.execute_stmt(f_init_stmt)
    
    with open(source) as fh:
        lines = fh.readlines()
        for line in lines:
            data = json.loads(line)
            client.execute_stmt(f_insert_stmt, [postgres_helpers.Json(data)])
    client.conn.commit()
    return lines


def transform(client: PostgresClient, source: str):
    f_parse_issue_details_stmt = parse_issue_details_stmt.format(
        source=source,
        view_name=f"{source}_parsed"
    )
    f_flattened_issue_details_stmt = flatten_issue_details_stmt.format(
        source_view_name=f"{source}_parsed",
        flattened_view_name=f"{source}_flattened"
    )
    client.execute_stmt(f_parse_issue_details_stmt)
    client.conn.commit()
    client.execute_stmt(f_flattened_issue_details_stmt)
    client.conn.commit()
    
