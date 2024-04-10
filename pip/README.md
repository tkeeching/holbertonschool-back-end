## Task 0 - Using pip on your system
Be sure that your OS (even if using a docker image) is up to date and has the correct set of tools. We assume that you will use the same docker images for the following tasks. On Ubuntu, run:

1. Make sure that pip is installed on your system. If not, install it.

    - ```sudo apt-get update```
    - ```sudo apt-get upgrade```
    - ```sudo apt-get install python3-pip```

2. List the available packages with ```pip list```. What version of pip do you have?

### Solution

```
> pip list
```
```
Package    Version
---------- -------
pip        24.0
setuptools 65.5.0
```

```
> pip --version
```
```
pip 24.0 from /Users/keetee/.pyenv/versions/3.11.6/lib/python3.11/site-packages/pip (python 3.11)
```

## Task 1 - Playing with pip in a virtual environment
1. Create a virtual environment with the system interpreter
2. Activate the environment and list the available packages with pip
3. Install the package for dotenv
    - Go on PyPi and search for dotenv. The first result is probably not what you want. Look at the last udpate dates.
    - <b>warning</b> the name of the python’s module (‘dotenv’) does not always match the name of the PyPi package!
    - <b>warning</b> always go on PyPi and check what you are downloading!
    - Looking at the results, install ```python-dotenv```
4. List the available packages
5. Install flask and list available packages. See how flask’s dependencies have been pulled in.
6. Uninstall both dotenv and flask. List the packages. What happened ?!
7. Get the frozen list of package from pip. Compare it to the list of all available packages (you should have 2 less packages in it!)
    - Tip: use a shell redirection with ```>``` to create a file
8. Uninstall all the packages from the frozen list using the ```-r``` flag of pip
9. List the available packages. It should be the same as step 2.
10. Deactivate the environment

### Solution
1. Create a virtual environment with ```pyenv``` that uses python version 3.8.10
    ```
    > python3 -m venv task-1-env
    ```

2. Activate the environment and list the available packages with pip.
    ```
    > source task-1-env/bin/activate
    > pip list
    ```
    ```
    Package    Version
    ---------- -------
    pip        24.0
    setuptools 56.0.0
    ```

3. Install the package ```python-dotenv```
    ```
    > pip install python-dotenv
    ```

4. List all available packages.
    ```
    > pip list
    ```
    ```
    Package       Version
    ------------- -------
    pip           24.0
    python-dotenv 1.0.1
    setuptools    56.0.0
    ```

5. Install ```flask``` and list available packages. See how ```flask```'s dependencies have been pulled in.
    ```
    > pip install flask
    ```
    ```
    Package            Version
    ------------------ -------
    blinker            1.7.0
    click              8.1.7
    Flask              3.0.3
    importlib_metadata 7.1.0
    itsdangerous       2.1.2
    Jinja2             3.1.3
    MarkupSafe         2.1.5
    pip                24.0
    python-dotenv      1.0.1
    setuptools         56.0.0
    Werkzeug           3.0.2
    zipp               3.18.1
    ```

6. Uninstall both ```python-dotenv``` and ```flask```, list the packages. What happended?
    ```
    > pip uninstall python-dotenv flask
    > pip list
    ```
    ```
    Package            Version
    ------------------ -------
    blinker            1.7.0
    click              8.1.7
    importlib_metadata 7.1.0
    itsdangerous       2.1.2
    Jinja2             3.1.3
    MarkupSafe         2.1.5
    pip                24.0
    setuptools         56.0.0
    Werkzeug           3.0.2
    zipp               3.18.1
    ```
    > **NOTE**: Dependencies of ```flask``` are not removed!

7. Frozen list of package from pip.
    ```
    > pip freeze > requirements.txt
    > cat requirements.txt
    ```
    ```
    blinker==1.7.0
    click==8.1.7
    importlib_metadata==7.1.0
    itsdangerous==2.1.2
    Jinja2==3.1.3
    MarkupSafe==2.1.5
    Werkzeug==3.0.2
    zipp==3.18.1
    ```

