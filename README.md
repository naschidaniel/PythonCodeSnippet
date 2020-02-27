# Description

A small example program for a Python script that runs in a Docker container. The program contains an argparse and logging module.

# Quick start
The project needs `python`, `invoke`, `docker` and `docker-compose`. For details and information on the versions of the dependencies, see the [Contributing Guide](./CONTRIBUTING.md).


# Get help from the main program

```
python ./task.py local.python "main.py -h"
```


# Example

```
python ./task.py local.python "main.py --name Rudi --settings en"
```
Expected result: Hello my name is Rudi!


# Settings
## Program settings

The available settings can be made in the `availableSettings.json` file.

```
vim program/availableSettings.json
```


## Settings for the logger

The settings for the logger can be made in the file `misc/logging.cfg`. For the fileHandler, only the logLevel `info` is logged. For the consoleHandler the logLevel `debug` is used.

```
[handler_fileHandler]
args=('%(logfilename)s','a') # will append to the logfile
args=('%(logfilename)s','w') # will create a new logfile
```



# Contribution
Please make sure to read the [Contributing Guide](./CONTRIBUTING.md) before making a pull request.



# License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2020-present, Daniel Naschberger
