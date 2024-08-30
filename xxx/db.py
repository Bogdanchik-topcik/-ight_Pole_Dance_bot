import sqlite3 as sq

with sq.connect('users.db') as con:
    cur = con.cursor()

    cur.executescript('''CREATE TABLE IF NOT EXISTS messagesID(
                      userID TEXT PRIMARY KEY,
                      mesID TEXT)
                      ''')
    
    def checkDB(id):
        '''Есть ли такой id пользователя? Если нет, то добавляем'''

        res = cur.execute('''SELECT userID FROM messagesID''')
        usersID = res.fetchall()

        if not (str(id),) in usersID:
            cur.execute(f'''INSERT INTO messagesID (userID) VALUES (?)''', (id,))
            con.commit()
    

    def new_mesidDB(mes  # код сообщения
                    ):
        '''Добавляет id новых сообщений'''
    
        newID = mes.message_id
        userID = mes.chat.id
    
        cur.execute(f'''SELECT mesID FROM messagesID 
                    WHERE userID=?''', (userID,))
        mesID = cur.fetchone()[0]
        
        if not mesID is None:
            newID = f'{mesID} {newID}'
        
        cur.execute(f'''UPDATE messagesID SET mesID=?
                    WHERE userID=?''', (newID, userID,))
        con.commit()



    def give_mesidBD(userID: int) -> list:
        '''Достаёт id всех присланных сообщений'''

        cur.execute(f'''SELECT mesID from messagesID WHERE userID={userID}''')
        mesID = cur.fetchone()[0]
        if mesID:
            mesID = mesID.split()  # Получаю список со всеми id
        else:
            mesID = []
        return mesID
    

    def del_mesidDB(userID: int, all = True):
        '''Удаляет все id сообщений'''
        if all:
            cur.execute(f'''UPDATE messagesID SET mesID = NULL 
                        WHERE userID={userID}''')
        else:
            cur.execute(f'SELECT mesID from messagesID WHERE userID={userID}')
            mesID = cur.fetchone()[0]
            mesID = mesID.split()
            mesID = mesID[0]
            cur.execute('''UPDATE messagesID SET mesID = ? 
                        WHERE userID=?''', (mesID, userID))
        con.commit()
