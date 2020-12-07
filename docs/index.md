# Scrutinizer Dashboard Maker

A project that helps Users and Engineers create 'quick start' dashboards for Scrutinizer deployments. 

## Commands


* `python dashboard_maker.py --make [string that fires main() function call]` - call the main function to build your dashboards.
* `python dashboard_maker.py --delete [string that fires delete_all() function call]` - call the delete_all function to remove your dashboard.

## Example Commands 

* `python dashboard_maker.py --make gigamon` - Create the pre-built gigamon dashboard.
* `python dashboard_maker.py --delete gigamon` - Delete pre-built gigamon dashboard.


## Project layout

    config/
        db_creds.ini   # The configuration file. This is where the user will fill out required DB usernames / passwords.
    docs/ 
        index.md  # The documentation homepage.
    modules/
        dashboard_handler.py # Handles creating queries needed for dashboard creating and management. 
        db_handler.py # Responsible for establishing connections to the database and executing queries.
        json_handler.py # Many of the database queries require a JSON object as part of the query. This class contains various methods for generating those JSON objects. 
        report_designer.py # In the event that your dashboard required reports that are not native to Scrutinizer, they can be designed using the report_designer method. 
        report_handler.py # Used to generate the SQL needed for making Saved Reports and fetching ID's. 
        report_maker.py # Function that is used to execute all of the designed report SQL in the proper order. 
    custom_dashboards/ #This is where users can add in there own custom dashboards as desired. 
        gigamon/ #pre-built Gigamon dashboard ready to be used.
            dashboards/ #pre-built dashboards
                gigamon_counts.py 
                gigamon_dns.py
                gigamon_sus.py
            designed_reports/ #since the gigamon dashbaords rely on reports that are not native to Scrutinizer, they will be created as the script runs. Those reports are stored here.
                gigamon_reports.py #holds all of the reports to be created for the Gigamon dashboard
    dashboard_maker.py #primary file used to execute the created of dashboards. Holds a variety of methods that receive the necessary object for dashboard creation.


## Modifying the Script

If you would like to create a dashboard outside of what is provided you will need to:

* create a **project directory** in  'custom_dashboards'  hold your new dashboard(s). 
    * Add a **dashboards** sub directory
    * Add a **designed reports** sub directory - only if you intend on using reports that aren't out of the box with Scrutinizer. 



    #### Example    

        custom_dahboards/
            my_new_project/
                dashboards/
                designed_reports/


* within the dashboards folder create a python file that will hold the gadget objects. That file will have the following structure. 

    ### Global Variables

    These globale variables will be passed into each dashboard object, the could be ommited and placed into each object manually if desired 

        dashboard_name = 'Name of Dashboard to be Created'

        exporter = 'in_GROUP_ALL' # this will use all exporters, alternativaly you could use an object for the exporters you want.

        user_id = 1 # Part of making the dashbaords required yout o make the dashboard visible to a user. 1 represents the default admin user. 

    ### Dashboard Objects

    Each dashboard object <b>MUST</b> have all of the key / value pairs shown below. if you omit any of them you will throw an error and terminate the Script. 
    
    These objects are responsible for: 

    1.) Creating the Dashboard 

    2.) Creating Saved Reports 

    3.) Converting those Saved Reports into Gadgets

    4.) Moving those Gadgets to the Dashboard in the correct position. 

    


    * lang : this is the report lang key, examples would be things like "conversationsWKP" or "applications"
    * filters : 



```json
report_1 = {
    "name" : "Name for Gadget1",    
    "lang" : "report lang key", 
    "filters" : {}, 
    "position" : { "width":4, "height":15, "y":0, "x":0 },
    "direction":"inbound",
    "time_range":"Last24Hours",
    "data_type": "total",
    "stacked":"stacked",
    "exporter": exporter,
    "view":"tableGraph",
    "user_id":user_id,
    "dashboard": dashboard_counts
}

report_2 = {
    "name" : "Name for Gadget2",    
    "lang" : "report lang key", 
    "filters" : {}, 
    "position" : { "width":4, "height":15, "y":0, "x":0 },
    "direction":"inbound",
    "time_range":"Last24Hours",
    "data_type": "total",
    "stacked":"stacked",
    "exporter": exporter,
    "view":"tableGraph",
    "user_id":user_id,
    "dashboard": dashboard_counts
}

example_gadgets_list = [report_1, report_2]
```
    
    

