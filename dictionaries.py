import json
json_string_data='''
{
    "env": "dev",
    "db_main": "DEV_CLAIMS_ETL_INCREMENTAL",
    "schema_main": "CUSTOM_RUN",
    "sf_account": "kyber",
    "sf_username": "REPLACE_ME",
    "sf_password": "123456",
    "sf_role": "DEV_SUPPL_PIPELINE",
    "warehouse": "wh_data_eng_dev_med_pipeline",
    "sf_small_warehouse": "METADATA",
    "sf_medium_warehouse": "MEDIUM_QUERY",
    "sf_large_warehouse": "LARGE_QUERY",
    "sf_xlarge_warehouse": "XL_QUERY_MED",
    "sf_2xlarge_warehouse": "MORE_XL_QUERY_MED",
    "sf_2xlarge_warehouse_2": "MORE_XL_QUERY",
    "sf_3xlarge_warehouse": "XL3_QUERY",
    "debug": true,
    "databases": {
        "suppl_tables": "DEV_SUPPL_TABLES",
        "claims_etl_incremental": "DEV_CLAIMS_ETL_INCREMENTAL",
        "claims_etl": "DEV_CLAIMS_ETL",
        "kyber_shared": "DEV_KYBER_SHARED",
        "kyber_shared_last_delivery": "fake_kyber_shared_latest_delivery",
        "projects": "fake_projects"

    },
 "roles": {
          "prod_health_trial": "DEV_SUPPL_PIPLINE",
          "accountadmin": "DEV_SUPPL_PIPELINE"
     }
}
'''

print(json_string_data)

config = json.loads(json_string_data)

for item in config:
    if type(config[item]) is dict:
       print()
       print(item)
       print("----------") 
       for item2 in config[item]:
           print(str(type(config[item][item2])) + " : " + item2 + " = " + str(config[item][item2]))
       print()
    else:
        print(str(type(config[item])) + " : " + item + " = " + str(config[item]))


>>> for key in config["databases"].keys():
...     print(key)