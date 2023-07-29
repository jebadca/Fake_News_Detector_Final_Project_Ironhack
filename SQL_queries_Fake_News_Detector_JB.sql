#Creating the schema before using the Table Import Wizard

#CREATE TABLE df_sql (
    #id INT AUTO_INCREMENT PRIMARY KEY, 
    #date DATE,
    #target INT, 
    #text_length INT
#);

#Querying the number of fake news per month & year
SELECT 
    YEAR(date) AS Year,
    MONTH(date) AS Month,
    COUNT(*) AS FakeNewsCount
FROM 
    df_sql
WHERE 
    target = 1
GROUP BY 
    YEAR(date),
    MONTH(date)
ORDER BY
    Year ASC,
    Month ASC;

#Querying the text length per year per target
SELECT 
    YEAR(date) AS Year,
    target,
    AVG(text_length) AS AvgTextLength
FROM 
    df_sql
GROUP BY 
    YEAR(date),
    target
ORDER BY
    Year ASC,
    target ASC;