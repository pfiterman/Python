# Python

## Introduction
Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the [Python Web site](https://www.python.org/), and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.

The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.

This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial can be read off-line as well.

For a description of standard objects and modules, see The Python Standard Library. The Python Language Reference gives a more formal definition of the language. To write extensions in C or C++, read Extending and Embedding the Python Interpreter and Python/C API Reference Manual. There are also several books covering Python in depth.

This tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used feature. Instead, it introduces many of Python’s most noteworthy features, and will give you a good idea of the language’s flavor and style. After reading it, you will be able to read and write Python modules and programs, and you will be ready to learn more about the various Python library modules described in The Python Standard Library.

## Why use Phyton?
If you do much work on computers, eventually you find that there’s some task you’d like to automate. For example, you may wish to perform a search-and-replace over a large number of text files, or rename and rearrange a bunch of photo files in a complicated way. Perhaps you’d like to write a small custom database, or a specialized GUI application, or a simple game.

If you’re a professional software developer, you may have to work with several C/C++/Java libraries but find the usual write/compile/test/re-compile cycle is too slow. Perhaps you’re writing a test suite for such a library and find writing the testing code a tedious task. Or maybe you’ve written a program that could use an extension language, and you don’t want to design and implement a whole new language for your application.

Python is just the language for you.

You could write a Unix shell script or Windows batch files for some of these tasks, but shell scripts are best at moving around files and changing text data, not well-suited for GUI applications or games. You could write a C/C++/Java program, but it can take a lot of development time to get even a first-draft program. Python is simpler to use, available on Windows, Mac OS X, and Unix operating systems, and will help you get the job done more quickly.

Python is simple to use, but it is a real programming language, offering much more structure and support for large programs than shell scripts or batch files can offer. On the other hand, Python also offers much more error checking than C, and, being a very-high-level language, it has high-level data types built in, such as flexible arrays and dictionaries. Because of its more general data types Python is applicable to a much larger problem domain than Awk or even Perl, yet many things are at least as easy in Python as in those languages.

Python allows you to split your program into modules that can be reused in other Python programs. It comes with a large collection of standard modules that you can use as the basis of your programs — or as examples to start learning to program in Python. Some of these modules provide things like file I/O, system calls, sockets, and even interfaces to graphical user interface toolkits like Tk.

Python is an interpreted language, which can save you considerable time during program development because no compilation and linking is necessary. The interpreter can be used interactively, which makes it easy to experiment with features of the language, to write throw-away programs, or to test functions during bottom-up program development. It is also a handy desk calculator.

Python enables programs to be written compactly and readably. Programs written in Python are typically much shorter than equivalent C, C++, or Java programs, for several reasons:

- The high-level data types allow you to express complex operations in a single statement;
- Statement grouping is done by indentation instead of beginning and ending brackets;
- No variable or argument declarations are necessary.

Python is extensible: if you know how to program in C it is easy to add a new built-in function or module to the interpreter, either to perform critical operations at maximum speed, or to link Python programs to libraries that may only be available in binary form (such as a vendor-specific graphics library). Once you are really hooked, you can link the Python interpreter into an application written in C and use it as an extension or command language for that application.

By the way, the language is named after the BBC show “Monty Python’s Flying Circus” and has nothing to do with reptiles. Making references to Monty Python skits in documentation is not only allowed, it is encouraged!

Now that you are all excited about Python, you’ll want to examine it in some more detail. Since the best way to learn a language is to use it, the tutorial invites you to play with the Python interpreter as you read.

In the next chapter, the mechanics of using the interpreter are explained. This is rather mundane information, but essential for trying out the examples shown later.

The rest of the tutorial introduces various features of the Python language and system through examples, beginning with simple expressions, statements and data types, through functions and modules, and finally touching upon advanced concepts like exceptions and user-defined classes.

### Using Python on Windows
This document aims to give an overview of Windows-specific behaviour you should know about when using Python on Microsoft Windows.

Unlike most Unix systems and services, Windows does not include a system supported installation of Python. To make Python available, the CPython team has compiled Windows installers (MSI packages) with every release for many years. These installers are primarily intended to add a per-user installation of Python, with the core interpreter and library being used by a single user. The installer is also able to install for all users of a single machine, and a separate ZIP file is available for application-local distributions.

As specified in PEP 11, a Python release only supports a Windows platform while Microsoft considers the platform under extended support. This means that Python 3.9 supports Windows Vista and newer. If you require Windows XP support then please install Python 3.4.

There are a number of different installers available for Windows, each with certain benefits and downsides.

The full installer contains all components and is the best option for developers using Python for any kind of project.

The Microsoft Store package is a simple installation of Python that is suitable for running scripts and packages, and using IDLE or other development environments. It requires Windows 10, but can be safely installed without corrupting other programs. It also provides many convenient commands for launching Python and its tools.

The nuget.org packages are lightweight installations intended for continuous integration systems. It can be used to build Python packages or run scripts, but is not updateable and has no user interface tools.

The embeddable package is a minimal package of Python suitable for embedding into a larger application.

### Using Python on Windows
- [Installation Steps](#installation-steps)
- [Removing the MAX_PATH Limitation](#removing-the-max_path-limitation)
- [The Microsoft Store Package](#the-microsoft-store-package)
- [Alternative bundles](#alternative-bundles)
- [Configuring Python](#configuring-python)
- [Excursus: Setting environment variables](#excursus--setting-environment-python)
- [Finding the Python executable](#finding-the-python-executable)
- [UTF-8 mode](#utf-8-mode)

### Getting started
- [Invoking the Python Interpreter](#invoking-the-python-interpreter)
- [Argument Passing](#argument-passing)
- [Interactive Mode](#interactive-mode)

### An Informal Introduction to Python
- [Comments](#comments)
- [Variables](#variables)
- [Numbers](#numbers)
- [Strings](#strings)
- [Lists](#lists)

### Fist Steps Towards Programming
- [Fibonacci Series](#fibonacci-series)

### More Control Flow Tools
- [If Statements](#if-statements)
- [For Statements](#for-statements)
- [The range function](#the-range-function)

#### Installation Steps
Four Python 3.9 installers are available for download - two each for the 32-bit and 64-bit versions of the interpreter. The web installer is a small initial download, and it will automatically download the required components as necessary. The offline installer includes the components necessary for a default installation and only requires an internet connection for optional features. See Installing Without Downloading for other ways to avoid downloading during installation.

After starting the installer, one of two options may be selected. If you select “Install Now”:

- You will not need to be an administrator (unless a system update for the C Runtime Library is required or you install the Python Launcher for Windows for all users)
- Python will be installed into your user directory
- The Python Launcher for Windows will be installed according to the option at the bottom of the first page
- The standard library, test suite, launcher and pip will be installed
- If selected, the install directory will be added to your PATH
- Shortcuts will only be visible for the current user

Selecting “Customize installation” will allow you to select the features to install, the installation location and other options or post-install actions. To install debugging symbols or binaries, you will need to use this option.

To perform an all-users installation, you should select “Customize installation”. In this case:

- You may be required to provide administrative credentials or approval
- Python will be installed into the Program Files directory
- The Python Launcher for Windows will be installed into the Windows directory
- Optional features may be selected during installation
- The standard library can be pre-compiled to bytecode
- If selected, the install directory will be added to the system PATH
- Shortcuts are available for all users

#### Removing the MAX_PATH Limitation
Windows historically has limited path lengths to 260 characters. This meant that paths longer than this would not resolve and errors would result. In the latest versions of Windows, this limitation can be expanded to approximately 32,000 characters. Your administrator will need to activate the “Enable Win32 long paths” group policy, or set LongPathsEnabled to 1 in the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem.

This allows the open() function, the os module and most other path functionality to accept and return paths longer than 260 characters. After changing the above option, no further configuration is required.

Changed in version 3.6: Support for long paths was enabled in Python.

#### The Microsoft Store Package
The Microsoft Store package is an easily installable Python interpreter that is intended mainly for interactive use, for example, by students.

To install the package, ensure you have the latest Windows 10 updates and search the Microsoft Store app for “Python 3.9”. Ensure that the app you select is published by the Python Software Foundation, and install it.

After installation, Python may be launched by finding it in Start. Alternatively, it will be available from any Command Prompt or PowerShell session by typing python. Further, pip and IDLE may be used by typing pip or idle. IDLE can also be found in Start.

All three commands are also available with version number suffixes, for example, as python3.exe and python3.x.exe as well as python.exe (where 3.x is the specific version you want to launch, such as 3.9). Open “Manage App Execution Aliases” through Start to select which version of Python is associated with each command. It is recommended to make sure that pip and idle are consistent with whichever version of python is selected.

Virtual environments can be created with python -m venv and activated and used as normal.

If you have installed another version of Python and added it to your PATH variable, it will be available as python.exe rather than the one from the Microsoft Store. To access the new installation, use python3.exe or python3.x.exe.

The py.exe launcher will detect this Python installation, but will prefer installations from the traditional installer.

To remove Python, open Settings and use Apps and Features, or else find Python in Start and right-click to select Uninstall. Uninstalling will remove all packages you installed directly into this Python installation, but will not remove any virtual environments

- [Known Issues]
Because of restrictions on Microsoft Store apps, Python scripts may not have full write access to shared locations such as TEMP and the registry. Instead, it will write to a private copy. If your scripts must modify the shared locations, you will need to install the full installer.

#### Alternative Bundles
Besides the standard CPython distribution, there are modified packages including additional functionality. The following is a list of popular versions and their key features:

- [ActivePython](https://www.activestate.com/activepython/) : Installer with multi-platform compatibility, documentation, PyWin32
- [Anaconda](https://www.anaconda.com/download/) : Popular scientific modules (such as numpy, scipy and pandas) and the conda package manager.
- [Canopy](https://www.enthought.com/product/canopy/) : A “comprehensive Python analysis environment” with editors and other development tools.
- [WinPython](https://winpython.github.io/) : Windows-specific distribution with prebuilt scientific packages and tools for building packages.

Note that these packages may not include the latest versions of Python or other libraries, and are not maintained or supported by the core Python team.

#### Configuring Python
To run Python conveniently from a command prompt, you might consider changing some default environment variables in Windows. While the installer provides an option to configure the PATH and PATHEXT variables for you, this is only reliable for a single, system-wide installation. If you regularly use multiple versions of Python, consider using the [Python Launcher for Windows](https://docs.python.org/3/using/windows.html#launcher).

#### Excursus: Setting environment variables
Windows allows environment variables to be configured permanently at both the User level and the System level, or temporarily in a command prompt. To temporarily set environment variables, open Command Prompt and use the set command:

```Python
C:\>set PATH=C:\Program Files\Python 3.9;%PATH%
C:\>set PYTHONPATH=%PYTHONPATH%;C:\My_python_lib
C:\>python
```

These changes will apply to any further commands executed in that console, and will be inherited by any applications started from the console.

Including the variable name within percent signs will expand to the existing value, allowing you to add your new value at either the start or the end. Modifying PATH by adding the directory containing python.exe to the start is a common way to ensure the correct version of Python is launched.

To permanently modify the default environment variables, click Start and search for ‘edit environment variables’, or open System properties, Advanced system settings and click the Environment Variables button. In this dialog, you can add or modify User and System variables. To change System variables, you need non-restricted access to your machine (i.e. Administrator rights).

```Note
Note Windows will concatenate User variables after System variables, which may cause unexpected results when modifying PATH.
The PYTHONPATH variable is used by all versions of Python 2 and Python 3, so you should not permanently configure this variable unless it only includes code that is compatible with all of your installed Python versions.
```

#### Finding the Python executable
Besides using the automatically created start menu entry for the Python interpreter, you might want to start Python in the command prompt. The installer has an option to set that up for you.

On the first page of the installer, an option labelled “Add Python to PATH” may be selected to have the installer add the install location into the PATH. The location of the Scripts\ folder is also added. This allows you to type python to run the interpreter, and pip for the package installer. Thus, you can also execute your scripts with command line options, see [Command line](https://docs.python.org/3/using/cmdline.html#using-on-cmdline) documentation.

If you don’t enable this option at install time, you can always re-run the installer, select Modify, and enable it. Alternatively, you can manually modify the PATH using the directions in [Excursus: Setting environment variables](#excursus--setting-environment-variables). You need to set your PATH environment variable to include the directory of your Python installation, delimited by a semicolon from other entries. An example variable could look like this (assuming the first two entries already existed):

```Python
C:\WINDOWS\system32;C:\WINDOWS;C:\Program Files\Python 3.9
```

#### UTF-8 Mode
Windows still uses legacy encodings for the system encoding (the ANSI Code Page). Python uses it for the default encoding of text files (e.g. locale.getpreferredencoding(). This may cause issues because UTF-8 is widely used on the internet and most Unix systems, including WSL (Windows Subsystem for Linux).

You can use UTF-8 mode to change the default text encoding to UTF-8. You can enable UTF-8 mode via the `-X utf8` command line option, or the `PYTHONUTF8=1` environment variable. See [PYTHONUTF8](#pythonutf8) for enabling UTF-8 mode, and [Excursus: Setting environment variables](#excursus--setting-environment-variables) for how to modify environment variables.

When UTF-8 mode is enabled:

- locale.getpreferredencoding() returns 'UTF-8' instead of the system encoding. This function is used for the default text encoding in many places, including open(), Popen, Path.read_text(), etc.
- sys.stdin, sys.stdout, and sys.stderr all use UTF-8 as their text encoding.

You can still use the system encoding via the “mbcs” codec.

Note that adding `PYTHONUTF8=1` to the default environment variables will affect all Python 3.7+ applications on your system. If you have any Python 3.7+ applications which rely on the legacy system encoding, it is recommended to set the environment variable temporarily or use the `-X utf8` command line option.

```Note
Note Even when UTF-8 mode is disabled, Python uses UTF-8 by default on Windows for: Console I/O including standard I/O and The filesystem encoding.
```

### Getting Started
#### Using the Python Interpreter
##### Invoking the Python Interpreter
The Python interpreter is usually installed as `/usr/local/bin/python3.9` on those machines where it is available; putting `/usr/local/bin` in your Unix shell’s search path makes it possible to start it by typing the command:

```Python
python3.9
```

On Windows machines where you have installed Python from the Microsoft Store, the python3.9 command will be available. If you have the `py.exe` launcher installed, you can use the `py command`. See [Excursus: Setting environment variables](#excursus--setting-environment-variables) for other ways to launch Python.

```Python
D:\Developer\Python\projects\learning\documentation>py
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Typing an end-of-file character (Control-D on Unix, `Control-Z on Windows`) at the primary prompt causes the interpreter to exit with a zero exit status. If that doesn’t work, you can exit the interpreter by typing the following command: `quit()`.

```Python
D:\Developer\Python\projects\learning\documentation>py
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()

D:\Developer\Python\projects\learning\documentation>
```

The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a script from that file.

A second way of starting the interpreter is python -c command [arg] ..., which executes the statement(s) in command, analogous to the shell’s -c option. Since Python statements often contain spaces or other characters that are special to the shell, it is usually advised to quote command in its entirety with single quotes.

Some Python modules are also useful as scripts. These can be invoked using python -m module [arg] ..., which executes the source file for module as if you had spelled out its full name on the command line.

When a script file is used, it is sometimes useful to be able to run the script and enter interactive mode afterwards. This can be done by passing -i before the script.

All command line options are described in [Command line and environment](https://docs.python.org/3/using/cmdline.html#using-on-general).


##### Argument Passing
When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and assigned to the `argv` variable in the `sys` module. You can access this list by executing `import sys`. The length of the list is at least one; when no script and no arguments are given, `sys.argv[0]` is an empty string. When the script name is given as `-` (meaning standard input), `sys.argv[0]` is set to `-`. When -c command is used, `sys.argv[0]` is set to `-c`. When `-m` module is used, `sys.argv[0]` is set to the full name of the located module. Options found after `-c` command or `-m` module are not consumed by the Python interpreter’s option processing but left in `sys.argv` for the command or module to handle.

Let’s create a test Python script - create a file called hello.py with the following contents

```Python
#! python
import sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))
```

You should notice the version number of your latest Python installation is printed.

##### Interactive Mode
When commands are read from a tty, the interpreter is said to be in interactive mode. In this mode it prompts for the next command with the primary prompt, usually three greater-than signs `(>>>)`; for continuation lines it prompts with the secondary prompt, by default three dots `(...)`. The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt:

```Python
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Continuation lines are needed when entering a multi-line construct. As an example, take a look at this if statement:

```Python
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
>>>
```

### An Informal Introduction to Python
#### Comments
In the following examples, input and output are distinguished by the presence or absence of prompts (`>>>` and `…`): to repeat the example, you must type everything after the prompt, when the prompt appears; lines that do not begin with a prompt are output from the interpreter. Note that a secondary prompt on a line by itself in an example means you must type a blank line; this is used to end a multi-line command.

Many of the examples in this manual, even those entered at the interactive prompt, include comments. Comments in Python start with the hash character, `#`, and extend to the end of the physical line. A comment may appear at the start of a line or following whitespace or code, but not within a string literal. A hash character within a string literal is just a hash character. Since comments are to clarify code and are not interpreted by Python, they may be omitted when typing in examples.

Some examples:

```Python
# comments.py
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
print(text)
```

#### Variables
Python supports variables and in order to assign a new value to a variable, the syntax looks a little something like this:

```Python
# variables.py
a = 28        #int
b = 1.5       #float
c = "Hello!"  #str
d = True      #bool
e = None      #NoneType
```

If I have a line like a equals 28, what that's going to mean is take the value 28 and assign it, store it inside of this variable called `a`. Now, unlike other languages like C or Java which you might be familiar with, where you have to specify the type of every variable you create -- You have to say like, `int a` to mean a is an `integer`. Python doesn't require you to tell you what the types of each of these variables actually are. So we can just say a equals 28 and Python knows that because this number is an int, that it's going to represent the variable `a` as an `int`, that it knows, it's able to infer, what the types of any these values happen to be.

So all the values do indeed have types. You just don't explicitly need to state them. So, for example, in the variable.py file above, the number 28 is a type int, it's an integer. A number like 1.5 has a decimal in it, it's a floating point number. So that, in Python, is what we might call a float type. Any type of text, something like the word "hello" wrapped in either double quotation marks or single quotation marks -- Python supports both -- is what we would call the str type, short for string. We also have a type for Boolean values, things that can be either true or false. In Python, those are represented using a capital T, true, and a capital F, false. Those are of the type bool. And also, we have a special type in Python called the none type, which only has one possible value, this capital N, none. And none as a value we'll use whenever we want to represent the lack of a value somewhere. So if we have a function that is not returning anything, it is really returning none, effectively.

#### Numbers
The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / work just like in most other languages (for example, Pascal or C); parentheses (()) can be used for grouping. For example:

```Python
# numbers.py
addition = (2 + 2)
multiplication = (5 * 6)
subtraction = (50 - multiplication)
division = (subtraction / 4)
division2 = (8 / 5)             # division always returns a floating point number
division3 = (17 // 3)           # floor division discards the fractional part
remainder = (17 % 3)            # the % operator returns the remainder of the division
squared = (5 ** 2)              # 5 squared
powerof = (2 ** 7)              # 2 to the power of 7
floatpoint = (4 * 3.75 - 1)     # Operators with mixed type operands convert the integer operand to floating point

print(f"Addition of (2 + 2)={addition}")
print(f"Multiplication of (5 * 6)={multiplication}")
print(f"Subtraction of (50 - 5 * 6)={subtraction}")
print(f"Division always returns a floating point number: (8 / 5)={division2}")
print(f"Floor division discards the fractional part: (17 // 3)={division3}")
print(f"The operator % returns the remainder of the division: (17 % 3)={remainder}")
print(f"It is possible to use the ** operator to calculate powers: 5 squared(5 ** 2) ={squared}")
print(f"To calculate 2 to the power of 7: (2 ** 7)={powerof}")
print(f"Operators with mixed type operands convert the integer operand to floating point: (4 * 3.75 - 1)={floatpoint}")
```

The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float. Division (`/`) always returns a float. To do floor division and get an integer result (discarding any fractional result) you can use the (`//`) operator; to calculate the remainder you can use `%`. It is possible to use the `**` operator to calculate powers. There is also full support for floating point; operators with mixed type operands convert the integer operand to floating point.

In interactive mode, the last printed expression is assigned to the variable `_`. This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, for example:

```Python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

This variable should be treated as read-only by the user. Don’t explicitly assign a value to it — you would create an independent local variable with the same name masking the built-in variable with its magic behavior.

In addition to int and float, Python supports other types of numbers, such as Decimal and Fraction. Python also has built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).

#### Strings
Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 2. \ can be used to escape quotes:

```Python
# strings.py
string = 'spam eggs'    # strings can be enclosed in single quotes
string1 = 'doesn\'t'    # use \' to escape the single quote...
string2 = "doesn't"     # ...or use double quotes instead

print(f"Strings can be enclosed in sigle quotes \'\'")
print(f"Use \\ to escape the single quote \'")
print(f"You can use double quotes instead \"doesn't\"")
print(f"\"Yes,\" they said.'")
print(f"\"Yes,\" they said.")
print(f"Isn\'t, they said.")
```

In the interactive interpreter, the output string is enclosed in quotes and special characters are escaped with backslashes. While this might sometimes look different from the input (the enclosing quotes could change), the two strings are equivalent. The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes. The print() function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters:

```Python
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line. \nSecond line.'  # \n means newline
>>> s #without print(), \n is included in the output
'First line. \nSecond line.'
>>> print(s) # with print(), \n produces a new line
First line.
Second line.
```

If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

```Python
>>> print('C:\some\name') # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name') #note the r before the quote
C:\some\name
>>>
```

String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:

```Python
>>> print("""\
... Usage: thingy [OPTIONS]
...     -h                      Display this usage message
...     -H hostname             Hostname to connect to
... """)
Usage: thingy [OPTIONS]
        -h                      Display this usage message
        -H hostname             Hostname to connect to
>>>        
```

Strings can be concatenated (glued together) with the + operator, and repeated with *

```Python
# strings.py
string3 = 3 * 'un' + 'ium'      # 3 times 'un', followed by 'ium'
print(string3)                  # 'unununium'
```

Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

```Python
# strings.py
string4 = 'Py' 'thon'           # Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print(string4)                  # Python
```

This feature is particularly useful, in the interactive interpreter, when you want to break long strings:

```Python
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
>>>
```

This only works with two literals though, not with variables or expressions:

```Python
>>> prefix = 'Py'
>>> prefix 'thon' # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon' # can't concatenate a variable and a string literal
           ^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^
SyntaxError: invalid syntax
>>>
```

If you want to concatenate variables or a variable and a literal, use +:

```Python
>>> prefix + 'thon'
'Python'
```

Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:

```Python
>>> word = 'Python'
>>> word[0] # character in position 0
'P'
>>> word[5] # character in position 5
'n'
>>>
```

Indices may also be negative numbers, to start counting from the right:

```Python
>>> word[-1] # Last character
'n'
>>> word[-2] # second-Last character
'o'
>>> word[-6]
'P'
>>>
```

Note that since -0 is the same as 0, negative indices start from -1. In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:

```Python
>>> word[0:2] # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5] # characters from position 2 (included) to 5 (excluded)
'tho'
>>>
```

Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:

```Python
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
>>>
```

Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

```Python
>>> word[:2] # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:] # characters from position 4 (included) to the end
'on'
>>> word[-2:] # characters from the second-Last (included) to the end
'on'
>>>
```

One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:

```Python
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices. The slice from i to j consists of all characters between the edges labeled i and j, respectively.

For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.

Attempting to use an index that is too large will result in an error:

```Python
>>> word[42] # the word onle has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>>
```

However, out of range slice indexes are handled gracefully when used for slicing:

```Python
>>> word[4:42]
'on'
>>> word[42:]
''
>>>
```

Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:

```Python
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

If you need a different string, you should create a new one:

```Python
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
>>>
```

The built-in function len() returns the length of a string:

```Python
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```

#### Lists
Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.

```Python
# lists.py
# Lists can be written as a list of comma-separated values (items) between square brackets
squares = [1, 4, 9, 16, 25]
print(f"squares={squares}")
```

Like strings (and all other built-in sequence types), lists can be indexed and sliced:

```Python
# lists.py
# Lists can be indexed and slices like strings
print(f"squares[0]={squares[0]}")
print(f"squares[-1]={squares[-1]}")
print(f"squares[-3:]={squares[-3:]}")
```

All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:

```Python
# lists.py
# All slice operations return a new list containing the requested elements
print(f"squares[:]={squares[:]}")
```

Lists also support operations like concatenation:

```Python
# lists.py
# Lists also support operations like concatenation
squares2 = squares + [36, 49, 64, 81, 100]
print(f"squares2 = squares + [36, 49, 64, 81, 100] = {squares2}")
```

Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:

```Python
# lists.py
# Lists are a mutable type, i.e. it is possible to change their content
cubes = [1, 8, 27, 65, 125] #something wrong here, the cube of 4 (4 ** 3) is 64, not 65!
cubes[3] = 64
print(f"cubes = {cubes}")
```

You can also add new items at the end of the list, by using the append() method (we will see more about methods later):

```Python
# lists.py
# You can also add new items at the end of the list, by using the append() method
cubes.append(216) #add the cube of 6
cubes.append(7 ** 3) # and the cube of 7
print(f"cubes = {cubes}")
```

Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

```Python
# lists.py
# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"letters = {letters}")

letters[2:5] = ['C', 'D', 'E'] #replacing some values
print(f"letters = {letters}")

letters[2:5] = [] #removing values
print(f"letters = {letters}")

letters[:] = [] # clear the list by replacing all the elements with an empty list
print(f"letters = {letters}")
```

The built-in function len() also applies to lists:

```Python
# lists.py
# The built-in function len() also applies to lists
letters = ['a', 'b', 'c', 'd']
print(f"len(letters) = {len(letters)}")
```

It is possible to nest lists (create lists containing other lists), for example:

```Python
# lists.py
# It is possible to nest lists (create lists containing other lists)
a = ['a', 'b', 'c']
n = [1, 2 ,3]
x = [a, n]
print(f"x = {x}")
print(f"x[0] = {x[0]}")
print(f"x[0][1] = {x[0][1]}")
```

### Fist Steps Towards Programming
#### Fibonacci Series
Of course, we can use Python for more complicated tasks than adding two and two together. For instance, we can write an initial sub-sequence of the Fibonacci series as follows:

```Python
# fibonacci.py
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
```

This example introduces several new features.

- The first line contains a multiple assignment: the variables a and b simultaneously get the new values 0 and 1. On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before any of the assignments take place. The right-hand side expressions are evaluated from the left to the right.
- The while loop executes as long as the condition (here: a < 10) remains true. In Python, like in C, any non-zero integer value is true; zero is false. The condition may also be a string or list value, in fact any sequence; anything with a non-zero length is true, empty sequences are false. The test used in the example is a simple comparison. The standard comparison operators are written the same as in C: < (less than), > (greater than), == (equal to), <= (less than or equal to), >= (greater than or equal to) and != (not equal to).
- The body of the loop is indented: indentation is Python’s way of grouping statements. At the interactive prompt, you have to type a tab or space(s) for each indented line. In practice you will prepare more complicated input for Python with a text editor; all decent text editors have an auto-indent facility. When a compound statement is entered interactively, it must be followed by a blank line to indicate completion (since the parser cannot guess when you have typed the last line). Note that each line within a basic block must be indented by the same amount.
- The print() function writes the value of the argument(s) it is given. It differs from just writing the expression you want to write (as we did earlier in the calculator examples) in the way it handles multiple arguments, floating point quantities, and strings. Strings are printed without quotes, and a space is inserted between items, so you can format things nicely, like this:

```Python
# fibonacci.py
i = 256*256
print('The value of i is', i)
```

The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:

```Python
# fibonacci.py
a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, a+b
```

### More Control Flow Tools
Besides the `while` statement just introduced, Python uses the usual flow control statements known from other languages, with some twists.

#### If Statements
Perhaps the most well-known statement type is the `if` statement. For example:

```Python
# if.py
x = int(input("Please enter a integer: "))
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")
```

There can be zero or more `elif` parts, and the else part is optional. The keyword `elif` is short for `else if`, and is useful to avoid excessive indentation. An `if … elif … elif …` sequence is a substitute for the `switch` or `case statements` found in other languages.

#### For Statements
The `for` statement in Python differs a bit from what you may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. For example (no pun intended):

```Python
# for.py
# Measure some string:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:

```Python
# for.py
# Strategy: Iterate over a copy
for user, status in users.copy.items():
    if status == 'inactive':
        del users[user]

# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

#### The range Function
If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:

```Python
# range.py
for i in range(5):
    print(i)
```

The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’):

```Python
# range.py
print("range(5, 10)")
for i in range(5, 10):
    print(i)

print("range(0, 10, 3)")
for i in range(0, 10, 3):
    print(i)

print("range(-10, -100, -30)")
for i in range(-10, -100, -30):
    print(i)
```

To iterate over the indices of a sequence, you can combine range() and len() as follows:

```Python
# range.py
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
      print(i, a[i])
```

In most such cases, however, it is convenient to use the enumerate() function, see Looping Techniques.

A strange thing happens if you just print a range:

```Python
# range.py
print(range(10))
```

In many ways the object returned by `range()` behaves as if it is a list, but in fact it isn’t. It is an object which returns the successive items of the desired sequence when you iterate over it, but it doesn’t really make the list, thus saving space.

We say such an object is `iterable`, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. We have seen that the for statement is such a construct, while an example of a function that takes an `iterable` is sum():

```Python
# range.py
sum(range(4)) # 0 + 1 + 2 + 3
```

Later we will see more functions that return `iterables` and take `iterables` as arguments. Lastly, maybe you are curious about how to get a list from a range. Here is the solution:

```Python
# range.py
sum(range(4)) # 0 + 1 + 2 + 3
```
