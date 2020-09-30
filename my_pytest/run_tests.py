import os
from config import RunConfig
import logging
import click
import pytest

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

@click.command()
@click.option('-m', default=None, help='输入运行模式：run 或 debug.')
def run(m):
    if m is None or m == "run":
        #logger.info("回归模式，开始执行✈✈！")
        pytest.main(["-s", "-v", RunConfig.cases_path,
                     "--maxfail", RunConfig.max_fail,
                     "--reruns", RunConfig.rerun])
        #logger.info("运行结束，生成测试报告♥❤！")
    elif m == "debug":
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", RunConfig.cases_path])
        print("运行结束！！")

if __name__ == '__main__':
    run()