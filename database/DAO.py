from database.DB_connect import DBConnect
from model.chromosome import Chromosome


class DAO():
    def __init__(self):


        pass

    @staticmethod
    def getAllChromosomes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """
        SELECT DISTINCT g.Chromosome 
        FROM genes g 
        WHERE g.Chromosome != 0
        """

        cursor.execute(query)

        for row in cursor:
            result.append(Chromosome(row["Chromosome"]))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getAllConnections(idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """
        with distinctChromosomes as (
        SELECT g.Chromosome, g.GeneID 
        FROM genes g 
        WHERE g.Chromosome != 0
        )
        SELECT ds1.Chromosome as Chromosome1, 
        ds2.Chromosome as Chromosome2,
        sum(DISTINCTROW i.Expression_Corr) as TotExprCorr
        FROM distinctChromosomes ds1, distinctChromosomes ds2, interactions i 
        WHERE ds1.Chromosome != ds2.Chromosome
        and ds1.GeneID = i.GeneID1 
        and ds2.GeneID = i.GeneID2 
        group by ds1.Chromosome, ds2.Chromosome 
        """

        cursor.execute(query)

        for row in cursor:
            if row["Chromosome1"] in idMap and row["Chromosome2"] in idMap:
                result.append([idMap[row["Chromosome1"]], idMap[row["Chromosome2"]], row["TotExprCorr"]])

        cursor.close()
        conn.close()

        return result
