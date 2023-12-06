from typing import List, Optional

from pydantic import BaseModel


class LevelInfo(BaseModel):
    id: str
    level: int = 0


class AvatarInfo(BaseModel):
    id: str
    name: str
    icon: str


class PathInfo(BaseModel):
    id: str
    name: str
    icon: str


class ElementInfo(BaseModel):
    id: str
    name: str
    color: str
    icon: str


class SkillInfo(BaseModel):
    id: str
    name: str
    level: int
    max_level: int
    element: Optional[ElementInfo]
    type: str
    type_text: str
    effect: str
    effect_text: str
    simple_desc: str
    desc: str
    icon: str


class SkillTreeInfo(BaseModel):
    id: str
    level: int
    anchor: str
    max_level: int
    icon: str
    parent: Optional[str] = None


class AttributeInfo(BaseModel):
    field: str
    name: str
    icon: str
    value: float
    display: str
    percent: bool


class PropertyInfo(BaseModel):
    type: str
    field: str
    name: str
    icon: str
    value: float
    display: str
    percent: bool


class SubAffixInfo(PropertyInfo):
    count: int
    step: int


class SubAffixBasicInfo(BaseModel):
    id: str
    cnt: int
    step: int = 0


class RelicBasicInfo(BaseModel):
    id: str
    level: int = 1
    main_affix_id: Optional[str] = None
    sub_affix_info: List[SubAffixBasicInfo] = []


class LightConeBasicInfo(BaseModel):
    id: str
    rank: int = 1
    level: int = 1
    promotion: int = 0


class CharacterBasicInfo(BaseModel):
    id: str
    rank: int = 0
    level: int = 1
    promotion: int = 0
    skill_tree_levels: List[LevelInfo] = []
    light_cone: Optional[LightConeBasicInfo] = None
    relics: Optional[List[RelicBasicInfo]] = None


class RelicInfo(BaseModel):
    id: str
    name: str
    set_id: str
    set_name: str
    rarity: int
    level: int
    icon: str
    main_affix: Optional[PropertyInfo] = None
    sub_affix: List[SubAffixInfo] = []


class RelicSetInfo(BaseModel):
    id: str
    name: str
    icon: str
    num: int
    desc: str = ""
    properties: List[PropertyInfo] = []


class LightConeInfo(BaseModel):
    id: str
    name: str
    rarity: int
    rank: int
    level: int
    promotion: int
    icon: str
    preview: str
    portrait: str
    path: Optional[PathInfo] = None
    attributes: List[AttributeInfo] = []
    properties: List[PropertyInfo] = []


class CharacterInfo(BaseModel):
    id: str
    name: str
    rarity: int
    rank: int
    level: int
    promotion: int
    icon: str
    preview: str
    portrait: str
    rank_icons: List[str] = []
    path: Optional[PathInfo] = None
    element: Optional[ElementInfo] = None
    skills: List[SkillInfo] = []
    skill_trees: List[SkillTreeInfo] = []
    light_cone: Optional[LightConeInfo] = None
    relics: List[RelicInfo] = []
    relic_sets: List[RelicSetInfo] = []
    attributes: List[AttributeInfo] = []
    additions: List[AttributeInfo] = []
    properties: List[PropertyInfo] = []
