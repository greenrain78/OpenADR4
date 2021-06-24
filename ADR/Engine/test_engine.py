"""
정상 작동하는지 임시로 구현한 테스트 엔진
드라이버
"""

from datetime import datetime

from DataProcessing.data_engine import DataEngine
from settings import siteId_list


class TestEngine:
    def __init__(self, data_engine: DataEngine):
        # DB 데이터 입출력
        self.data_engine = data_engine
        # api 사용
        self.data_receiver = DataReceiver()

    def test_hello(self):
        """
        간단 engine 동작 확인
        """
        print(f"hello {datetime.now()}", flush=True)

    def test_get_data(self):
        # 데이터를 읽어옴
        data = self.data_engine.read_data_elec('ace', 300, api_time="20200309")
        # 데이터를 저장
        self.data_engine.save_api_elec_raw('ace', data)
        # 화면에 표시
        # print(f"data : {data}", flush=True)

    def get_data_recent_month(self):

        # 각 사이트 별로 검색
        for siteId in siteId_list:
            pass


# data_engine = DataEngine()
# test = TestEngine(data_engine=data_engine)
# test.test_get_data()