import operations
import view
import os


def main() -> None:
    while True:
        operation = operations.get_operation()
        if operation == 1:
            view.add_contact()
        elif operation == 2:
            view.get_contact()
        elif operation == 3:
            view.set_contact()
        elif operation == 4:
            view.del_contact()
        else:
            print("До свидания")
            break


if __name__ == "__main__":
    if not "file.txt" in os.listdir():
        with open("file.txt", "w") as file:
            pass
    main()