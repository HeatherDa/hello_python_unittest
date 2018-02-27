import sqlite3

db_url = 'mileage.db'   # Assumes the table miles have already been created.

def add_miles(vehicle, new_miles):
    '''If the vehicle is in the database, increment the number of miles by new_miles
    If the vehicle is not in the database, add the vehicle and set the number of miles to new_miles

    If the vehicle is None or new_miles is not a positive number, raise Error
    '''

    if not vehicle:
        raise Exception('Provide a vehicle name')
    else:
        vehicle = vehicle.upper()
    #if isinstance(new_miles, float) or new_miles < 0:
    if new_miles < 0:
        raise Exception('Provide a positive number for new miles')

    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    rows_mod = cursor.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (new_miles, vehicle))
    if rows_mod.rowcount == 0:
        cursor.execute('INSERT INTO MILES VALUES (?, ?)', (vehicle, new_miles))
    conn.commit()
    conn.close()





def search_vehicle(name):
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    name = name.upper()
    rows = cursor.execute('SELECT * FROM Miles WHERE vehicle = ? ', (name,))
    cursor.row_factory=sqlite3.Row
    if rows.rowcount == 0:
        conn.close()
        return None
    else:
        for r in rows:
            miles = r['total_miles']
            conn.close()
            return miles

def main():
    while True:
        choice = input('1. update miles \n2. search for miles \n3. delete')
        vehicle = input('Enter vehicle name or enter to quit')
        vehicle = vehicle.upper()
        if len(vehicle)==0:
            break
        elif choice == '1':
            miles = input('Enter new miles for %s' % vehicle)

            if is_float(miles):
                miles = float(miles)
                add_miles(vehicle, miles)

        elif choice == '2':
            miles = search_vehicle(vehicle)
            if miles == None:
                print('This vehicle is not in the database')
            else:
                print(vehicle.upper() + ' has been driven ', miles, ' miles.')

        elif choice == '3':
            delete(vehicle)


def delete(name):
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM MILES WHERE vehicle = ?', (name,))
    conn.commit()
    conn.close()


def is_float(n):
    st = ''
    for char in n:
        if (char.isnumeric()) | (char == '.'):
            st += char
        else:
            print('not a number')
            return False
    return True


if __name__ == '__main__':
    main()
