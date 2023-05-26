import sqlite3

def create_connection(db_file):
    #create a database connection to the SQLite database
    #return: Connection object or None
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn


def insert_db(conn,table, columns,data):
    col = ",".join(columns)
    fill = tuple(data)
    unknow=["?"]*len(columns)
    x=",".join(unknow)
    sql = f''' INSERT INTO {table} ({col}) VALUES({x})'''
    conn.execute(sql,fill)
    conn.commit()


def create_table(conn,table, columns):
    col = ",".join(columns)
    sql = f'''CREATE TABLE IF NOT EXISTS {table}( id INTEGER PRIMARY KEY, {col});'''
    conn.execute(sql)


def update_keys(conn,table,coll,new_val,curr_val):
    cur=conn.cursor()
    com = f"UPDATE {table} SET {coll} = '{new_val}' WHERE {coll} = '{curr_val}'"
    try:
        cur.execute(com)

        conn.commit()

    except:

        print('error')
        conn.rollback()

def select_db(conn,table,columns_and_data=None):
    if not columns_and_data==None:
        col = " AND ".join(columns_and_data)
        sql=f'''SELECT * FROM {table} WHERE {col}'''
        #where 4 is the id i am looking for
        return conn.execute(sql)
    else:
        sql =f"SELECT * from {table}"
        return conn.execute(sql)
    
    
def select__db_f_l(conn,table,first_name,last_name):
    sql=f"SELECT * FROM {table} WHERE first=? AND last=?"
    return conn.execute(sql,(first_name,last_name)) 


def select__db_array(conn,table,name):
    sql=f"SELECT {name} FROM {table}"
    return conn.execute(sql) 


def tuple_list(list): 
    new_list = []
    for element in list:
        new_list.append(element[0])
    return new_list


def delete_db(conn,table,column,what_to_remove):
    sql=f'''DELETE FROM {table} WHERE {column} = ?''',(what_to_remove,)
    conn.execute(sql)
    conn.commit()  
    
    
connection = create_connection('game_data.db')
create_table(connection,"Player_Save_Info",["Save_Number INTEGER","Play_Time FLOAT", "Player_Hp INTEGER","Player_Max_Hp INTEGER","Player_Dmg_Mult FLOAT","P_Loc_X INTEGER","P_Loc_Y INTEGER","Slash_Unlock BOOLEAN","Sprint_Unlock BOOLEAN","Djump_Unlock BOOLEAN","Shoot_Unlock BOOLEAN"])   
create_table(connection,"Keybinds", ["LEFT STRING","RIGHT STRING","JUMP STRING","CROUCH STRING","ATTACK STRING","SPRINT STRING"])


#def save_initial():
#    insert_db(connection,"Player_Save_Info",["Save_Number","Play_Time", "Player_Hp","Player_Max_Hp","Player_Dmg_Mult","P_Loc_X","P_Loc_Y","Slash_Unlock","Sprint_Unlock","Djump_Unlock","Shoot_Unlock"],[int(1),float(0.00),int(5),int(5),float(0.0),int(0),int(0),bool(False),bool(False),bool(False),bool(False)])
#    insert_db(connection,"Player_Save_Info",["Save_Number","Play_Time", "Player_Hp","Player_Max_Hp","Player_Dmg_Mult","P_Loc_X","P_Loc_Y","Slash_Unlock","Sprint_Unlock","Djump_Unlock","Shoot_Unlock"],[int(2),float(0.00),int(5),int(5),float(0.0),int(0),int(0),bool(False),bool(False),bool(False),bool(False)])
#    insert_db(connection,"Player_Save_Info",["Save_Number","Play_Time", "Player_Hp","Player_Max_Hp","Player_Dmg_Mult","P_Loc_X","P_Loc_Y","Slash_Unlock","Sprint_Unlock","Djump_Unlock","Shoot_Unlock"],[int(2),float(0.00),int(5),int(5),float(0.0),int(0),int(0),bool(False),bool(False),bool(False),bool(False)])
#save_initial
#def keys_initial():
#    insert_db(connection,"Keybinds",["LEFT","RIGHT","JUMP","CROUCH","ATTACK","SPRINT"],["A","D","SPACE","LEFT CTRL","E","LEFT SHIFT"])
#keys_initial()
