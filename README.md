# Random Melody Generator

Generate random melody under specific rules.

## Getting started
### Prerequisites
This project is written in [Python](https://www.python.org/) 3.6. I haven't tested in other versions.

[MIDIUtil](https://github.com/MarkCWirt/MIDIUtil) library is used in my project. You can install it simply by using `pip`:

```console
pip install MIDIUtil
```

### How to use?
Simply run `main.py`. A standard MIDI file will be generated in `output` folder. The filename is `midi_{timestamp}.mid`.

You can play it using a media player (e.g. Windows Media Player) or import it into a Digital Audio Workstation (DAW).

## Customize
By default, the melody is in major pentatonic scale, chord progression is C-Am-F-G (1-6-4-5), and percussion pattern is fixed. Also, the interval of notes within a phrase is constrained.

The rules can be modified in `rules.json`.

You can also adjust the length of song and tempo in `song_settings.json`.

### rules.json

| Parameter  | Description |
| ------------- | ------------- |
| `notes`  | Defines the notes used for composition.  |
| `interval_upper`  | Defines the upper bound of interval of notes. The values in this list will be randomly chosen.  |
| `interval_lower`  | Defines the lower bound of interval of notes. The values in this list will be randomly chosen.  |
| `rhythm`  | Defines rhythm pattern for melody. The numbers are in beats (quarter notes).  |
| `seq_chord` | Defines the chord sequence. Notes in each sub-array will be played simultaneously to form a chord.  |
| `seq_perc` | Defines the percussion sequence. The first element in the sub-array denotes the drum sound, and the second element denotes time value in beats.  |
| `velocity` | Defines the velocity of strong, intermediate and weak beats.  |

### song_settings.json

| Parameter  | Description |
| ------------- | ------------- |
| `length`  | Defines the length of song.  |
| `tempo`  | Defines the tempo of song, measured in Beats per Minute (BPM).  |

## Credits
- The whole project is written in Python ([python.org](https://www.python.org/)).
- The project uses [MIDIUtil](https://github.com/MarkCWirt/MIDIUtil) library by [MarkCWirt](https://github.com/MarkCWirt).
- I would appreciate [ScoreDraft](https://github.com/fynv/ScoreDraft) by [fynv](https://github.com/fynv). My project is partially inspired by ScoreDraft. Since ScoreDraft uses scripts to compose music, I found its potential to automatically generate music. My algorithm of randomly generating melody was initially tested on ScoreDraft.
