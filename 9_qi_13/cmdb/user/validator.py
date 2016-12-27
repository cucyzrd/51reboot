#encoding: utf-8

'''
===
rule:

'str' : {
    'type' : 'str',
    'empty' : True,
    'min_len' : None,
    'max_len' : None,
    'in' : [],
    'match' : '',
    'validate' : None
},
'int/float' : {
    'type' : 'int',
    'empty' : True,
    'min' : None,
    'max' : None,
    'in' : [],
    'validate' : None
},
'list' : {
    'type' : 'list',
    'empty' : True,
    'min_len' : None,
    'max_len' : None,
    'in' : [],
    'validate' : None
}
'''

NIL = lambda *args, **kwargs:True

ERROR_TYPE_CODE = 1
ERROR_TYPE_MSG = '类型不正确'
ERROR_TYPE_STR_MSG = '类型不是字符串'
ERROR_TYPE_INT_MSG = '类型不是整型'
ERROR_TYPE_NUM_MSG = '类型不是数字'
ERROR_TYPE_LIST_MSG = '类型不是列表'

ERROR_EMPTY_CODE = 2
ERROR_EMPTY_MSG = '内容不能为空'

ERROR_MAX_LEN_CODE = 3
ERROR_MAX_LEN_MSG = '不能超过%s个字符'

ERROR_MIN_LEN_CODE = 4
ERROR_MIN_LEN_MSG = '不能少于%s个字符'

ERROR_IN_CODE = 5
ERROR_IN_MSG = '不在%s范围内'

ERROR_MAX_CODE = 6
ERROR_MAX_MSG = '不能超过%s'

ERROR_MIN_CODE = 7
ERROR_MIN_MSG = '不能小于%s'

ERROR_LIST_MAX_CODE = 8
ERROR_LIST_MAX_MSG = '最多选择%s个元素'

ERROR_LIST_MIX_CODE = 9
ERROR_LIST_MIX_MSG = '最少选择%s个元素'

'''
验证函数
'''
def validate(o, key, rule):
    _type = rule.get('type', 'str')
    _func = globals().get('_validate_on_%s' % _type, NIL)
    return _func(o, key, rule)


'''
验证字符串类型
'''
def _validate_on_str(o, key, rule):
    _value = o.get(key, '').strip()
    if _value == '':
        if rule.get('empty', False):
            return True, 0, ''
        else:
            return False, ERROR_EMPTY_CODE, ERROR_EMPTY_MSG

    if rule.get('max_len', None) and len(_value) > rule.get('max_len'):
        return False, ERROR_MAX_LEN_CODE, ERROR_MAX_LEN_MSG % rue.get('max_len')

    if rule.get('min_len', None) and len(_value) < rule.get('min_len'):
        return False, ERROR_MIN_LEN_CODE, ERROR_MIN_LEN_MSG % rue.get('max_len')

    if rule.get('in', []) and _value not in rule.get('in', []):
        return False, ERROR_IN_CODE, ERROR_IN_MSG % ','.join(rule.get('in', []))

    if rule.get('match'):
        pass

    _callback = rule.get('validate')
    if _callback and callable(_callback):
        _status, _code, _msg = _callback(_value)
        if not _status:
            return False, _code, _msg

    return True, 0, ''


'''
验证整数类型
'''
def _validate_on_int(o, key, rule):
    return validate_on_num(o, key, rule, int)


'''
验证数字类型
'''
def _validate_on_float(o, key, rule):
    return validate_on_num(o, key, rule, float)


'''
验证数值类型
'''
def _validate_on_num(o, key, rule, clazz=int):
    _value = o.get(key, '').strip()
    if _value == '':
        if rule.get('empty', False):
            return True, 0, ''
        else:
            return False, ERROR_EMPTY_CODE, ERROR_EMPTY_MSG

    try:
        _value = clazz(_value)
    except BaseException as e:
        if clazz == int:
            return False, ERROR_TYPE, ERROR_TYPE_INT_MSG
        else:
            return False, ERROR_TYPE, ERROR_TYPE_NUM_MSG

    if rule.get('max') and _value > rule.get('max'):
        return False, ERROR_MAX_CODE, ERROR_MAX_MSG % rule.get('max')

    if rule.get('mix') and _value < rule.get('min'):
        return False, ERROR_MIX_CODE, ERROR_MIX_MSG % rule.get('min')

    if rule.get('in', []) and _value not in rule.get('in', []):
        return False, ERROR_IN_CODE, ERROR_IN_MSG % ','.join(map(str, rule.get('in', [])))

    _callback = rule.get('validate')
    if _callback and callable(_callback):
        _status, _code, _msg = _callback(_value)
        if not _status:
            return False, _code, _msg

    return True, 0, ''

'''
验证list
'''
def _validate_on_list(o, key, rule):
    _value = o.get(key, [])
    if not _value:
        if rule.get('empty', False):
            return True, 0, ''
        else:
            return False, ERROR_EMPTY_CODE, ERROR_EMPTY_MSG

    if not isinstance(_value, list):
        return False, ERROR_TYPE, ERROR_TYPE_LIST_MSG

    if rule.get('max_len') and len(_value) > rule.get('max_len'):
        return False, ERROR_LIST_MAX_CODE, ERROR_LIST_MAX_MSG % rule.get('max_len')

    if rule.get('mix_len') and _value < rule.get('min_len'):
        return False, ERROR_LIST_MIX_CODE, ERROR_LIST_MIX_MSG % rule.get('min_len')

    if rule.get('in', []) and len(set(_value) - set(rule.get('in', [])) != 0:
        return False, ERROR_IN_CODE, ERROR_IN_MSG % ','.join(map(str, rule.get('in', [])))

    _callback = rule.get('validate')
    if _callback and callable(_callback):
        _status, _code, _msg = _callback(_value)
        if not _status:
            return False, _code, _msg
