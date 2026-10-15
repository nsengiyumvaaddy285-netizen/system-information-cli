System Information CLI

A command-line application built with Python that collects and displays system information using the psutil and standard-library modules.

Features:

System information:
operating system, machine architecture, Python version, hostname, processor information, physical CPU cores and CPU usage.

Memory information:
RAM usage, total RAM and swap memory statistics.

Storage information: 
disk space used, total disk space and percentage of storage used.

Interactive menu: choose which information to display or view all available information at once.

Formatted output: 
readable sections with memory and storage measurements displayed in gigabytes.

Requirements:
Python version 3.14, psutil installed.

Personal Notes: This project was developed as part of my Python learning journey towards cloud engineering and DevOps.

During development, I practised collecting system metrics (like basic ram and cpu usage), storing related data in a dictionary, separating data collection from presentation, formatting numerical output and implementing a menu-driven command-line interface.
I started out with a basic form containing only print code, and kept evolving, improving both the efficiency and readability of the code as I went on.

This project helped me apply core Python concepts to a practical system-monitoring task. Proving to be a good first project. 