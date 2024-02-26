init_stmt = """
create table {table_name} (
  id serial primary key, 
  loaded_at timestamp without time zone default (now() at time zone 'utc'),
  data jsonb not null
);
"""

insert_issue_stmt = """
insert into {table_name} (data) values (%s)
"""

parse_issue_details_stmt = """
create or replace view {view_name} as
select
  {source}.data ->> 'number' as issue_id,
  ({source}.data ->> 'created_at')::timestamp as created_at,
  {source}.data -> 'labels' as labels
from {source}
"""

flatten_issue_details_stmt = """
create or replace view {flattened_view_name} as
select 
  {source_view_name}.issue_id,
  {source_view_name}.created_at,
  details.name as label
from {source_view_name},
jsonb_to_recordset({source_view_name}.labels) as details (name varchar)
"""