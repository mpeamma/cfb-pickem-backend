from dataclasses import dataclass
from typing import List, Optional
from dataclasses_json import DataClassJsonMixin, dataclass_json

@dataclass_json
@dataclass
class Group(DataClassJsonMixin):
    name: str
    users: List[str]
    id: Optional[str] = None
    creator: Optional[str] = None
