from colorama import Fore, Style
import colorama
import os
import subprocess
import pickle
import os
import requests
import shutil

colorama.init()

os.system("clear")

history = []

print(Fore.GREEN + """
██████╗░██╗░░░██╗███╗░░░███╗███████╗██████╗░
██╔══██╗╚██╗░██╔╝████╗░████║██╔════╝██╔══██╗
██████╔╝░╚████╔╝░██╔████╔██║█████╗░░██████╔╝
██╔═══╝░░░╚██╔╝░░██║╚██╔╝██║██╔══╝░░██╔══██╗
██║░░░░░░░░██║░░░██║░╚═╝░██║███████╗██║░░██║
╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
""" + Style.RESET_ALL)

def copyes(x, b):
    shutil.copy(x, b)
    print(Fore.GREEN + " File " + x + " Successfully Copy In " + b + Style.RESET_ALL)

def copytree(x, b):
    shutil.copytree(x, b)
    print(Fore.GREEN + " Directory " + x + " Successfully Copy In " + b + Style.RESET_ALL)

def move(x, b):
    shutil.move(x, b)
    print(Fore.GREEN + " Object " + x + " Successfully Move In " + b + Style.RESET_ALL)


def mainlol():
    filename = 'user_stst.pkl'

    # Проверяем, существует ли файл
    if os.path.exists(filename):
        # Пытаемся загрузить ник из файла
        try:
            with open(filename, 'rb') as file:
                user_nick = pickle.load(file)
            print(f'Account Status: {user_nick}')
        except EOFError:
            user_nick = "Python Developer"
            with open(filename, 'wb') as file:
                pickle.dump(user_nick, file)
            print(f'Account Status: {user_nick}')
        except Exception as e:
            print(f'ERROR: {e}')
    else:
        # Запрашиваем ник у пользователя
        user_nick = "Python Developer"
        # Сохраняем ник в файл
        with open(filename, 'wb') as file:
            pickle.dump(user_nick, file)
        print(f'Account Status: {user_nick}')

def install_package(package_name):
    try:
        subprocess.run(['pip', 'install', package_name], check=True)
        print(f'Package {package_name} installed successfully.')
    except subprocess.CalledProcessError:
        print(f'Failed to install {package_name}.')
        
def list_installed_packages():
    try:
        output = subprocess.check_output(['pip', 'list']).decode('utf-8')
        print(output)
    except subprocess.CalledProcessError:
        print('Failed to list installed packages.')

storage = None

script_directory = os.path.dirname(os.path.abspath(__file__))




while True:
    com = input(Fore.RED + "~" + Style.RESET_ALL + Fore.GREEN + "$ - " + Style.RESET_ALL)

    if com.startswith("storage "):
        storage = com.split()[1]
        history.append("storage " + storage)
        print("Directory name = " + storage)

    elif com.lower() == "ls":
        history.append("ls")
        if storage is None:
            print(f"{script_directory}")
        else:
            print(storage)

    elif com.lower() == "catalog":
        history.append("catalog")
        print("garvard")
    elif com.lower() == "status":
        mainlol()
    elif com.lower() == "exit":
        print(Fore.RED + "Ending The Session" + Style.RESET_ALL)
        break
    elif com.lower() == "GET":
        url = input("url ")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print('Ответ от сервера:')
                print(response.json())  
            else:
                print(f'Ошибка {response.status_code}: {response.reason}')
        except requests.exceptions.RequestException as e:
            print(f'Произошла ошибка: {e}')
    elif com.startswith("dicopy"):
        parts = com.split()
        try:
            copytree(parts[1], parts[2])
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
    elif com.startswith("move"):
        parts = com.split()
        try:
            move(parts[1], parts[2])
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
    elif com.startswith("filecopy"):
        parts = com.split()
        try:
            copyes(parts[1], parts[2])
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)


    elif com.startswith("history"):
        part = com.split()
        if len(part) >= 2 and part[1].isdigit():
            count = int(part[1])  
            for item in history[:count]:
                print(item)
        else:
            for item in history:
                print(item)
    elif com.lower() == "clearn":
        os.system("clear")

    elif com.startswith("newFile"):
        parts = com.split()
        if len(parts) < 2:
            print(Fore.RED + "Error: File Name is not defined" + Style.RESET_ALL)
        else:
            file_name = parts[1]
            if not os.path.isfile(file_name) and len(file_name) >= 1:
                history.append("newFile " + file_name)
                with open(file_name, 'w') as file:
                    file.write('')  # Можно записать что-то по умолчанию или оставить пустым
                print(Fore.GREEN + "File " + file_name + " Successfully Created" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Error: File " + file_name + " already exists or has an incorrect name" + Style.RESET_ALL)

    elif com.startswith("newFolder"):
        parts = com.split()
        if len(parts) < 2:
            print(Fore.RED + "Error: Folder Name is not defined" + Style.RESET_ALL)
        else:
            direct = parts[1]
            if not os.path.isdir(direct) and len(direct) >= 1:
                history.append("newFolder " + direct)
                os.mkdir(direct)
                print(Fore.GREEN + "Folder " + direct + " Successfully Created" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Error: Folder " + direct + " already exists or has an incorrect name" + Style.RESET_ALL)

    elif com.startswith("python "):
        pytan = com.split()[1]
        
        if storage is None:
            try:
                with open(os.path.join(script_directory, pytan), 'r', encoding='utf-8') as file:
                    soder = file.read()
                    history.append("python " + pytan)
                    print(exec(soder))
            except FileNotFoundError:
                print(Fore.RED + "File not found." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Unknown Command" + Style.RESET_ALL)

    elif com.startswith("pip install "):
        package_name = com.split()[2]
        history.append("pip install " + package_name)
        install_package(package_name)

    elif com.lower() == "pip freeze":
        list_installed_packages()

    else:
        print(Fore.RED + "Command not recognized." + Style.RESET_ALL)
