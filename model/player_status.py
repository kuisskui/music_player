from enum import Enum, auto


class PlayerStatus(Enum):
    STOPPED = auto()
    PLAYING = auto()
    CHANGING_TRACK = auto()
    ENDED = auto()
    LOADING = auto()
    READY = auto()

    def label(self):
        return {
            PlayerStatus.STOPPED: "Stopped",
            PlayerStatus.PLAYING: "Playing",
            PlayerStatus.CHANGING_TRACK: "Changing",
            PlayerStatus.ENDED: "Finished",
            PlayerStatus.LOADING: "Loading",
            PlayerStatus.READY: "Ready"
        }[self]
