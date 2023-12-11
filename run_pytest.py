import pytest
import subprocess

pytest.main()

#生成allure报告
subprocess.call('allure generate ./result/temp -o ./result/report --clean', shell=True)
#自动打开生成的allure报告
subprocess.call('allure open -h 127.0.0.1 -p 8883 ./result/report', shell=True)