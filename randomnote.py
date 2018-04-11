# -*- coding: utf-8 -*-

import random


class RandomNote(object):
    def __init__(self, choose_from, interval_upper, interval_lower):
        self.last_played = 0
        self.notes = choose_from
        self.interval_upper = interval_upper
        self.interval_lower = interval_lower

    def random_note(self):
        while True:
            note = random.choice(range(1, len(self.notes) + 1))
            if not self.last_played:
                break
            else:
                # 音程限制
                if random.choice(self.interval_upper) \
                        >= abs(note - self.last_played) \
                        >= random.choice(self.interval_lower):
                    break
                else:
                    continue
        self.last_played = note
        return self.notes[self.last_played - 1]

    def reset(self):
        self.last_played = 0
