# CSV_Report_Processing

This script is intended to read CSV input file from current working
directory and write proper report file aggregated by date
and country code.

Example input lines:
```
    01/21/2019,Mandiana,883,0.38%
    01/22/2019,Berlin,139,0.61%
```
Example output lines:
```
    2019-01-21,GIN,883,3
    2019-01-22,DEU,139,1
```
## Installation

Clone this repository to your computer using link:

```
    https://github.com/Sonny-skyez/CSV_Report_Processing.git
```

Use package manager [pip](https://pypi.org/project/pip/) to install required Python packages:

```
    pip install chardet
    pip install pycountry
```
## Usage

To use this script you need to:

- copy input *.csv* file to a script working directory
![alt text](https://i.ibb.co/dfmxg1w/Zrzut-ekranu-2019-02-08-o-16-33-17.png)


- run [Main.py](https://github.com/Sonny-skyez/CSV_Report_Processing/blob/master/Main.py) with Python interpreter.

-
