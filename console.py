#!/usr/bin/python3
"""
this is the console module
"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl-D)
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id
        """
        if not arg:
            print("** class name is missing **")
            return
        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Print the string representation of an instance
        """
        args = arg.split()
        if not arg or args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instances = storage.all()
        key = "BaseModel." + instance_id
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            if len(args) < 2:
                print("** instance id missing **")
                return
            class_name = args[0]
            instance_id = args[1]
            instances = storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")
        except Exception as e:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Print all string representations of instances
        """
        args = arg.split()
        if not arg or args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        instances = storage.all()
        instance_list = [str(instances[k]) for k in instances if k.startswith("BaseModel.")]
        print(instance_list)

    def do_update(self, arg):
        """
        Update an instance's attributes
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            if len(args) < 2:
                print("** instance id missing **")
                return
            class_name = args[0]
            instance_id = args[1]
            instances = storage.all()
            key = "{}.{}".format(class_name, instance_id)
            if key not in instances:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_name = args[2]
            attribute_value = args[3]
            if attribute_name not in ["id", "created_at", "updated_at"]:
                instance = instances[key]
                setattr(instance, attribute_name, attribute_value)
                instance.save()
        except Exception as e:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
