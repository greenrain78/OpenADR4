"""
정상 작동하는지 임시로 구현한 테스트 엔진
드라이버
"""

from datetime import datetime
from DataProcessing.API.data_receiver import API_Receiver
from Engine.data_engine import DataEngineELEC, DataEngineEQPS
from settings import siteId_list


class TestEngine:
    """
    정상 작동하는지 임시로 구현한 테스트 엔진
    """
    def __init__(self):
        # DB 데이터 입출력
        self.data_ELEC = DataEngineELEC()
        self.data_EQPS = DataEngineEQPS()
        # api 사용
        self.api_receiver = API_Receiver()

    def test_hello(self):
        """
        간단 engine 동작 확인
        """
        print(f"hello {datetime.now()}", flush=True)

    def test_get_data(self):
        """
        api를 통해 요청받은 데이터를 DB까지 정상적으로 전달되는지 테스트
        """
        # 데이터를 읽어옴
        data = self.api_receiver.read_api_elec('ace', 300, api_time="20200309")
        # 데이터를 저장
        self.data_ELEC.save_by_api('ace', data)
        # 화면에 표시
        print(f"data : {data}", flush=True)

    def get_data_recent_month(self):

        # 각 사이트 별로 검색
        for siteId in siteId_list:
            pass


# data_engine = DataEngine()
# test = TestEngine(data_engine=data_engine)
# test.test_get_data()