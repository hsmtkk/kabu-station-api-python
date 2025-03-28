import enum


class FutureCode(enum.StrEnum):
    NK225 = "NK225"
    NK225mini = "NK225mini"
    VI = "VI"


class OptionCode(enum.StrEnum):
    NK225op = "NK225op"
    NK225miniop = "NK225miniop"


class PutOrCall(enum.StrEnum):
    Put = "P"
    Call = "C"
