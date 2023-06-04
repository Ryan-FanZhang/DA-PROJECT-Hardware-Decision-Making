# import packages

from snowflake.snowpark.functions import *
from snowflake.snowpark import Session
import pandas as pd
import datetime
import calendar

connection_parameters = {
        "account": "<your snowflake account>",
        "user": "<your snowflake user>",
        "password": "<your snowflake password>",
        "role": "<your snowflake role>",  # optional
        "warehouse": "<your snowflake warehouse>",  # optional
        "database": "<your snowflake database>",  # optional
        "schema": "<your snowflake schema>",  # optional
    }  

session = Session.builder.configs(connection_parameters).create()

def udf_time():
    # Get current date
    current_date = datetime.date.today()

    # Calculate 7 months ago
    seven_months_ago = current_date - datetime.timedelta(weeks=4*7)

    # Calculate the first date of 7 months ago
    first_date_of_seven_months_ago = datetime.date(seven_months_ago.year, seven_months_ago.month, 1)

    # Calculate the last date of 7 months ago
    last_date_of_seven_months_ago = first_date_of_seven_months_ago\
                                    .replace(day=calendar.monthrange(first_date_of_seven_months_ago.year, first_date_of_seven_months_ago.month)[1])

    return first_date_of_seven_months_ago, last_date_of_seven_months_ago

def run():
    # Get the time 
    first_date_of_seven_months_ago, last_date_of_seven_months_ago = udf_time()

    # Get the application info
    df_applications = session.table('DB_NAME.SCHEMA_NAME.applications')\
                         .select('*')\
                         .filter((col('submit_dt') >= first_date_of_seven_months_ago) & 
                                (col('submit_dt') < last_date_of_seven_months_ago))\
                         .filter(withColumn('hardware_fg', when(col('product_name')).isNotNull(), 'Y').otherwise('N'))\
                         .filter(col('hardware_fg') == 'Y')
    
    # Get the visa infomation from table Passport 
    df_passport = session.table('DB_NAME.SCHEMA_NAME.Passport')\
                     .select('*')\
                     .withColumn('visa_status', when(col('cd_type_visa')).isNotNull(), col('cd_type_visa')).otherwise('N/A')\
                     .select([
                            col('uuid').name('b_uuid'),
                            col('submit_dt').name('b_submit_dt'),
                            'visa_status'
                            ])
    

    # Get the alert info
    df_alert = session.table('DB_NAME.SCHEMA_NAME.alert')\
                  .select('*')\
                  .filter(col('status')._in(['Decline-Pending', 'Refer', 'BiometricsRequired']))\
                  .withColumn('alert_code_desc', when(col('alert_code').isin(['D18','D181']), 'D - Scorecard Related'),
                                                 when(col('alert_code').isin(["D2", "D32", "D7"]), 'D - Debt related'),
                                                 when(col('alert_code').isin(["D20", "D99"]), 'D - Eligibility'),
                                                 when(col('alert_code') == "D222", 'D - Collections related'),
                                                 when(col('alert_code') == "D300", 'D - Iovation related'),
                                                 when(col('alert_code').isin(["D43", "D44", "D30"]), 'D - Business eligibility'),
                                                 when(col('alert_code').isin(["D55", "D56"]), 'D - Business debt related')
                              ).otherwise(None)\
                  .select([
                           col('uuid').name('c_uuid'),
                           col('su mit_dt').name('c_submit_dt'),
                           'alert_code',
                           'alert_code_desc'
                          ])
    
    # Get the queues info
    df_queues = session.table('DB_NAME.SCHEMA_NAME.queues_info')\
                  .select([
                           col('uuid').name('d_uuid'),
                           col('submit_dt').name('d_submit_dt'),
                           'QUEUE_ID
                         ])
    
    # set up drop columns
    drop_cols = [
        'b_uuid',
        'b_submit_dt',
        'c_uuid',
        'c_submit_dt',
        'd_uuid',
        'd_submit_dt',
    ]

    # Join Together
    df_sum = df_applications.join(df_passport, (df_applications.uuid == df_passport.b_uuid) & (df_applications.submit_dt == df_passport.b_submit_dt), 'left')\
                            .join(df_alert, (df_applications.uuid == df_alert.c_uuid) & (df_applications.submit_dt == df_alert.c_submit_dt), 'left')\
                            .join(df_queues, (df_applications.uuid == df_queues.d_uuid) & (df_applications.submit_dt == df_queues.d_submit_dt), 'left')\
                            .drop(drop_cols)\
                            .withColumn('queue_flag', when(col('queuue_id').isin(['BUREAU ERROR QUEUE DEALER',
                                                                                   'BUREAU ERROR QUEUE NONDEALER',
                                                                                   'CUSTOMER ENRICHMENT QUEUE',
                                                                                   'FINAL REFER QUEUE DEALER',
                                                                                   'FINAL REFER QUEUE NONDEALER',
                                                                                   'NO ID QUEUE','ONLINE AUTOMATION QUEUE',
                                                                                   'BUREAU ERROR QUEUE',
                                                                                   'IDENTIFICATION ERROR QUEUE'
                                                                                   ]), 'Manual Queue'
                                                            ).otherwise('Automation Queue'))
    # Output as a csv folder stored in local using pandas
    df_sum = df_sum_final_1.to_pandas()
    df_sum.to_csv('file_name.csv')
    return print(f'run successfully')

if __name__ == "__main__":
    run()


