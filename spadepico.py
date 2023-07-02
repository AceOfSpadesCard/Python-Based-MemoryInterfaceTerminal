# Importing all the modules
import os

# Initializing variables
directory = "Files"
exit_code = False
color_end = '\033[39m'

# Initializing Data Structures
data_dict = {}
data_list = []


# Forever loop for terminal inputs unless exit command entered
while not exit_code:
    # Initializing the variables that need to reset with each iteration
    file_name = ""
    file_path = ""
    dict_exit = False
    write_command_flag = False
    terminal = input(f"{directory} $ ")

    # Creating an external .txt. storage file
    if "cre@te " in terminal:
        file_name = str(terminal[7:]) + ".txt"
        file_path = os.path.join('Files', file_name)
        # Checking if the directory exists, if not then create it
        if not os.path.exists('Files'):
            os.makedirs('Files')
        file_handle = open(file_path, "a")
        create_command = input("~content $ ")
        file_handle.write(create_command)
        file_handle.close()

    # Writing to an external .txt. storage file
    elif "wr!te " in terminal:
        file_name = str(terminal[6:]) + ".txt"
        file_path = os.path.join('Files', file_name)
        # Checking if the directory exists, if not then create it
        if not os.path.exists('Files'):
            os.makedirs('Files')
        file_handle = open(file_path, "a")
        create_command = input("~content $ ")
        file_handle.write(create_command)
        file_handle.write("\n")
        file_handle.close()
        write_command_flag = True

    # Writing to a local dictionary
    elif "wr!te-local-dict" in terminal:
        while dict_exit == False:
            key_command = input("~key $ ")
            if key_command == "exit-dict":
                dict_exit = True
            value_command = input("~value $ ")
            if value_command == "exit-dict":
                dict_exit = True
            if dict_exit == False:
                data_list.append(value_command)
        write_command_flag = True

    # Writing to a local list
    elif "wr!te-local-list" in terminal:
        while dict_exit == False:
            value_command = input("~value $ ")
            if value_command == "exit-list":
                dict_exit = True
            if dict_exit == False:
                data_list.append(value_command)
        write_command_flag = True

    # Reading from a local dictionary
    elif "re@d-local-dict" in terminal:
        print(str(data_dict))

    # Reading from a local list
    elif "re@d-local-list" in terminal:
        print(str(data_list))

    # Reading from an external .txt. storage file
    elif "re@d " in terminal:
        try:
            file_name = str(terminal[4:]) + ".txt"
            file_path = os.path.join('Files' + file_name)
            file_name = file_name.strip()
            file_handle = open("Files/" + file_name, "r")
            total = file_handle.read()
            print(str(total))
            file_handle.close()
        except:
            print("[error{1} file does not exist]")

    # Exit command for the terminal
    elif terminal == "exit":
        exit_code = True

    # Write Command flag to pass the error
    elif write_command_flag:
        write_command_flag = False
        pass

    # Error 2 Command does not exist
    else:
        print("[error{2} command does not exist]")
