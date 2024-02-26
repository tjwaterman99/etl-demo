from pipeline.clients import GitHubClient, PostgresClient


# I think this will fail if the token does not have the `user` scope, so not
# sure it can run in CI with the default GitHub workflow context's token
def test_client_connect(github_client: GitHubClient):
    resp = github_client.api.get_user()
    assert resp.email is not None


def test_client_get_repo(github_client: GitHubClient):
    repo = github_client.get_repo('tjwaterman99', 'theydo-exercise')
    assert repo.default_branch == 'main'


def test_client_get_issues(github_client: GitHubClient):
    issues = github_client.get_issues('tjwaterman99', 'theydo-exercise')
    assert issues.totalCount > 0
    assert len(list(issues)) > 0


def test_postgres_client(postgres_client: PostgresClient):
    resp = postgres_client.execute_stmt('select current_role')
    assert resp.fetchall()[0][0] is not None