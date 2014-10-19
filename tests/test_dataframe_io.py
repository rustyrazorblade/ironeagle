from cassandra.cluster import Cluster
from pandas import DataFrame

from ironeagle import get_prepared_statement

cluster = Cluster()
session = cluster.connect("ironeagle")

tab = """
      CREATE TABLE IF NOT EXISTS simple (
      id int primary key,
      name text
      )
      """
session.execute(tab)

df = DataFrame.from_records([(1, "jon"), (2, "pete")],
                            columns=['id', 'name'])


def test_get_prepared_statement():
    prepared = get_prepared_statement(session, df, "simple")
    assert "id, name" in prepared
    assert "(?,?)" in prepared
