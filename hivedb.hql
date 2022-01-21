create external table if not exists countries_list1(CountryID int, CountryName string, Capital string, Population string) comment 'List of Countries' row format delimited fields terminated by ',' stored as textfile location 'gs://anuj-suchchal-bucket/input';
create table if not exists countries_managed1 (CountryID int, CountryName string, Capital string, Population string) comment 'List of Countries';
insert overwrite table countries_managed select * from countries_list1;
insert overwrite directory 'gs://anuj-suchchal-bucket/output' row format delimited fields terminated by ',' stored as textfile select * from countries_managed;
