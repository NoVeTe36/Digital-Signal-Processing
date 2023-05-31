import json

table_list = []

# list = [1, 2, 3, 4, 5]
# dictionary = {'ban 1': 10, 'ban 2': 20}

# Thêm bàn vào danh sách bàn
def _insert_table(table_id):
    # Kiểm tra xem bàn đã tồn tại hay chưa
    for table in table_list:
        if table['Table ID'] == table_id:
            print("***Table id already exists***")
            return
    # tạo ra một dictionary mới là 1 bàn
    table_dict = {}
    table_dict['Table ID'] = table_id
    table_list.append(table_dict)
    for i in range(0, len(table_list)):
        if 'Status check-in' not in table_list[i]:
            table_list[i]['Status check-in'] = u'\u2717'
    table_list.sort(key=lambda x: x['Table ID'])
    # check if the wait list is empty or not
    if len(wait_list) != 0:
        guest_phone = wait_list.pop(0)
        for i in range(0, len(table_list)):
            if table_list[i]['Status check-in'] == u'\u2717':
                table_list[i]['Status check-in'] = u'\u2713'
                table_list[i]['Status check-out'] = u'\u2717'
                table_list[i]['Guest phone'] = guest_phone['Guest phone']
                print("***Guest from wait list check-in successfully***")
    print("***Table inserted successfully***")
    return

def _display_all_tables():
    print(json.dumps(table_list, indent=4, ensure_ascii=False))

# u'\u2713' = check mark
# u'\u2717' = cross mark
 
wait_list = [] 
def _check_in():
    guest_phone = input("\nPlease enter the phone number of the guest: ")
    # display_list để hiển thị danh sách bàn sau khi đã check-in
    display_list = []
    print("Table list that not check-in yet:")
    for i in range(0, len(table_list)):
        if table_list[i]['Status check-in'] == u'\u2717':
            display_list.append(table_list[i])
    if len(display_list) == 0:
        print("***Out of tables, move the guest to wait list***")
        if guest_phone == '':
            print("***Guest phone is empty***")
            return
        else:
            wait_dict = {}
            if guest_phone in wait_list:
                print("***Guest phone already exists***")
                return
            wait_dict['Index'] = len(wait_list) + 1
            wait_dict['Guest phone'] = guest_phone
            wait_list.append(wait_dict)
        return
    print(json.dumps(display_list, indent=4, ensure_ascii=False))
    table_id = input("\nPlease enter the table id that guest order: ")
    table_id = table_id.split()
    table_id.sort()
    for i in range(0, len(table_list)):
        for j in range(0, len(table_id)):
            if table_list[i]['Table ID'] == table_id[j]:
                table_list[i]['Status check-in'] = u'\u2713'
                table_list[i]['Status check-out'] = u'\u2717'
                table_list[i]['Guest phone'] = guest_phone
                print("***Guest check-in successfully***")

    

def _check_out():
    display_list = []
    print("Table list after check-in:")
    for i in range(0, len(table_list)):
        if table_list[i]['Status check-in'] == u'\u2713':
            display_list.append(table_list[i])
    if len(display_list) == 0:
        print("***No table is checked-in***")
        return
    print(json.dumps(display_list, indent=4, ensure_ascii=False))
    print("Wait list: ")
    print(json.dumps(wait_list, indent=4, ensure_ascii=False))
    # kiểm tra xem số điện thoaị của khách hàng có tồn tại hay không
    guest_phone = input("\nPlease enter the phone number of the guest: ")
    for i in range(0, len(table_list)):
        # remove all tables that have the same guest phone
        if table_list[i]['Guest phone'] == guest_phone:
            table_list[i]['Status check-in'] = u'\u2717'
            table_list[i]['Status check-out'] = u'\u2713'
            table_list[i]['Guest phone'] = ''
            print("***Guest check-out successfully***")
            if len(wait_list) != 0:
                guest_phone_wait = wait_list.pop(0)
                for i in range(0, len(table_list)):
                    if table_list[i]['Status check-in'] == u'\u2717':
                        table_list[i]['Status check-in'] = u'\u2713'
                        table_list[i]['Status check-out'] = u'\u2717'
                        table_list[i]['Guest phone'] = guest_phone_wait['Guest phone']
                        print("***Guest from wait list check-in successfully\n***")
                        # change the index of wait list
                        for j in range(0, len(wait_list)):
                            wait_list[j]['Index'] -= 1
                            if wait_list[j]['Index'] == -1:
                                wait_list[j]['Index'] = 0
            else:
                print("***Guest phone does not exist***")
                return

def _remove_table():
    # display table list
    _display_all_tables()
    guest_phone = input("\nPlease enter the phone number of the guest: ")
    table_id = input("\nPlease enter the table id that guest order: ")
    table_id = table_id.split()
    table_id.sort()
    for i in range(0, len(table_list)):
        for j in range(0, len(table_id)):
            if table_list[i]['Table ID'] == table_id[j]:
                table_list[i]['Status check-in'] = u'\u2717'
                table_list[i]['Status check-out'] = ''
                table_list[i]['Guest phone'] = ''
                if len(wait_list) != 0:
                    guest_phone = wait_list.pop(0)
                    for i in range(0, len(table_list)):
                        if table_list[i]['Status check-in'] == u'\u2717':
                            table_list[i]['Status check-in'] = u'\u2713'
                            table_list[i]['Status check-out'] = u'\u2717'
                            table_list[i]['Guest phone'] = guest_phone['Guest phone']
                            print("***Guest from wait list check-in successfully***")

def main():
    print("Welcome to the restaurant")
    while True:
        print("\n1. Add tables")
        print("2. Display all tables")
        print("3. Guest check-in")
        print("4. Guest check-out")
        print("5. Remove table")
        print("6. Exit")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            number = int(input("\nPlease enter the number of tables: "))
            for i in range(0, number):
                print("--------------------------------------------------------")
                table_id = input("\nPlease enter the id of the table " + str(i+1) +": ")
                _insert_table(table_id)

        elif choice == 2:
            _display_all_tables()

        elif choice == 3:
            _check_in()

        elif choice == 4:
            _check_out()

        elif choice == 5:
            _remove_table()

        elif choice == 6:
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()