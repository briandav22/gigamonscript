
### Three Dashboards that are created for Gigamon Devices. 

dashboard_DNS = 'Gigamon - DNS Monitor 69'
exporter = 'in_GROUP_ALL'
user_id = 1

#### DNS Monitor Reports ####

report_1 = {
    'name' : 'Brian - TOP DNS Gigamon69',
    'lang' : 'flowCountByWKP',
    'filters' : {"sdfPorts_0":"in_53-17"},
    'position' : { 'width':12, 'height':14, 'y':0, 'x':0 },
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter': exporter,
    'view':'graph',
    'user_id':user_id,
    'dashboard': dashboard_DNS

}

report_2 = {
    'name': 'Brian - DNS Source Test69',
    'lang': 'flowCountBySource',
    'filters' : {"sdfPorts_0":"in_53-17"},
    'position': {'width':4,'height':9,'x':0,'y':14},
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter':exporter,
    'view':'table',
    'user_id':user_id,
    'dashboard': dashboard_DNS

}


report_3 = {
    'name': 'Brian Top Queries Test69',
    'lang': 'custom_briancount69',
    'filters' : {},
    'position': {'width':4,'height':9,'x':4,'y':14},
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter':exporter,
    'view':'table',
    'user_id':user_id,
    'dashboard': dashboard_DNS

}


report_4 = {
    'name': 'Brian Top Requestor Test69',
    'lang': 'custom_brianrequest69',
    'filters' : {},
    'position': {'width':4,'height':9,'x':8,'y':14},
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter':exporter,
    'view':'table',
    'user_id':user_id,
    'dashboard': dashboard_DNS

}


dns_monitor = [report_1, report_2, report_3, report_4]