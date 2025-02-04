from typing import NamedTuple


class Config(NamedTuple):
    host: str = ""
    max_retries: int = 3
    max_connections: int = 12
    timeout: int =30


DefaultConfig = Config(host="localhost:9001")
