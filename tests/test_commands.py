import json
from click.testing import CliRunner
from pipeline.cli import extract_command, transform_command, load_command


def test_extract(target_dir):
    runner = CliRunner()
    resp = runner.invoke(extract_command, [
        '--repo-owner', 'tjwaterman99',
        '--repo-name', 'theydo-exercise',
        '--target', target_dir / 'out.json'
    ])
    assert resp.exit_code == 0
    print(resp.stdout)
    data = open(target_dir / 'out.json').readlines()
    assert len(data) >= 1
    assert 'tjwaterman99/theydo-exercise' in json.loads(data[0])['url']


def test_load(target_dir):
    runner = CliRunner()
    resp = runner.invoke(load_command, [
        '--source', target_dir / 'out.json',
        '--target', 'issues'
    ])
    assert resp.exit_code == 0
    print(resp.stdout)


def test_transform(target_dir):
    runner = CliRunner()
    resp = runner.invoke(transform_command, [
        '--source', 'issues'
    ])
    assert resp.exit_code == 0
    print(resp.stdout)

