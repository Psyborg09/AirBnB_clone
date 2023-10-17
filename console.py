#!/usr/bin/python3
"""This module defines the class `HBHBCommand`"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the entry point of the command interpreter"""
    prompt = "(hbnb) "
    __classes = ["BaseModel"]


    def do_quit(self, arg):
        """a quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """shows End of file
        """
        return True

    def emptyline(self):
        """Defines what happens when the `Enter` key is pressed
        """
        return

    def do_create(self, arg):
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{args[0]}")()
            print(new_instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
