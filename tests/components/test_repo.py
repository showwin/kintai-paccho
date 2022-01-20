from components.repo import Employee

def test_create():
    Employee.create('test_user', 'test_key')
    assert Employee.get_key('test_user') == 'test_key'

def test_get_key():
    Employee.create('test_user', 'test_key')
    assert Employee.get_key('test_user') == 'test_key'
    assert Employee.get_key('user_not_exist') == None
    Employee._refresh_cache()
    assert Employee.get_key('test_user') == 'test_key'
    assert Employee.get_key('user_not_exist') == None

def test_update_timezone():
    Employee.update_timezone('test_user', '+09:00')
    assert Employee.get_timezone('test_user') == '+09:00'
    Employee.update_timezone('test_user', '-02:00')
    assert Employee.get_timezone('test_user') == '-02:00'
    Employee.update_timezone('test_user_1', '+17:00')
    assert Employee.get_timezone('test_user_1') == '+17:00'
    assert Employee.get_timezone('test_user') == '-02:00'

def test_get_timezone():
    Employee.update_timezone('test_user', '+09:00')
    assert Employee.get_timezone('test_user') == '+09:00'
    assert Employee.get_timezone('user_not_exist') == None
    Employee._refresh_cache()
    assert Employee.get_timezone('test_user') == '+09:00'
    assert Employee.get_timezone('user_not_exist') == None