8. Uninstall all the packages from the frozen list using the ```-r``` flag of pip
    > **NOTE**: ```-r``` stands for "requirement". When used with the ```pip uninstall``` command, it indicates taht pip should uninstall all packages specified in a requirements file.

9. List the available packages. It should be the same as step 2.
    ```
    > pip list
    ```
    ```
    Package    Version
    ---------- -------
    pip        24.0
    setuptools 56.0.0
    ```

10. Deactivate the environment.
    ```
    > deactivate
    ```


## Task 2 - Manipulating package versions
Keep checking your package list with pip!

1. Create a virtual environment and activate it.
2. Install the old 0.21.1 version of dotenv.
3. Upgrade dotenv.
4. Upgrage pip itself!
5. Install the last version of numpy 1.23.x using ```==``` and the character ```*```
    - Ensure you get the version 1.23.5
6. Upgrade numpy to any version after 1.24 , and before 1.26 using only ```>``` and ```<```.
    - You may need to use single quotes if your terminal complains while reading the command!
    - Ensure you get the version 1.25.2
7. Upgrade to the last version of numpy
8. Deactivate your environment

### Solution
1. Create a virtual environment and activate it.
    ```
    > python3 -m venv task-2-env
    > source task-2-env/bin/activate
    ```

2. Install the old 0.21.1 version of dotenv.
    ```
    > pip install python-dotenv==0.21.1
    ```
    ```
    Package       Version
    ------------- -------
    pip           24.0
    python-dotenv 0.21.1
    setuptools    56.0.0
    ```

3. Upgrade dotenv.
    ```
    > pip --upgrade python-dotenv
    ```
    ```
    Package       Version
    ------------- -------
    pip           24.0
    python-dotenv 1.0.1
    setuptools    56.0.0
    ```

4. Upgrage pip itself!
    > **NOTE**: Done in Step 1.

5. Install the last version of numpy 1.23.x using ```==``` and the character ```*```
    - Ensure you get the version 1.23.5
    ```
    > pip install numpy~=1.23
    > pip list
    ```
    ```
    Package       Version
    ------------- -------
    numpy         1.24.4
    pip           24.0
    python-dotenv 1.0.1
    setuptools    56.0.0
    ```

6. Upgrade numpy to any version after 1.24 , and before 1.26 using only ```>``` and ```<```.
    - You may need to use single quotes if your terminal complains while reading the command!
    - Ensure you get the version 1.25.2
    ```
    > pip install 'numpy>1.24, <1.26'
    > pip list
    ```
    ```
    Package    Version
    ---------- -------
    numpy      1.25.2
    pip        24.0
    setuptools 65.5.0
    ```

7. Upgrade to the last version of numpy
    ```
    > pip install --upgrade numpy
    > pip list
    ```
    ```
    Package    Version
    ---------- -------
    numpy      1.26.4
    pip        24.0
    setuptools 65.5.0
    ```

8. Deactivate your environment
    ```
    > deactivate
    ```

## Task 3 - Playing with requirements in several environments
Keep checking your package list with pip!

1. Create and activate a new fresh environment
    ```
    > python3 -m venv task-3-env
    > source task-3-env/bin/activate
    ```

2. Install ```requests 2.30.0``` and ```pandas 2.1.1```
    ```
    > pip install requests==2.23.0 pandas==2.1.1
    > pip list
    ```
    ```
    Package            Version
    ------------------ -----------
    certifi            2024.2.2
    charset-normalizer 3.3.2
    idna               3.6
    numpy              1.26.4
    pandas             2.1.1
    pip                24.0
    python-dateutil    2.9.0.post0
    pytz               2024.1
    requests           2.30.0
    setuptools         65.5.0
    six                1.16.0
    tzdata             2024.1
    urllib3            2.2.1
    ```

