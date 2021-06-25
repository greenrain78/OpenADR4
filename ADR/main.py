from logging import getLogger

from Controller.schedule_manager import MainScheduler
from Engine.test_engine import TestEngine

log = getLogger(__name__)

if __name__ == '__main__':

    # 로거 설정
    # create_log_setting()

    # 객체 설정
    scheduler = MainScheduler()
    test_engine = TestEngine()

    # log.info('start main')

    if False:
        # 작업 생성
        # 매 10초에 hello출력
        scheduler.create_job(test_engine.test_hello, "test hello", second=0)
        # # 매 40초에 api로 데이터를 받아와 DB에 저장
        # scheduler.create_job(test_engine.test_get_data, "test get date", second=20)
        #
        scheduler.create_job(test_engine.get_data_recent, "get_data_recent", second=40)

        # 실행
        scheduler.run()
    else:
        test_engine.get_data_recent()

    # 프로그램 종료 방지
    print("main python start q")
    while True:
        pass

    print("end")
