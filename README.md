<!--- Copyright (c) 2023 Benjamin Mummery -->

# Plex Footage Sorter

A simple script to process android phone footage default names into plex-friendly filename

<!--TOC-->

- [Plex Footage Sorter](#plex-footage-sorter)
  - [Description](#description)
  - [Renaming phone footage as date-based series](#renaming-phone-footage-as-date-based-series)
    - [Caveat - Part Naming](#caveat---part-naming)
  - [Renaming Movpilot downloads as season-based series](#renaming-movpilot-downloads-as-season-based-series)

<!--TOC-->

## Description

This package bundles a set of tools for renaming and/or moving files from various sources into plex-friendly patterns.
Most of these are highly specific.

## Renaming phone footage as date-based series

Android phones (and possible iPhones, we haven't checked) name video files in the format `YYYYMMDD_SSSSSS.EXT`.
Plex can interpret video files as a date-based tv series if they are named in the format `SERIESNAME-YYYY-MM-DD[ - PartX].EXT`.
This tool is designed for the case where you take a lot of phone footage that you want to organise into a chronological series.
We use it for organising our videos of our progress at learning various activities.

To use this utility, dump all of the relevant footage into a folder, and run

```bash
plex-footage-sorter date-based SERIESNAME
```

### Caveat - Part Naming

We number parts consecutively for a single day.
If there are more videos for that day that are not in the folder, the part numbering will be wrong.
We might fix this at a later date.

## Renaming Movpilot downloads as season-based series

Movpilot downloads of series episodes do not fit plex structures.
For example, downloads from Amazon Prime follow the structure:

```txt
root
└── Castlevania
    ├── 1
    |   └── S01E001_witchbottle.mp4
    └── 2
        └── S02E002_old_homes.mp4
```

whereas Plex would expect these to look like:

```txt
root
└── Castlevania
    ├── Season01
    |   └── Castlevania - S01E01 - witchbottle.mp4
    └── Season02
        └── Castlevania - S02E02 - old homes.mp4
```

Renaming these by hand is tedious, so we have developed the `movpilot-series` utility.

To use this utility, run

```bash
plex-footage-sorter movpilot-series
```

in the root directory.
