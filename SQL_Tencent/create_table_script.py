#!/usr/bin/python3
import os
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
    "uin": "string",
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

table_name = '`media_streaming`'
src_file_name = "/vodlog2.csv"
db_name = "mtr"
drop_table_sentence="Use "+db_name + ";"+"DROP Table if exists"+ table_name +";"
print(drop_table_sentence)

table_create_sentence = "Create Table "+table_name+" ("
insert_sentence = "LOAD DATA infile '" + \
    os.path.abspath("./") + src_file_name + "\' INTO Table " + table_name + " ("

integer_column={}

for column_name in table_desc_dict:
    column_type = table_desc_dict[column_name]
    if "url" in column_name or "key" in column_name or "filesize" in column_name:
        table_create_sentence += (column_name + " VARCHAR(500), ")
        insert_sentence += (column_name + ",")
    else:
        if column_type == "long":
            table_create_sentence += (column_name + " INT, ")
            insert_sentence += ("@v"+column_name + ",")
            integer_column[column_name]=column_type
        elif column_type == "string":
            table_create_sentence += (column_name + " VARCHAR(200), ")
            insert_sentence += (column_name + ",")
        else:
            table_create_sentence += (column_name + " " + column_type + ", ")
            insert_sentence += (column_name + ",")

insert_sentence = insert_sentence[:-1] + ") SET "

for column_name in integer_column:
    insert_sentence += (column_name + " = nullif(@v" + column_name + ',\'\'), ')

insert_sentence = insert_sentence[:-2]


table_create_sentence = table_create_sentence[:-2]
table_create_sentence += ") Engine=ROCKSDB;"

print(table_create_sentence)

print(insert_sentence)

table_head = ""
for column_name in table_desc_dict:
    table_head += (column_name+",")

table_head = table_head[:-1]


# insert_sentence += "INSERT INTO media_streaming ("

# insert_sentence += table_head

# insert_sentence += ") VALUES "

# FILENAME = "test.csv"
# table_records = open(FILENAME,"r")

# line = table_records.readline()

# i = 1
# values=""

# while line:
#     value_set = ""
#     for column,key in zip(line[:-1].split("\t"),table_desc_dict):
#         value_set += "\""+ column + "\","
#     value_set = "("+value_set[:-1]+")"
#     if i % 10 == 0:
#         print(insert_sentence + values[:-1])
#         values=""
#     else:
#         values+=(value_set + ",")
#     line = table_records.readline()
#     i=i+1

# table_records.close()
