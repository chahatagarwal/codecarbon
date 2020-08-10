"""
Provides functionality for unit conversions
"""

from dataclasses import dataclass


@dataclass
class CO2EmissionsPerKwh:
    """
    Measured in kg/kwh
    """

    LBS_MWH_TO_KG_KWH = 0.00045359237
    G_KWH_TO_KG_KWH = 0.001

    kgs_per_kwh: float

    @classmethod
    def from_lbs_per_mwh(cls, lbs_per_mwh: float) -> "CO2EmissionsPerKwh":
        return cls(kgs_per_kwh=lbs_per_mwh * CO2EmissionsPerKwh.LBS_MWH_TO_KG_KWH)

    @classmethod
    def from_g_per_kwh(cls, g_per_kwh: float) -> "CO2EmissionsPerKwh":
        return cls(kgs_per_kwh=g_per_kwh * CO2EmissionsPerKwh.G_KWH_TO_KG_KWH)

    @classmethod
    def from_kgs_per_kwh(cls, kgs_per_kwh: float) -> "CO2EmissionsPerKwh":
        return cls(kgs_per_kwh=kgs_per_kwh)


@dataclass
class Energy:
    """
    Measured in kwh
    """

    kwh: float

    @classmethod
    def from_power_and_time(cls, *, power: "Power", time: "Time") -> "Energy":
        return cls(kwh=power.kw * time.hours)

    @classmethod
    def from_energy(cls, kwh: float) -> "Energy":
        return cls(kwh=kwh)

    def __add__(self, other: "Energy") -> "Energy":
        return Energy(self.kwh + other.kwh)

    def __iadd__(self, other: "Energy") -> "Energy":
        return Energy(self.kwh + other.kwh)


@dataclass
class Power:
    """
    Measured in kw
    """

    MILLI_WATTS_TO_WATTS = 0.001
    WATTS_TO_KILO_WATTS = 0.001

    kw: float

    @classmethod
    def from_milli_watts(cls, milli_wats: float) -> "Power":
        return cls(
            kw=milli_wats * Power.MILLI_WATTS_TO_WATTS * Power.WATTS_TO_KILO_WATTS
        )


@dataclass
class Time:
    """
    Measured in seconds
    """

    SECONDS_TO_HOURS = 0.00027777778

    seconds: float

    @property
    def hours(self) -> float:
        return self.seconds * Time.SECONDS_TO_HOURS

    @classmethod
    def from_seconds(cls, seconds: float) -> "Time":
        return cls(seconds=seconds)
