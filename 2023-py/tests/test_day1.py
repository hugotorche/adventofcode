from runs.day1 import total_calibration


def test_calibrations():
    assert total_calibration(['eightone9nbdrkonenine8']) == 88
    assert total_calibration(['nzgtvl4tvseven']) == 47
    assert total_calibration(['gbtwoneftrjc733four']) == 24
    assert total_calibration(['8pljqhtm']) == 88
    assert total_calibration(['sixfconesix6three1sixsix']) == 66
    assert total_calibration(['3five4two1dbqztzfxrxfdhh']) == 31
