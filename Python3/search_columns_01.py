#!/home/cloudera/anaconda3/bin/python

####################################################################################################
# Description: This is used to search column name in a table based on a particular pattern.
#
# History:
#        2019-08-01 : Subrat Kumar       : Created
####################################################################################################

import logging
import datetime
import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_list, concat, col, lit

def search_col(trg_db, trg_table, search_str):
    sql_stmt = "desc {0}.{1}".format(trg_db, trg_table)
    col_df = spark.sql(sql_stmt).select("col_name", concat(lit("nvl("), "col_name", lit(", 0)")).alias("d_col_name"))

    col_list = col_df.select("col_name").select(collect_list("col_name")).collect()[0][0]
    d_col_list = col_df.select("d_col_name").select(collect_list("d_col_name")).collect()[0][0]

    col_str = "||':'||".join(col_list)
    d_col_str = "||':'||".join(d_col_list)

    sql_stmt = "select count(*) from {0}.{1} where instr({2}, ':{3}:') <> 0".format(trg_db, trg_table, d_col_str, search_str)
    REC_COUNT = spark.sql(sql_stmt).collect()[0][0]

    logging.info("Sql Query: {0}".format(sql_stmt))

    print(LN_T)

    if REC_COUNT > 0:
        logging.info("Search string '{0}' found in table {1}.{2}".format(search_str, trg_db, trg_table))

        for i in col_list:
            sql_stmt = "select count(*) from {0}.{1} where {2} = '{3}'".format(trg_db, trg_table, i, search_str)
            REC_KOUNT = spark.sql(sql_stmt).collect()[0][0]

            if REC_KOUNT > 0:
                logging.info("{0}:{1}:{2}:{3}".format(trg_db, trg_table, i, search_str))
    else:
        logging.info("Search string '{0}' not found in table {1}.{2}".format(search_str, trg_db, trg_table))

    print(LN_T)

if __name__ == '__main__':
    logging.basicConfig(
                         level = logging.INFO,
                         format = '%(asctime)s:%(filename)s:%(levelname)-8s:%(message)s',
                         datefmt = '%Y-%m-%d %H:%M:%S'
                       )

    LN_T = "~"*100

    spark = SparkSession.builder.appName('search_str_Test').enableHiveSupport().getOrCreate()

    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="Search String"
    )

    # Add the parameters positional/optional
    parser.add_argument('-d', '--db', help = "Database Name", type = str)
    parser.add_argument('-t', '--table', help = "Table Name", type = str)
    parser.add_argument('-s', '--search', help = "Search String", type = str)

    args = parser.parse_args()
    logging.info("Argument Details: {0}".format(args))

    if not args.db.strip() or not args.table.strip() or not args.search.strip():
        logging.error("None of the argument can be blank/null")
    else:
        search_col(args.db, args.table, args.search)
