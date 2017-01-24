# Python Virtual Environment Reference Manual

This short document presents virtualenv setup guide for OrangeADE project.

In short words **Virtualenv** is a dedicated and independent **container**
for **Python Application** along with its **Dependencies**.
Different Operating Systems may be bundled with different versions of
Python and different set of available packages by default.
This makes project **deployment** and **maintenance** difficult,
if possible at all.
This is why we want to create from scratch dedicated environment
that we can control.
**Virtualenv** is here to make it happen in an **automated** way.


## Using Virtualenv

OrangeADE project contains several scripts that will make it easier
for you develop, test, and deploy it using provided Virtualenv.
Assuming that you already did a successful setup of Virtualenv:

* `venv.sh` script will take you inside `bash` shell with target python
environment in path, so you can test some code.
* `venv-django-runserver.sh` script will launch a TEST Django
web server that will help you in a platform development and testing.
Note that the serves is ONLY intended for development purposes and NOT
as production deployment. If you have all dependencies met, you should
get server instance running at `http://localhost:8000`.


## Creating Virtualenv

* We are using the `Python 2.7.13` interpreter and so `virtualenv-2.7`.
* You can get Python [directly
from the Python Project Website]
(https://www.python.org/downloads/) or using your
Operating System Package Management.
* OrangeADE assumes virtualenv location at `../venv/default/` from the
project root (that is where `venv.sh` is located). This location is important!
* If you work with [PyCharm IDE](https://www.jetbrains.com/pycharm/) go to `Preferences / Project / Interpreter`
and use creator to make all work for you.
* You can create Virtualenv from a Terminal:
```
$ mkdir ../venv
$ virtualenv-2.7 ../venv/macos-venv-2.7
$ ln -s macos-venv-2.7 ../venv/default
```
* You can have multiple instances of virtualenv in `../venv` directory,
for instance when you develop on [MacOS](https://en.wikipedia.org/wiki/MacOS)
and deploy on [FreeBSD](https://en.wikipedia.org/wiki/FreeBSD),
just remember to link the one you need as `default`.
* Virtualenv requires `bash` to run.
* You can test your setup with:
```
$ pwd
/(...)/OrangeADE/OrangeADE.git
$ ./venv.sh
(macos-venv-2.7) pwd
/(...)/OrangeADE/OrangeADE.git
(macos-venv-2.7) which python
/(...)/OrangeADE/venv/macos-venv-2.7/bin/python
(macos-venv-2.7) python
Python 2.7.13 (default, Dec 18 2016, 05:36:03) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

## Installing dependencies

After you have installed the virtualenv you need to install project
dependencies, that is libraries and modules that the project depends on.
Here is an example:

```
$ ./venv.sh
(macos-venv-2.7) pip install django
...
```

<hr/>
<sup>(C) 2017 [CeDeROM Tomasz CEDRO](http://www.tomek.cedro.info), All rights reserved! :-)</sup>
