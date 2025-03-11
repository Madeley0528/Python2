def conectar (Consulta_sql):
    #Modulo para concetar con base de datos sql
    import mysql.connector
    
    #Credenciales para la conexion
    config = {
        'user': 'us7wj5xw2oxjvwzt',
        'password':'DbeFLFamrWgMyuL8NvFp',
        'host':'bepj2a0dsxg3jaxcxwwe-mysql.services.clever-cloud.com',
        'database':'bepj2a0dsxg3jaxcxwwe',
        'raise_on_warnings': True
    }
    
    #Conectar a la base de datos
    try: 
        conexion = mysql.connector.connect(**config)
        print("Conexion exitosa a la base de datos")
        
        #Objeto para crear consultas 
        consultas = conexion.cursor()
        
        #Funcion para agregar la consulta sql 
        consultas.execute(Consulta_sql)

        #Almacena el resultao de la consulta SQL
        resultado = consultas.fetchall()

        return resultado
    
    #Respuesta si al conectar da error
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
