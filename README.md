# etl-demo

Demo of a simple ETL proejct

## Usage

```
python3 -m pipeline --help
Usage: python -m pipeline [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  extract    Extract the details of all repo issues
  load       Load extracted issues into a target Postgres table
  transform  Run transformations on issues loaded into Postgres
```

## Examples

Extract issues from a specific repository.

```sh
export REPO_OWNER=dbt-labs
export REPO_NAME=dbt-utils
export RAW_FILE=target/issues.json
export RAW_TABLE=issues_raw

python3 -m pipeline extract \
  --repo-owner $REPO_OWNER \
  --repo-name $REPO_NAME \
  --target $RAW_FILE

python3 -m pipeline load \
  --source $RAW_FILE \
  --target $RAW_TABLE

python3 -m pipeline transform \
  --source $RAW_TABLE
```

## Demo

The raw data is loaded into a table that can be used to summarize the issues over time, and by issue label.

See the screenshots in the [demo folder](/demo).

## Setup

Open the project in a GitHub codespace. The [postCreateCommand](.devcontainer/postCreateCommand.sh) will install various dependencies.

After starting the codespace, create a virtual environment and install the Python packages.

```
virtualenv .venv
.venv/bin/pip install --editable .
.venv/bin/pip install -r requirements.txt
```

Next, start the postgres database and create a role and user.

```sh
sudo service postgresql start
sudo su postgres
createdb vscode
createuser vscode
exit
```

You should now be able to connect to the database as the codespace user.

```sh
psql -c 'select current_role'
```

Create a GitHub token and save it in a `.env` file in the root of the repo.

```
GITHUB_TOKEN=ghp...
```

## Testing

Run the pipeline tests with pytest.

```
pytest
```

## TODO's

- Configurable landing zones (eg support S3 and not just local filesystem, differentiate test / staging / prod)
- CDC for the issues list, rather than full table refreshes
- CI for tests
