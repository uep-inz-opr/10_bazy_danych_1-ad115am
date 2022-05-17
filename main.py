import pandas as pd
import sqlite3
print(pd.__version__)
if __name__ == "__main__":
    # 'polaczenia_duze.csv'
    def calculate_sum_of_calls():
        filename = input()
        sqlite_con = sqlite3.connect(":memory:")
        cursor = sqlite_con.cursor()
        cursor.execute('''CREATE TABLE polaczenia (from_subscriber data_type INTEGER, 
                          to_subscriber data_type INTEGER, 
                          datetime data_type timestamp, 
                          duration data_type INTEGER , 
                          celltower data_type INTEGER);''')

        df = pd.read_csv(filename, sep=';')
        df.to_sql(name='polaczenia', con=sqlite_con, if_exists='append', index=False)
        sqlite_con.commit()
        cursor.execute('SELECT sum(duration) FROM polaczenia ')
        result = cursor.fetchone()[0]
        print(result)

    calculate_sum_of_calls()
