# python-file-system-simulator
A command line file management system built in Python using lists and dictionaries.

# Python File System Simulator

## Overview
This project is a command line simulation of a basic file management system, created as part of my independent learning in Python. It demonstrates fundamental programming concepts including lists, dictionaries, and user interaction.

## Features

### v1
- Created files with names, content, and authors
- Viewed stored files
- Searched for files
- Deleted files

### v2
- Added password authentication
- Added three login attempts before access is denied
- Refactored authentication into a reusable login() function
- Improved code organisation for future development

### v3
- Added persistent file storage using text files
- Files can now be saved and loaded between program sessions
- Added the ability to edit existing files

### v4: Current version
- Simulated storage system based on file content size
- Configurable storage limit
- Storage usage warnings when nearing capacity
- Prevents files from being created if storage is exceeded
- Prevents rewrites that would exceed available storage
- Improved case-insensitive file searching and deletion

The simulator uses a simplified storage model where each character in a file's content represents 1 byte.

e.g. hello = 5 'bytes' of storage used

The system tracks total usage and prevents files being added if they exceed the storage limit.

### future v4.1
- Metadata

## Skills demonstrated
- Python programming
- Lists and dictionaries
- Functions and code organisation
- File handling and persistent storage
- User input validation
- Problem solving and debugging

## Future improvements
- Graphical user interface
- User accounts with separate files
- More advanced file organisation, including folders
- Improved storage methods

## Why did I make this?
To practise Python programming while exploring how a simple file management system could be developed. The project has been expanded gradually to improve functionality, organisation, and usability.
