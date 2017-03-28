# MySQL-gernal-log-add-timestamp
This scripts is used for adding timestamp to MySQL's gernal log, and cutting the log by timestamp.

一、简介
MySQL DBA 经常会在全日志中定位问题SQL，但是现阶段实例一天的全日志量往往很可观，十几GB的日志很常见；而且定位到问题SQL之后，往往没有时间戳，给定位问题带来很大的不便。该脚本目前实现两个功能：1、按照时间截取日志；2、给所有SQL加上时间戳。

二、使用方法
假如按照指定时间来截取日志：
python log.py -b '170327  1:30:00' -e '170327  2:30:00' -f '/data/opdir/zhouyangfan/mysql.log' -s 1024 -r '/data/opdir/zhouyangfan/tmp.txt'
-b:开始截取时间戳（可以不加该选项，默认从头开始）
-e:结束截取时间戳（可以不加该选项，默认到文件结束）
-f:日志路径
-r:输出文件路径
-s:一次读取的字节数
