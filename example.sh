#!/bin/bash

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