
#!/bin/bash

nohup python hourly.py > output.log 2>&1 & echo $! > pid.file

echo "Python script has been started in the background."
