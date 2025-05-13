from database.DB_connect import DBConnect
from model import Prodotto as p
from model import Sale as s

class DAO():
    def getColours(self):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        res = []
        query = """select distinct Product_color
                    from go_products 
                    where Product_color != 'Unspecified'"""

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
                    from go_products 
                    where Product_color = %s"""

        cursor.execute(query, (colore,))

        for row in cursor:
            res.append(p.Prodotto(**row))

        cursor.close()
        conn.close()
        return res

    # def getArchi(self, colore, anno):
    #     conn = DBConnect.get_connection()
    #     cursor = conn.cursor(dictionary=True)
    #     res = []
    #     query = """
    #             """
    #
    #     cursor.execute(query, (colore,))
    #
    #     for row in cursor:
    #         res.append(p.Prodotto(**row))
    #
    #     cursor.close()
    #     conn.close()
    #     return res

    def getSalesColore(self, prodotti_colore):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []
        query = """select *
                from go_daily_sales
                        """

        cursor.execute(query)

        for row in cursor:
            if row['Product_number'] in prodotti_colore:
                res.append(s.Sale(**row))

        cursor.close()
        conn.close()
        return res



