from odmantic import Field, Model, Reference

from .section import Section


class Staff(Model):
    name: str = Field(description="员工名")
    tags: list[str] = Field(description="员工标签")
    user_id: str = Field(description="绑定的 Fief User ID")
    section: Section = Reference()
