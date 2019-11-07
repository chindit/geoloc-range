# geoloc-range
A python script to add/remove meters to a specific geolocation (latitude and longitude)

### Usage
Just run `python main.py` and follow instructions.

### Example
As an example, you can have this result:

```shell script
$ python main.py 
Do you want to use separate latitude and longitude or enter a geolocation string (ex: 1.234, 4.567) ? Choices are S(eparate) or T(ogether).Default is Together [s/T]: t
Enter coordinates: 1.234, 5.678
Enter radius in meters: 25
Latitudes:
    Min: 1.233777
    Max: 1.234223
Longitudes:
   Min: 5.677551
   Max: 5.678449
Add a new coordinate ? [Y/n] n
Bye

```