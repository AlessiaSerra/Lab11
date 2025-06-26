from database.DB_connect import DBConnect
from database import Prodotto as p


class DAO():
    def getColours(self):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        res = []
        query = """select distinct Product_color
                from go_products gp"""

        cursor.execute(query)

        for row in cursor:
            res.append(row['Product_color'])
        cursor.close()
        conn.close()
        return res


    def getProdottiColore(self, colore):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []
        query = """select *
            from go_products gp 
            where Product_color = %s"""

        cursor.execute(query, (colore,))

        for row in cursor:
            res.append(p.Prodotto(**row))

        cursor.close()
        conn.close()
        return res


    def getSales(self, p1, p2, anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []
        query = """ select count(distinct s1.Date) as c
                from go_daily_sales s1, go_daily_sales s2
                where year(s1.Date) = %s and
                    s1.Retailer_code = s2.Retailer_code and
                    s1.Product_number = %s and
                    s2.Product_number = %s and
                    s1.Date = s2.Date"""

        cursor.execute(query, (anno, p1, p2))

        for row in cursor:
            res.append(row['c'])

        cursor.close()
        conn.close()
        return res[0]



