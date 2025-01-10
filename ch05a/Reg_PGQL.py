import psycopg2
import psycopg2.extras

try:

    with psycopg2.connect(database = "fcms", 
                            user = "reg", 
                            host= 'localhost',
                            password = "reg",
                            port = 5432) as fconn:

        print ("---> conectado:", fconn)

        with fconn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute ('DROP TABLE IF EXISTS cliente')

            create_script = ''' CREATE TABLE cliente (
                                    id      int PRIMARY KEY,
                                    nome    varchar(40) NOT NULL,
                                    ranking int,
                                    casa_id varchar
            )'''

            cur.execute(create_script)

            insert_script = 'INSERT INTO cliente (id, nome, ranking, casa_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'reg1', 5, '05140 000'), 
                            (2, 'reg12', 6, '05140 001'), 
                            (3, 'reg123', 7, '05140 002'), 
                            (4, 'reg1234', 8, '05140 003')]

            for registro in insert_values:
                cur.execute (insert_script, registro)

            cur.execute ('SELECT * FROM cliente')
            for registro in cur.fetchall():
                print (registro['nome'], registro['casa_id'], registro['ranking'])
            print ("***")

            

            update_script = 'UPDATE cliente SET ranking=ranking + 3'
            cur.execute (update_script)
            
            delete_script = 'DELETE FROM cliente WHERE nome = %s'
            delete_value = ('reg1',)
            cur.execute(delete_script, delete_value)
            

            cur.execute ('SELECT * FROM cliente')
            for registro in cur.fetchall():
                print (registro['nome'], registro['casa_id'], registro['ranking'])

        fconn.commit()
            
except Exception as error:
    print (error)

finally:
    if fconn is not None:
        fconn.close()