3. Create a ```requirements.txt``` file with ```pip``` freeze command
    ```
    > pip freeze > requirements.txt
    > cat requirements.txt
    ```
    ```
    certifi==2024.2.2
    charset-normalizer==3.3.2
    idna==3.6
    numpy==1.26.4
    pandas==2.1.1
    python-dateutil==2.9.0.post0
    pytz==2024.1
    requests==2.30.0
    six==1.16.0
    tzdata==2024.1
    urllib3==2.2.1
    ```

4. Create and activate another new fresh environment
5. Install the packages using the same ```requirements.txt``` file as step 2
6. Upgrade ```requests```.
    - Have a good look at the command line output and see how ```pip``` identifies already satisfied dependencies
        ```
        > pip install --upgrade requests
        ```
        ```
        Requirement already satisfied: requests in ./task-3b-env/lib/python3.11/site-packages (2.30.0)
        Collecting requests
        Downloading requests-2.31.0-py3-none-any.whl.metadata (4.6 kB)
        Requirement already satisfied: charset-normalizer<4,>=2 in ./task-3b-env/lib/python3.11/site-packages (from requests) (3.3.2)
        Requirement already satisfied: idna<4,>=2.5 in ./task-3b-env/lib/python3.11/site-packages (from requests) (3.6)
        Requirement already satisfied: urllib3<3,>=1.21.1 in ./task-3b-env/lib/python3.11/site-packages (from requests) (2.2.1)
        Requirement already satisfied: certifi>=2017.4.17 in ./task-3b-env/lib/python3.11/site-packages (from requests) (2024.2.2)
        Downloading requests-2.31.0-py3-none-any.whl (62 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 kB 782.5 kB/s eta 0:00:00
        Installing collected packages: requests
        Attempting uninstall: requests
            Found existing installation: requests 2.30.0
            Uninstalling requests-2.30.0:
            Successfully uninstalled requests-2.30.0
        Successfully installed requests-2.31.0
        ```

7. Check the list of packages
    ```
    > pip list
    ```
    ```
    Package            Version
    ------------------ -----------
    certifi            2024.2.2
    charset-normalizer 3.3.2
    idna               3.6
    numpy              1.26.4
    pandas             2.1.1
    pip                24.0
    python-dateutil    2.9.0.post0
    pytz               2024.1
    requests           2.31.0
    setuptools         65.5.0
    six                1.16.0
    tzdata             2024.1
    urllib3            2.2.1
    ```

8. Go back in the previous environment, and check the list of packages. See how we can have two different versions of ```requests```!

    **requests 2.30.0**
    ```
    Package            Version
    ------------------ -----------
    certifi            2024.2.2
    charset-normalizer 3.3.2
    idna               3.6
    numpy              1.26.4
    pandas             2.1.1
    pip                24.0
    python-dateutil    2.9.0.post0
    pytz               2024.1
    requests           2.30.0
    setuptools         65.5.0
    six                1.16.0
    tzdata             2024.1
    urllib3            2.2.1
    ```

    **requests 2.31.0**
    ```
    Package            Version
    ------------------ -----------
    certifi            2024.2.2
    charset-normalizer 3.3.2
    idna               3.6
    numpy              1.26.4
    pandas             2.1.1
    pip                24.0
    python-dateutil    2.9.0.post0
    pytz               2024.1
    requests           2.31.0
    setuptools         65.5.0
    six                1.16.0
    tzdata             2024.1
    urllib3            2.2.1
    ```     

### Solution


## Task 4 - Changing your python version
1. Install ```pyenv``` on your system.
2. Using ```pyenv``` , check the current version of the ```global``` and ```local``` interpreter
    - No local version should be available!
    - Check the path to the interpreter with ```which python``` – You should see some ```shims```!
