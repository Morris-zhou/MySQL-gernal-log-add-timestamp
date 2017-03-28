# MySQL-gernal-log-add-timestamp
This scripts is used for adding timestamp to MySQL's gernal log, and cutting the log by timestamp.

### 一、简介
MySQL DBA 经常会在全日志中定位问题SQL，但是现阶段实例一天的全日志量往往很可观，十几GB的日志很常见；而且定位到问题SQL之后，往往没有时间戳，给定位问题带来很大的不便。该脚本目前实现两个功能：</br>
1、按照时间截取日志；</br>
2、给所有SQL加上时间戳。</br>

### 二、使用方法
假如按照指定时间来截取日志：</br>
python log.py -b '170327  1:30:00' -e '170327  2:30:00' -f '/data/opdir/mysql.log' -s 1024 -r '/data/opdir/result.log'</br>

# 选项意义
-b:开始截取时间戳（可以不加该选项，默认从头开始）</br>
-e:结束截取时间戳（可以不加该选项，默认到文件结束）</br>
-f:日志路径</br>
-r:输出文件路径</br>
-s:一次读取的字节数</br>
