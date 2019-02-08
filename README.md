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

- copy input *.csv* file to a script working directory, file format should be:
```
01/21/2019,Mandiana,883,0.38%
01/21/2019,Lola,76,0.78%
01/22/2019,Lola,201,0.82%
01/22/2019,Beroun,139,0.61%
01/22/2019,Mandiana,1050,0.93%
01/23/2019,Unknown,777,0.22%
01/23/2019,Gaoual,72,0.7%
01/23/2019,Lola,521,0.19%
01/24/2019,Beroun,620,0.1%
01/24/2019,Unknown,586,0.86%
01/24/2019,Unknown,1082,0.68%
```
- run [Main.py](https://github.com/Sonny-skyez/CSV_Report_Processing/blob/master/Main.py) with Python interpreter.

-
