# This is the guildline for you to compile the myrocks into mariadb

[main reference](https://mariadb.com/kb/en/library/building-myrocks-in-mariadb/)

## MyRocks is a storage engine built as a plugin of MySQL, by logging the internal operation, we can get a heavy-writing workload by real-world dataset

> Pay attention! The MyRocks can only be built on GNU-based system, Mac OS will break up due to lack of GNU protocols

## Some former requirements

sudo apt-get update
sudo apt-get -y install g++ cmake libbz2-dev libaio-dev bison zlib1g-dev libsnappy-dev 
sudo apt-get -y install libgflags-dev libreadline6-dev libncurses5-dev libssl-dev liblz4-dev gdb git

sudo apt-get install gnutls-dev libbison-dev

> Attention, in some cases, your bison will be out-of-date, please re-install it. To check it, use `bison --version` to ensure the version is higher than 2.0

## Copy the repo and build

```bash
git clone https://github.com/MariaDB/server.git mariadb-10.2
cd mariadb-10.2
git checkout 10.2
git submodule init
git submodule update
cmake .
make -j10
```

## install the plugin to the mysqld by minimal 

```bash
datadir=../mysql-test/var/install.db
plugin-dir=../storage/rocksdb
language=./share/english
socket=/tmp/mysql.sock
port=3307

plugin-load=ha_rocksdb
default-storage-engine=rocksdb
```

## run the test case to ensure the plugin has been installed

```bash
(cd mysql-test; ./mtr alias)
cp -r mysql-test/var/install.db ~/data1
cd sql
```

## run the mysqld in command line or idea

```shell
./mysqld --defaults-file=~/my1.cnf
```

## useful commands

you can use the following command to change the storage engine

```SQL
alter table test_suppressions engine 'rocksdb';
```




# How to trace and reply the workload

Mostly, I once decided to record the trace according to this [documentation](https://github.com/facebook/rocksdb/wiki/RocksDB-Trace,-Replay,-Analyzer,-and-Workload-Generation).

But then I found that the trace recorder will optimize the write operations, so I tried to use some stupid ways....
