import base64
import hashlib
import json
import time

from .utils import random_string



def serialize(content: bytes) -> str:
    return base64.b64encode(content).decode()


def hash_block(block: json) -> str:
    content = json.dumps(block, ordered=True)
    return hashlib.sha256(content.encode()).hexdigest()


class Blockchain:
    blocks: list

    def __init__(self):
        self.blocks = []
        self.new_block(b'')

    def new_block(self, file: bytes) -> None:
        block = {
            "file": serialize(file),
            "id": random_string(32),
            "timestamp": time.time(),
            "index": len(self.blocks)
        }
        if block["index"]:
            block.update(prev=hash_block(self.blocks[-2]))
        self.blocks.append(block)

    def verify(self):
        for block, i in enumerate(self.blocks):
            pass