import nixops.statefile
from nixops.storage import StorageBackend
from nixops.util import ImmutableValidatedObject


class MemoryBackendOptions(ImmutableValidatedObject):
    pass


class MemoryBackend(StorageBackend[MemoryBackendOptions]):
    __options = MemoryBackendOptions

    @staticmethod
    def options(**kwargs) -> MemoryBackendOptions:
        return MemoryBackendOptions(**kwargs)

    def __init__(self, args: MemoryBackendOptions) -> None:
        pass

    # fetchToFile: acquire a lock and download the state file to
    # the local disk. Note: no arguments will be passed over kwargs.
    # Making it part of the type definition allows adding new
    # arguments later.
    def fetchToFile(self, path: str, **kwargs) -> None:
        pass

    def onOpen(self, sf: nixops.statefile.StateFile, **kwargs) -> None:
        sf.create_deployment()

    # uploadFromFile: upload the new state file and release any locks
    # Note: no arguments will be passed over kwargs. Making it part of
    # the type definition allows adding new arguments later.
    def uploadFromFile(self, path: str, **kwargs) -> None:
        pass