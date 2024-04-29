'''

Q) Write a query to find the address (location_id, street_address, city, state_province,country_name) of Canada using join in Python 
   (Input -We Can create a  table in FrontEnd like using variables)

'''



import mysql.connector as sqltor

# Establishing connection to MySQL server 
mycon = sqltor.connect(host="localhost", user="root", passwd="123098Abc@", database="SaferTech_Backend")

#  cursor object
cursor = mycon.cursor()

# The 'countries' table is created
cursor.execute("""
CREATE TABLE IF NOT EXISTS countries (
    country_id VARCHAR(2) PRIMARY KEY,
    country_name VARCHAR(50),
    region_id INT
)
""")

# The 'locations' table is created with a foreign key
cursor.execute("""
CREATE TABLE IF NOT EXISTS locations (
    location_id INT PRIMARY KEY,
    street_address VARCHAR(255),
    postal_code VARCHAR(20),
    city VARCHAR(100),
    state_province VARCHAR(100),
    country_id VARCHAR(2),
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
)
""")

# Inserting data into 'countries'
countries_data = [
    ('AR', 'Argentina', 2),
    ('AU', 'Australia', 3),
    ('BE', 'Belgium', 1),
    ('BR', 'Brazil', 2),
    ('CA', 'Canada', 2),
    ('CH', 'Switzerland', 1),
    ('CN', 'China', 3),
    ('DE', 'Germany', 1),
    ('IT', 'Italy', 1),  # Added Italy
    ('JP', 'Japan', 3),  # Added Japan
    ('US', 'United States', 2)  # Added United States
]

cursor.executemany("INSERT INTO countries (country_id, country_name, region_id) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE country_name=VALUES(country_name), region_id=VALUES(region_id)", countries_data)

# Inserting data into 'locations'
locations_data = [
    (1000, '1297 Via Cola di Rie', '989', 'Roma', None, 'IT'),
    (1100, '93091 Calle della Te', '10934', 'Venice', None, 'IT'),
    (1200, '2017 Shinjuku-ku', '1689', 'Tokyo', 'Tokyo Prefecture', 'JP'),
    (1300, '9450 Kamiya-cho', '6823', 'Hiroshima', None, 'JP'),
    (1400, '2014 Jabberwocky Rd', '26192', 'Southlake', 'Texas', 'US'),
    (1500, '2011 Interiors Blvd', '99236', 'South Sen', 'California', 'US'),
    (1600, '2007 Zagora St', '50090', 'South Brun', 'New Jersey', 'US'),
    (1700, '2004 Charade Rd', '98199', 'Seattle', 'Washington', 'US'),
    (1800, '147 Spadina Ave', 'M5V 2L7', 'Toronto', 'Ontario', 'CA')
]

cursor.executemany("INSERT INTO locations (location_id, street_address, postal_code, city, state_province, country_id) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE street_address=VALUES(street_address), postal_code=VALUES(postal_code), city=VALUES(city), state_province=VALUES(state_province), country_id=VALUES(country_id)", locations_data)

# Commit the changes
mycon.commit()

# Query to find addresses in Canada using a join
query = """
SELECT 
    l.location_id, 
    l.street_address, 
    l.city, 
    l.state_province, 
    c.country_name
FROM 
    locations l
JOIN 
    countries c ON l.country_id = c.country_id
WHERE 
    c.country_name = 'Canada';
"""

cursor.execute(query)
results = cursor.fetchall()

# Printing  results
for result in results:
    print("Location ID:", result[0])
    print("Street Address:", result[1])
    print("City:", result[2])
    print("State/Province:", result[3])
    print("Country Name:", result[4])
    print("-----------")

# Close the cursor and the connection
cursor.close()
mycon.close()
