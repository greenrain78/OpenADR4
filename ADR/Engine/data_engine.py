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

    def save_by_api(self, siteId, data):
        """
        api로 부터 받아온 데이터를 그대로 DB에 저장
        :param siteId:
        :param data: 데이터
        :return:
        """
        data_list = data.get('elecs')
        for data in data_list:
            # 데이터 전처리 필요
            self.db.insert_api_raw(siteId, data)
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



