import psycopg2

def check_postgresql_connection(server,port,username,password):
    print("Se va a conectar a Postgresql")
    
    try:
        connection = psycopg2.connect(
            host=server,
            port=port,
            user=username,
            password=password,
        )

        if connection:
            print("Connection successful!")
            dpg.set_value("connectionTag","Conexion establecida con Postgresql")
            # Perform further actions with the connection if needed

        # Close the connection
        connection.close()

    except psycopg2.Error as error:
        print("Error connecting to PostgreSQL:", error)