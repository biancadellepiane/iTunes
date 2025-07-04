from database.DB_connect import DBConnect
from model.album import Album


class DAO():

    @staticmethod
    def getAllNodes(durata):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select a.*, sum(t.Milliseconds)/1000/60 as dTot
                    from album a , track t 
                    where a.AlbumId = t.AlbumId 
                    group by a.AlbumId 
                    having dTot > %s"""

        cursor.execute(query,(durata,))

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select distinctrow t.AlbumId as a1, t2.AlbumId as a2
                    from playlisttrack p , playlisttrack p2 , track t , track t2 
                    where p.trackId = t.trackId and p2.TrackId = t2.TrackId 
                    and t.AlbumId < t2.AlbumId and p.PlaylistId = p2.PlaylistId """

        cursor.execute(query)

        for row in cursor:
            if row["a1"] in idMap and row["a2"] in idMap:
                result.append((idMap[row["a1"]], idMap[row["a2"]]))

        cursor.close()
        conn.close()
        return result
