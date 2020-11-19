from modules.db_handler import DB_handler
from modules.dashbaord_handler import Dash_handler
from modules.report_handler import Report_handler
from modules.json_handler import Json_handler
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config', 'db_creds.ini'))


config_info = config['DB']
db_name = config_info['db_name']
db_user = config_info['scrutinizer_user']
db_pass = config_info['scrutinizer_host']
db_host = config_info['scrutinizer_host']

# initiate class that handles DB connections. 
db_handler = DB_handler(db_name,db_user,db_pass,db_host)
# iniate class  to create dashbaords
dash_handler = Dash_handler()
# initiate class to create reports. 
report_handler = Report_handler()
# initiate class used to create JSON objects needed in for various queries. 
json_handler = Json_handler()

report_name = 'gigamon_test_brian'
dashbaord_name = 'gigamon dash brian'
user_id = 1

#open connection to DB
db_handler.open_connection()

#create query to find next available dash ID. 
dash_id = dash_handler.available_dash_id()

#execute query and store results to a variable. 
dashbaord_id = db_handler.execute_query(dash_id)[0]

#create dashbaord query
dashboard_query = dash_handler.create_dashboard(dashbaord_name, dashbaord_id)

#create the dashboard
db_handler.execute_query(dashboard_query)

#make dashboard visible for Admin User Query 
make_visible_query = dash_handler.make_visible(dashbaord_id, user_id)

#make dashbaord visible. 
db_handler.execute_query(make_visible_query)

#find next available report ID 
available_report_id = report_handler.available_report_id()

#store report ID to variable. 
report_id = db_handler.execute_query(available_report_id)[0]

#create report object needed to build a saved report. 
report_obj = json_handler.report_json(report_name, report_id)

#build query to create a saved report fromt he report object created above. 
create_report_query = report_handler.create_report_query(report_id, report_name, report_obj, user_id)

#execute query to create saved report

db_handler.execute_query(create_report_query)

#retrive report_id needed to create a gadget from the new saved report

report_id_query = report_handler.get_report_id(report_name)

#store report_id to variable
report_id = db_handler.execute_query(report_id_query)[0]

#create json needed to convert saved report to a gadget

gadget_json = json_handler.gadget_json('tableGraph',report_id )

#create query needed to convert saved report to a gadget 

gadget_query = dash_handler.make_dash_gadget(report_id, report_name,gadget_json, user_id)

#executre query to convert saved report to dashboard gadget 

db_handler.execute_query(gadget_query)

#create JSON needed to add new dashboard gadgets to the dashboard. 

add_gadget_json = json_handler.add_gadget_json(report_id)

#create list of all gadgets needed to be added. 

gadget_list = json_handler.add_json_to_list(add_gadget_json)

#create query needed to add gadget to the dashboard

add_gadget_query = dash_handler.add_gadget_to_dash(gadget_list, dashbaord_id)

#execute query to add gadget to dash 

db_handler.execute_query(add_gadget_query)






#close connection to DB.
db_handler.close_connection()



