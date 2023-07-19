from pydantic import BaseModel, validator
import numpy
from typing import List


class Model(BaseModel):
    values: numpy.ndarray

    @validator('values', pre=True)
    def parse_values(v):
        return numpy.array(v, dtype=float)

    class Config:
        arbitrary_types_allowed = True


print("generating")
big_list = numpy.random.rand(1000000).tolist()
print("starting model creation: ")
m = Model(values=big_list)
print(m)
print(type(m))