
#!/bin/bash

# Killing the process
if [ ! -f pid.file ]; then
    echo "pid.file does not exist. Process may not be running."
else
    kill $(cat pid.file)
    rm pid.file
    echo "Python script has been stopped."
fi
