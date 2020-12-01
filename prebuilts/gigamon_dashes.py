
### Three Dashboards that are created for Gigamon Devices. 

dashboard_DNS = 'Gigamon - DNS Monitor'
dashboard_Sus = 'Gigamon - Suspicious Traffic'
dashboard_Ver = 'Gigamon - Version Count'

exporter = 'in_GROUP_ALL'
user_id = 1

#### DNS Monitor Reports ####

dns_1 = {
    'name' : 'Gigamon - Top DNS',
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

dns_monitor = [dns_1, dns_2]