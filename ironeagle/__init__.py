
def save_dataframe_to_cassandra(session, dataframe, table):
    """

    :param session:
    :param dataframe:
    :param table:
    :return:
    """
    statement = get_prepared_statement(dataframe, table)

    prepared = session.prepare(statement)



def get_prepared_statement(dataframe, table):
    """

    :param session:
    :param dataframe:
    :type dataframe pandas.DataFrame
    :param table:
    :return:
    """
    keys = dataframe.keys()

    str_keys = ", ".join(keys)

    placeholders = ",".join(["?"] * len(keys))

    stmt = "INSERT INTO %s (%s) VALUES (%s)" % (table, str_keys, placeholders)

    return stmt


