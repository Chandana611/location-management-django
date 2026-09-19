from django.db import connection

def get_districts():
    with connection.cursor() as cursor:
        cursor.execute("EXEC dbo.GetDistrictsMaster")

        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

    districts = [
        dict(zip(columns, row))
        for row in rows
    ]

    return districts


def get_taluks(district_id):
    with connection.cursor() as cursor:
        cursor.execute("EXEC dbo.GetTaluksMaster @district_id = %s", 
                       [district_id])

        # columns = [column[0] for column in cursor.description]

        columns = []
        for column in cursor.description:
            columns.append(column[0])


        rows = cursor.fetchall()

        # taluks = [
        #     dict(zip(columns, row))
        #     for row in rows
        # ]

        taluks = []

        for row in rows:
            taluk = dict(zip(columns, row))
            taluks.append(taluk)

        return taluks


def get_hobli(taluk_id):
    with connection.cursor() as cursor:
        cursor.execute("EXEC [dbo].[GetHobliMaster] @taluk_id = %s", [taluk_id])

        columns = []
        for column in cursor.description:
            columns.append(column[0])

        rows = cursor.fetchall()

        hoblis = []
        for row in rows:
            hobli = dict(zip(columns, row))
            hoblis.append(hobli)

        return hoblis


def save_data(name, address, district_id, taluk_id, hobli_id):
    with connection.cursor() as cursor:
        cursor.execute(
            """
                EXEC [dbo].[SaveFormDataa] 
                %s, %s, %s, %s, %s
            """, 
            [
                name,
                address,
                district_id,
                taluk_id,
                hobli_id
            ]
        )

        columns = []
        for column in cursor.description:
            columns.append(column[0])
        row = cursor.fetchone()

        result = dict(zip(columns, row))

        return result


def get_save_data(id):
    with connection.cursor() as cursor:
        cursor.execute("EXEC [dbo].[GetSaveFormData] %s ", [id])
        columns = []

        for column in cursor.description:
            columns.append(column[0])

        row = cursor.fetchone()

        result = dict(zip(columns, row))

        return result