dashboard_Sus = 'Gigamon - Suspicious Traffic'
dashboard_Ver = 'Gigamon - Version Count'


sus_protocals = { 'sdfPorts_0': 'in_22-6', 'sdfPorts_1': 'in_3389-6', 'sdfPorts_2': 'in_23-6'}

exporter = 'in_GROUP_ALL'
user_id = 1


sus_1 = {
    'name' : 'Gigamon - Protocol Watch',
    'lang' : 'flowCountByWKP',
    'filters' : sus_protocals,
    'position' : { 'width':12, 'height':14, 'y':0, 'x':0 },
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter': exporter,
    'view':'tableGraph"',
    'user_id':user_id,
    'dashboard': dashboard_Sus

}


dns_2 = {
    'name': 'Gigamon - DNS Source',
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

dns_3 = {
    'position': {'width':4,'height':9,'x':4,'y':14},
}

dns_4 = {
    'position': {'width':4,'height':9,'x':8,'y':14},
}

