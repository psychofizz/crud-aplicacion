import dearpygui.dearpygui as dpg

from mssql import check_mssql_connection
from postgresql import check_postgresql_connection

dpg.create_context()

List = ["Postgresql","MySQL","Microsoft SQL Server"]

def radio_button_callback(sender, app_data):
    print(f"Selected option: {app_data}")
    
def get_user_fields_select_db(sender, app_data):
    ip_address = dpg.get_value("fieldIpAddress")
    print(ip_address)
    port_db = dpg.get_value("fieldPort")
    print(port_db)
    username_db = dpg.get_value("fieldUsername")
    print(username_db)
    password_db = dpg.get_value("fieldPassword")
    print(password_db)
    db_select = dpg.get_value("radioDb")
    print(db_select)
    
    if db_select == "Postgresql":
        print("Processing with PostgreSQL")
        if check_postgresql_connection(ip_address,port_db,username_db,password_db) == 0:
            dpg.set_value("connectionTag","Conexion establecida con Postgresql Establecida")
        else: 
            dpg.set_value("connectionTag","Conexion establecida con Postgresql fallida")
    elif db_select == "MySQL":
        print("Processing with MySQL")
    elif db_select == "Microsoft SQL Server":
        print("Processing with Microsoft SQL Server")
        if check_mssql_connection(ip_address,port_db,username_db,password_db) == 0:
            dpg.set_value("connectionTag","Conexion establecida con SQL Server Establecida")
        else: 
            dpg.set_value("connectionTag","Conexion establecida con SQL Server fallida")
    else:
        print("Unsupported database option")
    

with dpg.window(label="Window", tag="window"):
    
    with dpg.tab_bar(tag="test_tab_bar") as tb:
        
        with dpg.tab(label="Ingreso de datos", tag="test_tab_1"):
            
            dpg.add_text("Seleccione su base de datos")
    
            dpg.add_radio_button(List,default_value=None, tag="radioDb",callback=radio_button_callback)
    
            dpg.add_text("Agregue informacion para conectarse con la base de datos")
    
            dpg.add_text("Direccion de IP")     
            dpg.add_input_text(tag="fieldIpAddress")
    
            dpg.add_text("Puerto")
            dpg.add_input_text(tag="fieldPort")
    
            dpg.add_text("Usuario de la db")
            dpg.add_input_text(tag="fieldUsername")
    
            dpg.add_text("Contrasenia")
            dpg.add_input_text(tag="fieldPassword")
    
            dpg.add_button(label="Hola Mundo", tag="btnChequeo", callback=get_user_fields_select_db)
        
        with dpg.tab(label="Ingreso de datos", tag="test_tab_2"):
            
            dpg.add_text("Mundo")
            
        with dpg.tab(label="tab 3", tag="test_tab_3"):
            
            dpg.add_text("Hello")

dpg.create_viewport(title='CRUD con base de datos', width=800, height=600)
dpg.set_primary_window("window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()