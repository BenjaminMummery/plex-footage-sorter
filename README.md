# Phone Footage Sorter

A simple script to process android phone footage default names into plex-friendly filename

<!--TOC-->

- [Phone Footage Sorter](#phone-footage-sorter)
  - [Description](#description)
  - [Caveats](#caveats)
    - [Part Naming](#part-naming)

<!--TOC-->

## Description

This tool is designed for the highly-specific case where you have a lot of files with names like `20231116_104404.mp4` that you want to make available in [Plex] in the form of a date-based series structure.

The script scans the input directory for filenames matching the pattern `YYYYMMDD_SSSSSS.EXT` and renames them to the format `CUSTOMSERIESNAME-YYYY-MM-DD[ - PartX].EXT`.

## Caveats

### Part Naming

We number parts consecutively for a single day.
If there are more videos for that day that are not in the folder, the part numbering will be wrong.
We might fix this at a later date.
