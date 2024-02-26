# etl-demo
Demo of a simple ETL proejct

## Setup

Open the project in a GitHub codespace. The [postCreateCommand](.devcontainer/postCreateCommand.sh) will install the Python and other dependencies the first time the codespace starts.

After starting the codespace, start the postgres database and create a role and user.

```sh
sudo service postgresql start
sudo su postgres
createdb codespace
createuser codespace
exit
```

You should now be able to connect to the database as the codespace user.

```sh
psql -c 'select current_role'
```
