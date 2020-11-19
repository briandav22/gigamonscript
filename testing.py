
from modules.db_handler import DB_handler
from modules.dashbaord_handler import Dash_handler
from modules.report_handler import Report_handler
from modules.json_handler import Json_handler
from modules.report_designer import Report_designer
from reports.reports import Report_types

import configparser
import json
import os


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config', 'db_creds.ini'))
config_info = config['DB']
db_name = config_info['db_name']
db_user = config_info['scrutinizer_user']
db_pass = config_info['scrutinizer_host']
db_host = config_info['scrutinizer_host']


dash_handler = Dash_handler()

report_handler = Report_handler()

json_handler = Json_handler()

report_types = Report_types()

report_designer = Report_designer()


column_names = [
                {"group_by":{"column_name":"sourceipaddress","column_lang":"Source Ip", "manufactured":"NULL"}},
                {"group_by":{"column_name":"commonport","column_lang":"Application", "manufactured":"NULL"}},     
                {"trend_by":{"column_name": "octetdeltacount","column_sum":"sum_octetdeltacount","column_lang":  "NULL","style":"rate","manufactured":"NULL" }}
                ]

report_lang = "newestGigamona"
report_pretty = "Gigamon Brian Da"

db_handler = DB_handler(db_name,db_user,db_pass,db_host)
#open connection to DB
db_handler.open_connection()


db_handler.test_connection()

#find next report ID
# report_id_query = report_designer.get_available_id()

# report_id = db_handler.execute_query(report_id_query)[0]

# report_id = 10700
# print(report_id)
# querys = []

# # create report header info 

# report_header_query = report_designer.report_headers(report_id,report_lang, 23, 'stacked')

# querys.append(report_header_query)

# ## create columns query

# report_columns_query = report_designer.create_report_columns(report_id, column_names)


# querys.append(report_columns_query)
# ## set group by information
# report_groupby_query = report_designer.report_types_groupby(report_id, column_names)


# querys.append(report_groupby_query)
# ## set aggregations
# report_aggregation_query = report_designer.report_type_aggregations(report_id, column_names)

# querys.append(report_aggregation_query)

# ## set whats mandatory for report
# report_type_select = report_designer.report_type_select(report_id, column_names)
# querys.append(report_type_select)

# # make report name prettier
# report_add_lang = report_designer.add_lang_kery(report_lang, report_pretty)


# querys.append(report_add_lang)

# # alter sequence
# report_restart_sequence = report_designer.alter_sequence(report_id)


# querys.append(report_restart_sequence)

# db_handler.execute_query(report_restart_sequence)
# # for query in querys:
# #     db_handler.execute_query(query)


# data_back = db_handler.execute_query("select * from plixer.report_types_rt_id_seq ;")

# print(data_back)

db_handler.close_connection()













# data = report_designer.report_columns('1', example_list)


# some_json = report_types.protocal_count('ProtocalCount',158)

# print(some_json)

# # # set up DB handler class that will be used to access database. 
