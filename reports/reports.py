import json

class Report_types:
    def __init__self(self):
        return
    
    def protocal_count(self, report_name, saved_id):
        protocal_count = json.dumps({"saved":{"name":"brian_protocals","id":164},"reportTypeLang":"flowCountByWKP","filters":{"sdfDips_0":"in_0A01027C_ALL","sdfPorts_1":"in_3389-6","sdfPorts_0":"in_22-6"},"byInt":{"selected":0},"dataMode":{"selected":"raw_flows"},"tableView":{"inbound":{"query_limit":{"max_num_rows":"10","offset":0}},"sorting":"DESC","maxNumRows":"10","outbound":{"query_limit":{"max_num_rows":"10","offset":0}},"hidden_cols":["rpt_man_peak","rpt_man_95th"]},"ipDns":{"selected":"dns"},"dataGranularity":{"selected":"auto"},"reportDirections":{"selected":"inbound"},"graphView":{"showOthers":1,"types":{"default":"pie","selected":"line","available":["pie","bar","step","total_bar","donut","hidden","line"]},"graphGranularity":{"seconds":60,"default":"medium","selected":"medium","sizes":{"high":180,"low":60,"medium":"120"},"available":["low"]},"hidden":False,"graphStyle":{"default":"nonStacked","selected":"stacked","available":["stacked","nonStacked"]}},"orderBy":"sum_plixeraggregatedrecordcount","dataFormat":{"selected":"normal"},"times":{"clientTimezone":"America/New_York","dateRange":"LastHour","end":"1605113820","start":"1605110220"},"rateTotal":{"selected":"total","available":["rate","total"]},"bbp":{"selected":"bits"}})

        return protocal_count



