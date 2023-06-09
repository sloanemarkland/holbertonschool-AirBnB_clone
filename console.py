#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '

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
        """Creates a new instance of BaseModel, saves to JSON file and prints id"""
        if not arg:
            print('** class name missing **')
        elif arg != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            objects = BaseModel.load_json()
            key = args[0] + '.' + args[1]
            if key in objects:
                print(objects[key])
            else:
                print('** no instance found **')

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            objects = BaseModel.load_json()
            key = args[0] + '.' + args[1]
            if key in objects:
                del objects[key]
                BaseModel.save_json(objects)
            else:
                print('** no instance found **')

    def do_all(self, arg):
        """Prints the string representation of all instances"""
        args = arg.split()
        if not args:
            print(BaseModel.__str__())
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            print(BaseModel.__str__())

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        elif len(args) < 3:
            print('** attribute name missing **')
        elif len(args) < 4:
            print('** value missing **')
        else:
            objects = BaseModel.load_json()
            key = args[0] + '.' + args[1]
            if key not in objects:
                print('** no instance found **')
                return
            instance = objects[key]
            attribute_name = args[2]
            attribute_value = args[3]

            if attribute_name in instance:
                attribute_value = type(instance[attribute_name])(attribute_value)
            instance[attribute_name] = attribute_value
            BaseModel.save_json(objects)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