3. How many different version of python can you install?
    - Tip: use the pipe operator and ```wc -l``` in your shell
    - The number should be north of 700
4. Install python 3.5 (specifying 3.5 is enough for pyenv to download the lastest 3.5 version, 3.5.10)
5. Create a new directory, move in, and specify a ```local``` 3.5 version for this directory
    - Check the ```local``` version of the interpreter again
    - run ```ls -a```: you should have a ```.python-version``` file, which configures the interpreter for this directory. Read it (it’s short!)
    - Check the output of ```python -V``` – it should be 3.5.10, and probably lower than what you got at step 2 (else, it is time to update your system!).
6. Within your new directory, create a virtual environment and activate it.
7. Install pandas with ```pip```
8. List the packages. Given the previous tasks, what can you say about pandas and numpy, and by extension about other packages?
9. Using pip, force installing pandas 2.1.1. What happens?
10. Deactivate your environment and remove the ```.python-version``` file and check the python version. It should match your system version.
11. Reactivate your environment. Check the python version. It should stay on 3.5.10! Your environment remembers the interpreter it was created with.
Remark: Removing ```.python-version``` file in your project folder is not recommended - this is for illustration purpose only!

### Solution
1. Install ```pyenv``` on your system.
    ```
    > brew update
    > brew install pyenv
    ```
    > **HOW-TO**: https://github.com/pyenv/pyenv

2. Using ```pyenv``` , check the current version of the ```global``` and ```local``` interpreter
    - No local version should be available!
    - Check the path to the interpreter with ```which python``` – You should see some ```shims```!
    ```
    > which python
    ```
    ```
    /Users/keetee/.pyenv/shims/python
    ```
    - Check the version of python with ```python -V```
    ```
    > python -V
    ```
    ```
    Python 3.11.6
    ```

3. How many different version of python can you install?
    - Tip: use the pipe operator and ```wc -l``` in your shell
    - The number should be north of 700
    ```
    > pyenv install --list | wc -l
    ```
    ```
    736
    ```
4. Install python 3.5 (specifying 3.5 is enough for pyenv to download the lastest 3.5 version, 3.5.10)
    ```
    > pyenv install 3.5
    ```
5. Create a new directory, move in, and specify a ```local``` 3.5 version for this directory
    - Check the ```local``` version of the interpreter again
        ```
        3.5
        ```
    - run ```ls -a```: you should have a ```.python-version``` file, which configures the interpreter for this directory. Read it (it’s short!)
        ```
        3.5
        ```
    - Check the output of ```python -V``` – it should be 3.5.10, and probably lower than what you got at step 2 (else, it is time to update your system!).
        ```
        Python 3.5.10
        ```
6. Within your new directory, create a virtual environment and activate it.
    ```
    > python3 -m venv task-4-env
    > source task-4-env/bin/activate
    ```
