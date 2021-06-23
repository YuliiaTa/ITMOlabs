import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS tab_company(
   ID_comp INT UNIQUE,
   name TEXT);""")

cur.execute("INSERT INTO tab_company VALUES (1, 'Luftbanda');")
cur.execute("INSERT INTO tab_company VALUES (2, 'Russianairways');")
cur.execute("INSERT INTO tab_company VALUES (3, 'Gamma');")
cur.execute("INSERT INTO tab_company VALUES (4, 'Allgreenlandia');")

cur.execute("""CREATE TABLE IF NOT EXISTS tab_trip(
   trip_no INT UNIQUE,
   ID_comp INT,
   plane TEXT,
   town_from TEXT,
   town_to TEXT,
   time_out TIME,
   time_in TIME);""")

cur.execute("INSERT INTO tab_trip VALUES (123, 1, 'Bong', 'Moscow', 'Berlin', '10:05', '13:20');")
cur.execute("INSERT INTO tab_trip VALUES (234, 2, 'ANT', 'SPb', 'Vladivostok', '11:20', '19:50');")
cur.execute("INSERT INTO tab_trip VALUES (345, 3, 'IL', 'Moscow', 'New-York', '20:15', '06:45');")
cur.execute("INSERT INTO tab_trip VALUES (456, 4, 'TU', 'SPb', 'Amsterdam', '23:05', '02:10');")
cur.execute("INSERT INTO tab_trip VALUES (567, 1, 'Airbus', 'Moscow', 'Drezden', '16:35', '19:55');")
cur.execute("INSERT INTO tab_trip VALUES (678, 2, 'YAK', 'SPb', 'Minvody', '09:10', '11:00');")

conn.commit()

companies = cur.execute("""SELECT name,
    SUM(
        CASE WHEN (strftime('%s', time(time_in)) - strftime('%s', time(time_out))) / 60 > 0
             THEN (strftime('%s', time(time_in)) - strftime('%s', time(time_out))) / 60
             ELSE (strftime('%s', time(time_in)) - strftime('%s', time(time_out))) / 60 + 1440
        END
        ) AS flight_time
    FROM tab_trip,tab_company
    WHERE tab_trip.ID_comp = tab_company.ID_comp
    GROUP BY name ORDER BY flight_time;""")

for c in companies:
    print(c)