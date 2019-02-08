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
