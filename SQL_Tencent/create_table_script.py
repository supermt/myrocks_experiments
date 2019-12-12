#!/usr/bin/python3

table_desc_dict = {
    "logtime": "timestamp",
    "svr_ip": "string",
    "user_ip": "string",
    "port": "long",
    "host": "string",
    "url": "string",
    "req_args": "string",
    "strrange": "string",
    "http_code": "long",
    "send_bytes": "long",
    "handle_time": "long",
    "refer": "string",
    "user_agent": "string",
    "stdform": "string",
    "uin": "long",
    "isnormalclosed": "long",
    "url302": "string",
    "cdn": "long",
    "sample": "long",
    "filesize": "long",
    "inner_errcode": "long",
    "inner_filename": "string",
    "bizid": "long",
    "flow": "long",
    "clientappid": "string",
    "reverse_proxy": "string",
    "oc_id": "string",
    "str_reserve": "string",
    "vkey": "string",
    "int_reserve": "long",
    "province": "long",
    "isp": "long",
    "log_type": "long",
    "get_store_time": "long",
    "deliver_time": "long",
    "store_type": "long",
    "bit_rate": "long",
    "media_time": "long",
    "media_type": "string",
    "req_type": "long",
    "inner_errmsg": "string",
    "content_type": "string",
    "store_ip": "string",
    "resolution": "long",
    "reserve1": "long",
    "reserve2": "long",
    "reserve3": "long",
    "reserve4": "string",
    "reserve5": "string",
}

sql_query = "Create Table media_streaming (" 

for column_name in table_desc_dict:
    column_type = table_desc_dict[column_name]
    if column_type == "long":
        sql_query += (column_name +" INT, ")
    if column_type == "string":
        sql_query += (column_name + " VARCHAR(200), ")

sql_query += ") Engine=ROCKSDB"

print(sql_query)