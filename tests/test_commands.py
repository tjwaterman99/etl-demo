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
    print(resp.stdout)
    assert resp.exit_code == 0
    data = open(target_dir / 'out.json').readlines()
    assert len(data) >= 1
    assert 'tjwaterman99/theydo-exercise' in json.loads(data[0])['url']


def test_load(target_dir, target_table):
    runner = CliRunner()
    resp = runner.invoke(load_command, [
        '--source', target_dir / 'out.json',
        '--target', target_table
    ])
    print(resp.stdout)
    assert resp.exit_code == 0


def test_transform(target_dir, target_table):
    runner = CliRunner()
    resp = runner.invoke(transform_command, [
        '--source', target_table
    ])
    print(resp.stdout)
    assert resp.exit_code == 0
