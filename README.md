https://www.msn.com/en-us/lifestyle/shopping/best-affordable-headphones-2024/ar-BB1i47K9?ocid=msedgntp&pc=DCTS&cvid=666f1c82c9834566a3a69e3b698c1555&ei=7



ご旅程表
観光庁長官登録旅行業 第 64 号
(一社)日本旅行業協会正会員
株式会社 JTB
熊本支店
〒860-0807 熊本県熊本市下通 1-8-22 ＪＴＢ熊本ビル 2F
TEL：096-322-4115／FAX：096-325-8105
営業時間:9：30～17：30／定休日:土曜日・日曜日・祝日
支店長：島添 哲也
総合旅行業務取扱管理者：鍔 智之
担当者：大谷 祐人
作成日：2024 年 2 月 22 日
株式会社 ARIAKE 様
ご 旅 行 方 面 ： 関西 ご参加人数： 40 名様（添乗員 1 名）
ご 旅 行 期 間 ： 2024 年 5 月 23 日（木）～25 日（土） ご集合場所： 熊本空港
日次 月日曜 行程 食事
1
5/23
or
5/30
(木)
 JAL2382 
熊本空港 ✈✈✈✈✈✈ 伊丹空港 ═══ 昼食（南京町）・・・・・ 自由散策 ═══
8:00 9:15 10:20 10:50 12:15 13:15 14:00
══ ROKKO 森のミュージアム ════ ホテル ・・・・・ 有馬温泉街（※自由散策）・・・・・ 夕食（ホテル） 
１5:00 16:30 17:00 19:00
 宿泊：神戸市内 or 有馬温泉街ホテル
朝：－
昼：○
夕：〇
2
5/24
or
5/31
(金)
 
ホテル ════ ユニバーサルスタジオジャパン ════ ホテル
8:00 10:00 19:30 21:30
 宿泊：神戸市内 or 有馬温泉街ホテル
朝： ○
昼：（各自）
夕：（各自）
3
5/25
or
6/1
(土)
 
ホテル ═════ 阪神甲子園球場(スタジアムツアー) ═══ 昼食 ═══
 09:30 10:30 12:00 12:30 13:30
 
 
 JAL2389 
═══ カップヌードルミュージアム池田大阪 ═══ 伊丹空港 ✈✈✈✈✈✈ 熊本空港
14:00 15:30 16:00 17：35 18:45 19：20
朝：○
昼：○
夕：－
＜凡 例＞ ◎は入場観光／○は下車観光／△は車窓観光 ＜記入例＞ 鉄道◧◧◧ 航空機✈✈✈ 私鉄╪╪╪╪ バス═══ 船～～～ ケーブルカー≂≂≂ ロープウェイ≂≂≂ 徒歩････ タクシー／乗用車――
＜記 号＞ (指)普通車指定席、(自)普通車自由席、(G)グリーン車、(普)普通席、ｴｺﾉﾐｰ、ﾌｧｰｽﾄ、ｸﾗｽ J、ﾌﾟﾚﾐｱﾑｸﾗｽ、(直)直行便、(乗)乗継便、(経)経由便
＜お願い＞ この旅程は運輸機関のダイヤ改正および各地の道路状況により、多少時間が変更になる場合がございますのでお手数でも現地での出発時間をご確認ください。
旅行代金（概算費用）
お 1 人様あたり：85,000～125,000 円（40 名参加の場合）
旅行代金に含まれるもの
航空券代・各施設観光入場料・貸切バス代（大型 1 台/ガイドあり/有料道路代・乗務員費用等含む）
宿泊代（1 室 1 名利用）
行程表記載の食事（朝 2 回・昼 2 回・夕 1 回）
※夕食時飲み放題含む
注 1）食事時の飲み物代は含まれておりませんので、予めご了承ください。
注 2）2/22 現在の空き状況となります。
ゴルフ・ＵＳＪ・観光ツアー


28/02/2023
CAST(DateTime AS TIME) < '08:30:00' DELETE FROM mem
WHERE CAST(DateTime AS TIME) < '08:30:00' and CAST(DateTime AS TIME) > '17:15:00';
0 rows affected

-------------------------------------

DELETE FROM mem
WHERE DateTime NOT BETWEEN '2023-02-28 08:30:00' AND '2023-02-28 17:15:00';


\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\





i have 3 csv files. one is application server cpu data, one is database server cpu data and the last one is file server cpu data. each csv file contains 3 columns-date-time column,cpu using rate and server name. how do i show each day of  aprils avg and max cpu using rate in a table using sql management server. also show the dates from date time column in the first column in the combied table
ChatGPT
Certainly! If you want to display each day of April's average and maximum CPU usage for each server type in a combined table, you can modify the script as follows:

sql
Copy code
-- Create a combined table
CREATE TABLE CombinedServerData (
    ServerType NVARCHAR(255),
    DateColumn DATETIME,
    AvgCPURate FLOAT,
    MaxCPURate FLOAT
);

-- Insert data from Application Server
INSERT INTO CombinedServerData (ServerType, DateColumn, AvgCPURate, MaxCPURate)
SELECT 
    'Application Server' AS ServerType, 
    DateColumn, 
    AVG(CPURate) AS AvgCPURate, 
    MAX(CPURate) AS MaxCPURate
FROM 
    ApplicationServerData
WHERE 
    MONTH(DateColumn) = 4
GROUP BY 
    DateColumn;

-- Insert data from Database Server
INSERT INTO CombinedServerData (ServerType, DateColumn, AvgCPURate, MaxCPURate)
SELECT 
    'Database Server' AS ServerType, 
    DateColumn, 
    AVG(CPURate) AS AvgCPURate, 
    MAX(CPURate) AS MaxCPURate
FROM 
    DatabaseServerData
WHERE 
    MONTH(DateColumn) = 4
GROUP BY 
    DateColumn;

-- Insert data from File Server
INSERT INTO CombinedServerData (ServerType, DateColumn, AvgCPURate, MaxCPURate)
SELECT 
    'File Server' AS ServerType, 
    DateColumn, 
    AVG(CPURate) AS AvgCPURate, 
    MAX(CPURate) AS MaxCPURate
FROM 
    FileServerData
WHERE 
    MONTH(DateColumn) = 4
GROUP BY 
    DateColumn;

-- Query the combined table
SELECT 
    ServerType,
    DateColumn,
    AvgCPURate,
    MaxCPURate
FROM 
    CombinedServerData
ORDER BY 
    ServerType, DateColumn;
This script creates a new table named CombinedServerData and inserts the relevant data from each server table for each day in April. The final query retrieves the average and maximum CPU rates for each server type on each day in April.

Make sure to adjust the column and table names as needed based on your actual database structure and CSV file contents.


--------------------------------------------------------------------------
SELECT DATE(timestamp_column) AS date_only
FROM your_table
WHERE timestamp_column >= '2024-02-01' AND timestamp_column < '2024-03-01';


...............Replace timestamp_column with the actual name of your timestamp column, and your_table with the name of your table.

In this example, the DATE(timestamp_column) function extracts the date part from the timestamp. The WHERE clause filters the data for the month of February 2024. Adjust the date range in the WHERE clause based on your requirements.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

SELECT
  CONCAT(MIN(your_column) * 100, '% - ', MAX(your_column) * 100, '%') AS percentage_range,
  COUNT(*) AS count_of_records
FROM
  your_table
GROUP BY
  NTILE(10); -- Divide the data into 10 percentiles, you can adjust this value as needed

-------------------------------remove last col od df ---------------------
df.drop(columns=df.columns[-1],  axis=1,  inplace=True)
or
df.pop(df.columns[-1])







