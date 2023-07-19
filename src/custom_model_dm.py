"""

generated with chatgpt with the prompt:

"create a set of nested pydantic models for this json data, using the key "name" to specify model types"

<json data>
"""

from typing import List, Union, Optional
from typing import Annotated, Literal
from pydantic import BaseModel, validator, Field
import numpy as np


class UserInput(BaseModel):
    Channel_Request: int = Field(None, alias="Channel Request")
    label: Optional[str] = None
    name: Literal["UserInput"]


class SetVoltage(BaseModel):
    voltage: float
    label: Optional[str] = None
    name: Literal["SetVoltage"]


class Wait(BaseModel):
    time_waited: float
    label: Optional[str] = None
    name: Literal["Wait"]


class Integrate(BaseModel):
    counts: int
    delta_time: float
    coincidences: int
    singles_rate_1: float
    singles_rate_2: float
    coincidence_rate: float
    label: Optional[str] = None
    name: Literal["Integrate"]


class PowerResults(BaseModel):
    expected_amps: float
    voltage_sent: float


class SetPower(BaseModel):
    result: PowerResults
    name: Literal["SetPower"]
    label: Optional[str] = None


class ExtremumResults(BaseModel):
    counts_list: List[int]
    times_list: List[float]
    direction_array: List[Union[float, int]]
    voltage_list: List[float]

class ValueIntegrateExtraData(BaseModel):
    # state: str
    name: str
    label: str
    counts: int
    delta_time: float
    coincidences_hist_1: np.ndarray
    coincidences_hist_2: np.ndarray
    full_coinc_1: np.ndarray
    full_coinc_2: np.ndarray
    singles_hist_1: np.ndarray
    singles_hist_2: np.ndarray
    total_coincidences: int

    # these are heavy arrays, so don't validate every element
    @validator('coincidences_hist_1', 'coincidences_hist_2', 'full_coinc_1', 'full_coinc_2', pre=True)
    def to_numpy_float(cls, value):
        return np.array(value, dtype=float)
    
    @validator('singles_hist_1', 'singles_hist_2', pre=True)
    def to_numpy_int(cls, value):
        return np.array(value, dtype=int)
    
    class Config:
        arbitrary_types_allowed = True


class Extremum(BaseModel):
    results: ExtremumResults
    integration_results: List[ValueIntegrateExtraData]
    label: Optional[str] = None
    name: Literal["Extremum"]

class SimpleSet(BaseModel):
    results: List[ValueIntegrateExtraData]
    label: Optional[str] = None
    name: Literal["SimpleSet"]


class CombineStringStores(BaseModel):
    new_store: str = Field(None, alias="new store")
    label: Optional[str] = None
    name: Literal["CombineStringStores"]


class DerivedVoltages(BaseModel):
    derived_max_voltage: float
    derived_90_voltage: float
    label: Optional[str] = None
    name: Literal["DerivedVoltages"]

Measurement = Annotated[
    Union[
        UserInput,
        SetVoltage,
        Wait,
        Extremum,
        SetPower,
        Integrate,
        CombineStringStores,
        DerivedVoltages,
        SimpleSet
    ],
    Field(discriminator="name"),
]


class DensityMatrixData(BaseModel):
    state: str
    name: Optional[str] = None
    label: Optional[str] = None
    results: List[Measurement]

    # Use a validator to check that each result is of the correct type for its name
    # @validator("results")
    # def check_results(cls, results):
    #     for result in results:
    #         if result.name == "UserInput":
    #             assert isinstance(result, UserInput)
    #         elif result.name == "SetVoltage":
    #             assert isinstance(result, SetVoltage)
    #         elif result.name == "Wait":
    #             assert isinstance(result, Wait)
    #         elif result.name == "Integrate":
    #             assert isinstance(result, Integrate)
    #         elif result.name == "SetPower":
    #             assert isinstance(result, SetPower)
    #         elif result.name == "Extremum":
    #             assert isinstance(result, Extremum)
    #     return results
