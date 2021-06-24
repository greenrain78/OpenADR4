"""
api를 사용하여 데이터를 가져오는 객체
지정된 형식에 맞게 api를 요쳥
"""

from datetime import datetime
from typing import Dict

from DataProcessing.API.adr_api_client import ADR_API_Client


class API_Receiver(object):
    """
    api를 사용하여 데이터를 가져오는 객체
    지정된 형식에 맞게 api를 요쳥
    """
    def __init__(self):
        self.adr_api = ADR_API_Client()

    def read_api_elec(self, siteId, perfId, api_time) -> Dict:
        """
        api를 사용하기 위해 인자를 받음
        :param siteId:
        :param perfId:
        :param api_time:
        :return:
        """
        # 오늘 날짜 기준으로 데이터를 받음
        if api_time == "now":
            req_time = datetime.now().strftime("%Y%m%d")  # 오늘 날짜를 api 형식에 맞게 변형
            req_time = req_time[:-1] + '2'
            print(f"api 데이터 수집: {req_time}", flush=True)
            data = self.adr_api.fetch_elec(siteId, perfId, req_time)
            return data
        else:
            data = self.adr_api.fetch_elec(siteId, perfId, api_time)
            return data

    def read_api_eqps(self, siteId) -> Dict:
        """
        site id을 입력받아 설비 정보를 가져온다
        :param siteId:
        :return:
        """
        data = self.adr_api.fetch_eqps(siteId)
        return data
