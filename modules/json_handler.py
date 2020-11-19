import json

class Json_handler:
    def __init__(self):
        return    

    def report_json(self, report_name, saved_id):
        report_json = json.dumps({"saved":{"name":f"{report_name}","id":f"{saved_id}"},"reportTypeLang":"conversationsApp","filters":{"sdfDips_0":"in_0A010104_0A010104-11"},"byInt":{"selected":0},"dataMode":{"selected":"raw_flows"},"tableView":{"inbound":{"query_limit":{"max_num_rows":"10","offset":0}},"sorting":"DESC","maxNumRows":"10","outbound":{"query_limit":{"max_num_rows":"10","offset":0}},"hidden_cols":["rpt_man_peak","rpt_man_95th"]},"ipDns":{"selected":"dns"},"dataGranularity":{"selected":"auto"},"reportDirections":{"selected":"both"},"graphView":{"showOthers":1,"types":{"default":"pie","selected":"line","available":["pie","total_bar","donut","matrix","step","bar","sankey","hidden","line"]},"graphGranularity":{"seconds":1800,"default":"medium","selected":"medium","sizes":{"high":180,"low":60,"medium":"120"},"available":["low"]},"hidden":False,"graphStyle":{"default":"stacked","selected":"stacked","available":["stacked","nonStacked"]}},"orderBy":"sum_octetdeltacount","dataFormat":{"selected":"normal"},"times":{"clientTimezone":"America/New_York","dateRange":"Last24Hours","end":"1601398800","start":"1601312400"},"bbp":{"selected":"percent"},"rateTotal":{"selected":"rate","available":["rate","total"]}})

        return report_json

    def gadget_json(self,view,saved_id):
        gadjet_json = json.dumps({"options":{"tableGraph":{"currentval":f"{view}","opts":[{"lbl":"Table","val":"table"},{"lbl":"Graph","val":"graph"},{"lbl":"Graph and Table","val":"tableGraph"}],"inputtype":"select"},"refresh_interval":{"currentval":10,"validation":"isNumberInteger","inputtype":"text"}},"foreign_key":f"{saved_id}"})

        return gadjet_json

    def add_gadget_json(self, saved_id):
        saved_id = 'report_' + str(saved_id)
        add_gadget = json.dumps({"gadget_type":"report","width":6,"y":0,"x":0,"id":f"{saved_id}","height":7})
        
        return add_gadget

    def add_json_to_list(self, report_json):
        gadget_list = []
        
        gadget_list.append(report_json)

        #strips out extre '' that PSQL doesn't like. 
        gadget_list = '[%s]' % ', '.join(map(str, gadget_list))

        return gadget_list
