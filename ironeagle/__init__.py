
def save_dataframe_to_cassandra(session, dataframe, table):
    """

    :param session:
    :param dataframe:
    :param table:
    :return:
    """
    statement = get_prepared_statement(session, dataframe, table)

    

def get_prepared_statement(session, dataframe, table):
    keys = dataframe.keys()
    str_keys = ", ".join(keys)

    placeholders = ",".join(["?"] * len(keys))

    stmt = "INSERT INTO station (%s) VALUES (%s)" % (str_keys, placeholders)
    prepared = session.prepare(stmt)

    return stmt


