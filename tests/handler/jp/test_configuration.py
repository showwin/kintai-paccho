from handler.jp.configuration import _valid_timezone

def test__valid_timezone():
    assert _valid_timezone('+09:00') == True
    assert _valid_timezone('-12:00') == True
    assert _valid_timezone('+00:00') == True
    assert _valid_timezone('-00:00') == True
    assert _valid_timezone('+11:30') == True
    assert _valid_timezone('-09:30') == True
    assert _valid_timezone('+23:00') == True
    assert _valid_timezone('++12:00') == False
    assert _valid_timezone('12:00') == False
    assert _valid_timezone('+9') == False
    assert _valid_timezone('-12') == False
    assert _valid_timezone('+18') == False
    assert _valid_timezone('+34:00') == False
    assert _valid_timezone('-24:00') == False
    assert _valid_timezone('00:00') == False
