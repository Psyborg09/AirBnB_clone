# 0x00. AirBnB clone - The console


## Description of the project

Team project to build a clone of [AirBnB](https://www.airbnb.com/).

The console is a command interpreter 
The console will perform the following tasks using the command interpreter:

* create a new object
* retrive an object from a file
* do operations on objects
* destroy an object

## Storage

All the classes are handled by the "Storage" engine in the "FileStorage" Class.

All the development and testing was runned over an operating system Ubuntu 20.04 LTS using programming language Python 3.8.3. The editors used were VIM 8.1.2269, VSCode 1.6.1 and Atom 1.58.0 . Control version using Git 2.25.1.


change to the `AirBnb` directory and run the command:

```bash
 ./console.py
```

## Execution

In interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

in Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

##  Testing

All the test are defined in the `tests` folder.

### Documentation

* Modules:

```python
python3 -c 'print(__import__("my_module").__doc__)'
```

* Classes:

```python
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```

* Functions (inside and outside a class):

```python
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```

and

```python
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

### run test in interactive mode

```bash
echo "python3 -m unittest discover tests" | bash
```

### run test in non-interactive mode

To run the tests in non-interactive mode, and discover all the test, you can use the command:

```bash
python3 -m unittest discover tests
```


## Usage

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```

### Commands

> The commands are displayed in the following format *Command / usage / example with output*

* Create

> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*

```bash
create <class>

```

```bash
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb)
```

* Show

```bash
show <class> <id>
```

```bash
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb)
```

* Destroy

> *Deletes an instance of a given class with a given ID.*
> *Update the file.json*



* all

> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*


* update

> *Updates an instance based on the class name, id, and kwargs passed.*
> *Update the file.json*

## Authors
<details>
    <summary>kelvin chibuzo</summary>
    <ul>
    <li><a href="https://github.com/1Generic1">Github</a></li>
    </ul>
</details>
<details>
    <summary>Mawuli Agropah</summary>
</details>
