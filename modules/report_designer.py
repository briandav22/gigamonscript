import itertools

class Report_designer():
    def __init__(self):
        
        return

    def _unpack(self, columns):
        # helper function used to format list into a query for SQL
        return ",".join(map(str, columns))  

    def get_available_id(self):
        return(f"SELECT MAX(rt_id)+ 1 FROM plixer.report_types;")
    
    def report_headers(self, report_id, lang_key, menu_group, graph_type ):
        return(f"INSERT INTO plixer.report_types (rt_id, rpt_lang, menugroup, graphtype, biwidth, totalstable, rt_source) VALUES ('{report_id}','{lang_key}','{menu_group}','{graph_type}',950,0,0);")

    def create_report_columns(self, report_id, report_columns):

        #takes in a list that includes all the report columns, outputs a list that will be used to create the insert statement.


        all_report_column = []

        group_by = 'group_by'
        trend_by = 'trend_by'
        column_order = 1
        for report in report_columns:
            
            if group_by in report:

                column_name = report[group_by]["column_name"]
                column_lang = report[group_by]["column_lang"]
                column  = f"('{report_id}','{column_name}','{column_order}','{column_lang}',NULL,NULL,'dynamic')"
                all_report_column.append(column)
                column_order += 1
            elif trend_by in report:
                column_name = report[trend_by]["column_sum"]
                column = f"('{report_id}','{column_name}','{column_order}',NULL,'alignRight,dataWidth,width_dynamic',NULL,'dynamic')"
                all_report_column.append(column)
                column_order += 1

            else:
                print('Invalid column type passed your column needs to either have the key "group_by" or the key "trend_by"')

        values = self._unpack(all_report_column)
      
    
        return (f"INSERT INTO plixer.report_types_columns (rt_id,col_name,col_order,col_lang,col_style,col_header_title_attr,col_width) VALUES {values}")




    def report_types_groupby(self, report_id, report_columns):
        


        all_report_column = []
        group_by = 'group_by'

        for report in report_columns:
            
            if group_by in report:

                column_name = report[group_by]["column_name"]
                column  = f"('{report_id}','{column_name}')"
                all_report_column.append(column)

        values = self._unpack(all_report_column)


        return(f"INSERT INTO plixer.report_types_groupby (rt_id, col_name)VALUES{values}")

    def report_type_aggregations(self, report_id, report_columns):

        group_by = 'trend_by'
        all_report_column = []

        for report in report_columns:
            if group_by in report:
                column_name = report[group_by]["column_name"]
                style = report[group_by]['style']
                column = (f"('{report_id}','{column_name}','sum',1,'rate,total','{style}','stacked,nonStacked','stacked',0,0,'bB','sum',0)")
                all_report_column.append(column)

        values = self._unpack(all_report_column)



        return(f"INSERT INTO plixer.report_types_operations(rt_id, col_name, operation, default_col, availableratetotals,defaultratetotal, availablegraphstyles, defaultgraphstyle, showother,percentok, units, total_operation, lowbad) VALUES {values}")

    def report_type_select(self, report_id, report_columns):


        all_report_column = []

        group_by = 'group_by'
        trend_by = 'trend_by'

        for report in report_columns:
            
            if group_by in report:

                column_name = report[group_by]["column_name"]
                manufactured = report[group_by]["manufactured"]
                column  = f"('{report_id}', '{column_name}', {manufactured})"
                all_report_column.append(column)

            elif trend_by in report:
                column_name = report[trend_by]["column_name"]
                manufactured = report[trend_by]["manufactured"]
                column  = f"('{report_id}', '{column_name}', {manufactured})"
                all_report_column.append(column)

        values = self._unpack(all_report_column)

        return(f"INSERT INTO plixer.report_types_select(rt_id, col_name, manufactured)VALUES {values}")

    def add_lang_kery(self, report_lang, report_name, ):
        return(f"INSERT INTO languages.custom (id,string) VALUES ('{report_lang}','{report_name}');")

    def alter_sequence(self, report_id):
        return(f"ALTER SEQUENCE plixer.report_types_rt_id_seq RESTART WITH {report_id};")


