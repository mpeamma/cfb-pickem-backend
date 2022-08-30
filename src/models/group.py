from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin, dataclass_json

@dataclass_json
@dataclass
class Group(DataClassJsonMixin):
    id: int
    name: str
