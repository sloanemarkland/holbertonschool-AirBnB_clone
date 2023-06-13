#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '
    class_list = ["Review", "Place", "State",
                  "User", "BaseModel", "City", "Amenity"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
            saves to JSON file and prints id"""
        if not arg:
            print('** class name missing **')
            return

        class_name = arg.split()[0]
        try:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print('** class doesn\'t exist **')

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        class_name = args[0]
        instance_id = args[1]
        if class_name not in HBNBCommand.class_list:
            print('** class doesn\'t exist **')
            return
        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in objects:
            print('** no instance found **')
            return
        obj = objects[key]
        print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        class_name = args[0]
        instance_id = args[1]
        if class_name not in HBNBCommand.class_list:
            print('** class doesn\'t exist **')
            return
        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in objects:
            print('** no instance found **')
            return
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Prints the string representation of all instances"""
        args = arg.split()
        if not args:
            objects = storage.all().values()
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.class_list:
                print('** class doesn\'t exist **')
                return
            objects = []
            for key, obj in (storage.all().items()):
                if key.split('.')[0] == class_name:
                    objects.append(obj)

        print([str(jbo) for jbo in objects])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        class_name = args[0]
        if class_name not in HBNBCommand.class_list:
            print('** class doesn\'t exist **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all().get(key)
        if not objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print('** attribute name missing **')
            return
        attribute_name = args[2]
        if len(args) < 4:
            print('** value missing **')
            return
        attribute_value = args[3]
        setattr(objects, attribute_name, attribute_value)
        objects.save()
