import sqlite3

def test_db_insert():
    try:
        conn = sqlite3.connect('bike_db.db')
        cursor = conn.cursor()

        # Sample dummy values
        brand_name = "Honda"
        owner = 1
        kms_driven = 25000
        age = 4
        power = 110
        predicted_price = 65000

        # Insert query
        cursor.execute("""
            INSERT INTO bike_prediction 
            (brand_name, owner, kms_driven, age, power, predicted_price)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (brand_name, owner, kms_driven, age, power, predicted_price))

        conn.commit()
        print("✅ Data inserted successfully!")

        # Optional: verify insertion
        cursor.execute("SELECT * FROM bikes_prediction ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        print("Last inserted row:", row)

    except sqlite3.Error as e:
        print("❌ SQLite error:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()

test_db_insert()