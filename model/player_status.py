from enum import Enum, auto


class PlayerStatus(Enum):
    stopped = auto()
    playing = auto()
    loading = auto()
    ready = auto()

    def label(self):
        return {
            PlayerStatus.stopped: "Stopped",
            PlayerStatus.playing: "Playing",
            PlayerStatus.loading: "Loading",
            PlayerStatus.ready: "Ready"
        }[self]
