from odmantic import Field, Model


class Section(Model):
    name: str = Field(description="部门名称")