7. Install pandas with ```pip```
    ```
    > pip install pandas
    ```
    ```
    Collecting pandas
    Downloading https://files.pythonhosted.org/packages/b7/93/b544dd08092b457d88e10fc1e0989d9397fd32ca936fdfcbb2584178dd2b/pandas-0.25.3.tar.gz (12.6MB)
        100% |████████████████████████████████| 12.6MB 109kB/s
        Complete output from command python setup.py egg_info:
        Couldn't find index page for 'numpy' (maybe misspelled?)
        No local packages or working download links found for numpy>=1.13.3
        Traceback (most recent call last):
        File "<string>", line 1, in <module>
        File "/private/var/folders/yq/3gk6lvzx5jj4l_261ylkyn6c0000gn/T/pip-build-yfuockvs/pandas/setup.py", line 840, in <module>
            **setuptools_kwargs
        File "/Users/keetee/.pyenv/versions/3.5.10/lib/python3.5/distutils/core.py", line 108, in setup
            _setup_distribution = dist = klass(attrs)
        File "/Users/keetee/Projects/holberton/holbertonschool-back-end/pip/task-4/task-4-env/lib/python3.5/site-packages/setuptools/dist.py", line 315, in __init__
            self.fetch_build_eggs(attrs['setup_requires'])
        File "/Users/keetee/Projects/holberton/holbertonschool-back-end/pip/task-4/task-4-env/lib/python3.5/site-packages/setuptools/dist.py", line 361, in fetch_build_eggs
            replace_conflicting=True,
        File "/Users/keetee/Projects/holberton/holbertonschool-back-end/pip/task-4/task-4-env/lib/python3.5/site-packages/pkg_resources/__init__.py", line 850, in resolve
            dist = best[req.key] = env.best_match(req, ws, installer)
        File "/Users/keetee/Projects/holberton/holbertonschool-back-end/pip/task-4/task-4-env/lib/python3.5/site-packages/pkg_resources/__init__.py", line 1122, in best_match
            return self.obtain(req, installer)
        File "/Users/keetee/Projects/holberton/holbertonschool-back-end/pip/task-4/task-4-env/lib/python3.5/site-packages/pkg_resources/__init__.py", line 1134, in obtain
            return installer(requirement)
        File "/Users/keetee/Projects/holberton/holbertonschool-back-end/pip/task-4/task-4-env/lib/python3.5/site-packages/setuptools/dist.py", line 429, in fetch_build_egg
            return cmd.easy_install(req)
        File "/Users/keetee/Projects/holberton/holbertonschool-back-end/pip/task-4/task-4-env/lib/python3.5/site-packages/setuptools/command/easy_install.py", line 659, in easy_install
            raise DistutilsError(msg)
        distutils.errors.DistutilsError: Could not find suitable distribution for Requirement.parse('numpy>=1.13.3')
    ```
8. List the packages. Given the previous tasks, what can you say about pandas and numpy, and by extension about other packages?
    ```
    > pip list
    ```
    ```
    DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
    pip (9.0.1)
    setuptools (28.8.0)
    You are using pip version 9.0.1, however version 24.0 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.
    ```
    > **NOTE**: Python version determines which version of packages it can support! pandas requires numpy version >= 1.13.3

9. Using pip, force installing pandas 2.1.1. What happens?
    ```
    > pip install pandas==2.1.1
    ```
    ```
    Collecting pandas==2.1.1
    Could not find a version that satisfies the requirement pandas==2.1.1 (from versions: 0.1, 0.2, 0.3.0, 0.4.0, 0.4.1, 0.4.2, 0.4.3, 0.5.0, 0.6.0, 0.6.1, 0.7.0, 0.7.1, 0.7.2, 0.7.3, 0.8.0, 0.8.1, 0.9.0, 0.9.1, 0.10.0, 0.10.1, 0.11.0, 0.12.0, 0.13.0, 0.13.1, 0.14.0, 0.14.1, 0.15.0, 0.15.1, 0.15.2, 0.16.0, 0.16.1, 0.16.2, 0.17.0, 0.17.1, 0.18.0, 0.18.1, 0.19.0, 0.19.1, 0.19.2, 0.20.0, 0.20.1, 0.20.2, 0.20.3, 0.21.0, 0.21.1, 0.22.0, 0.23.0, 0.23.1, 0.23.2, 0.23.3, 0.23.4, 0.24.0, 0.24.1, 0.24.2, 0.25.0, 0.25.1, 0.25.2, 0.25.3)
    No matching distribution found for pandas==2.1.1
    You are using pip version 9.0.1, however version 24.0 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.
    ```

    > **NOTE**: Python version 3.5.10 only supports pandas version up to 0.25.3

10. Deactivate your environment and remove the ```.python-version``` file and check the python version. It should match your system version.
    ```
    Python 3.11.6
    ```
11. Reactivate your environment. Check the python version. It should stay on 3.5.10! Your environment remembers the interpreter it was created with.
    ```
    Python 3.5.10
    ```