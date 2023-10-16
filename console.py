#!/usr/bin/python3
import cmd
"""This module defines the class `HBHBCommand`"""


class HBNBCommand(cmd.Cmd):
    """Defines the entry point of the command interpreter"""
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
