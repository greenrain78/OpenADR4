"""
데이터를 관리하는 엔진
데이터를 사용할때 해당 객체를 이용해서 사용
해당 함수의 의미를 가지는 기능을 포괄적으로 담당
개념적인 기능을 수행

"""

from logging import getLogger

from DataProcessing.DB.data_manager import DBAdapterELEC, DBAdapterEQPS

log = getLogger(__name__)


class DataEngine:
    """
    데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """


class DataEngineELEC(DataEngine):
    """
    ELEC 데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self):
        self.db = DBAdapterELEC()

    def save(self):
        pass

    def read(self):
        pass

    def update(self):
        pass


class DataEngineEQPS(DataEngine):
    """
    EQPS 데이터를 사용하는 엔진
    해당 데이터를 다루는 모든 조작을 담당
    """

    def __init__(self):
        self.db = DBAdapterEQPS()

    def save(self):
        pass

    def read(self):
        pass

    def update(self):
        pass



