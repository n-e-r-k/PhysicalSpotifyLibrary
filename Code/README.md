# Code Directory

## Files

- *cacheGenerator.py* - A tool to generate an authentication cache for initial setup of a headless PSL.
- *data.csv* - The main database containing the UID to URI associations.
- *findDevices.py* - A program to display all devices attached to connected spotify account.
- *PSL_Play.py* - The main runtime for the PSL. Using the PSL library as it's backbone.
- *PSL_Write.py* - A program to associate UIDs to URIs.
- *PSL.py* - The main library powering the whole project. Manages all interfacing with spotify and peripherals.
- *PSLC.py* - PSL Connect is the visualization software to display the album artwork as well as the current playing song.
- *timeout.py* - A needed library for RFID timeouts to enable "None" cart reads.

## Directories

- *Legacy* - Initial code from when there was an Arduino acting as a middle man.