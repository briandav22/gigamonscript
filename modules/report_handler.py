import json

class Report_handler:
    def __init__(self):
        return

    def available_report_id(self):
        return ("SELECT MAX(saved_id)+ 1 FROM reporting.saved_reports;")



    def create_report_query(self, saved_id, saved_name, report_obj, created_by):
        return (f"INSERT INTO reporting.saved_reports(saved_id, saved_name, report_obj, hasthreshold, is_hidden, created_by)  VALUES ('{saved_id}','{saved_name}','{report_obj}', 0, 0, {created_by})")


    def get_report_id(self, report_name):
        return(f"SELECT saved_id FROM reporting.saved_reports WHERE saved_name = '{report_name}'")

    def get_gadget_id(self, report_name):
        return(f"SELECT gadget_id FROM plixer.dash_gadgets WHERE gadget_name = '{report_name}'")