import os
import pyodbc
import pandas as pd
import psycopg2

db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")

print(db_host)

class AqarRecommendation:
    def __init__(self, montly_salary = 18750, input_district = 'الرياض', input_rooms = 4):
        # input from user 
        self.montly_salary = float(montly_salary)
        self.input_district = input_district
        self.input_rooms = int(input_rooms)
        # connect to postgres
        try: 
            self.conn = psycopg2.connect("hostdb_host dbname=db_name user=db_user password=db_password")
            print("Connected")
        except psycopg2.Error as e: 
            print("Error: Could not make connection to the Postgres database")
            print(e)

        try: 
            self.cur = self.conn.cursor()
        except psycopg2.Error as e: 
            print("Error: Could not get curser to the Database")
            print(e)
        self.conn.set_session(autocommit = "True")
    
    def get_recommended_price(self, montly_salary):
        recommended_price = int((montly_salary*12) * 0.20)
        print("test",recommended_price)
        return recommended_price

    def recommend_aqar(self, montly_salary, input_district, input_rooms, saudi_aqar_riyadh):
        input_price = self.get_recommended_price(montly_salary)
        # 1- Filter on exact values.
        test_result = saudi_aqar_riyadh.loc[ (saudi_aqar_riyadh['city'] == input_district) \
                                  & (saudi_aqar_riyadh['price'] == input_price) \
                                  & (saudi_aqar_riyadh['bedrooms'] == input_rooms) ]
        print("come one")
        print(input_price)
        if len(test_result) == 0:
            # 2- If no results show up, Filter on approximate price.
            test_result = saudi_aqar_riyadh.loc[ (saudi_aqar_riyadh['city'] == input_district) \
                                    & (saudi_aqar_riyadh['price'] <= input_price+10000) \
                                    & (saudi_aqar_riyadh['price'] >= input_price-10000) \
                                    & (saudi_aqar_riyadh['bedrooms'] == input_rooms) ]
        if len(test_result) == 0:
            # 3- If no results, or want to search more, filter on approximate rooms.
            test_result = saudi_aqar_riyadh.loc[ (saudi_aqar_riyadh['city'] == input_district) \
                                    & (saudi_aqar_riyadh['price'] <= input_price +10000) \
                                    & (saudi_aqar_riyadh['price'] >= input_price -10000) \
                                    & (saudi_aqar_riyadh['bedrooms'] >= input_rooms -1) \
                                    & (saudi_aqar_riyadh['bedrooms'] <= input_rooms +1)]
        else:
            print('No results are found')
        
        ad_list = list(test_result['id'])
        
        return ad_list
    
    def main(self):
    
        # insert data into df
        # removed 'front' from the DF to match number of columns returned by the database
        saudi_aqar = pd.DataFrame(columns =['city', 'district', 'front', 'size', 'property_age', 'bedrooms', 'bathrooms', 'livingrooms', 'kitchen', 'garage', 'driver_room', 'maid_room', 'furnished', 'ac', 'roof', 'pool', 'frontyard', 'basement', 'duplex', 'stairs', 'elevator', 'fireplace', 'price', 'id'])

        try: 
            self.cur.execute("SELECT * FROM saudi_aqar;")
        except psycopg2.Error as e: 
            print("Error: select *")
            print (e)

        row = self.cur.fetchone()
        while row:
           #print(row)
           saudi_aqar.loc[len(saudi_aqar.index)] = row
           row = self.cur.fetchone()

        # read data into df

        # strip city and filter n Riyadh ads only
        saudi_aqar['city'] = saudi_aqar['city'].str.strip()
        #saudi_aqar_riyadh = saudi_aqar.loc[saudi_aqar['city'] == 'الرياض']
            
        # executing the main recommendation function 
        print("salary:",self.montly_salary)
        print(self.input_district)
        print(self.input_rooms)
        #print(saudi_aqar_riyadh)
        recommended_aqar = self.recommend_aqar(self.montly_salary, self.input_district, self.input_rooms, saudi_aqar)
        column = ['أفضل العروض اللي تناسبك:' + str(recommended_aqar)]
        print(column)
        if len(recommended_aqar) == 0:
            recommended_aqar = 'لم اجد خيار مناسب حاول بمدخلات اخرى'
        return column


if __name__ == 'main':
    rec = AqarRecommendation(18750, 'الرياض', 4)
    rec.main()
