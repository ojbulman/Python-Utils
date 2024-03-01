import re
from six import string_types


def boolean_str(val, allow_empty=False):
    if allow_empty and (val is None): val = ""
    if not isinstance(val, str): return False
    if allow_empty and val=="": return True
    if val == "True": return True
    if val == "False": return True
    return False


def boolean(val):
    return isinstance(val,bool)


def timezone(val):
    if not isinstance(val,str): return False
    import pytz
    if val in pytz.all_timezones: return True
    return False


def string(val, allow_empty=False, min_length=None):
    if allow_empty and (val is None): val = ""
    if not isinstance(val, str): return False
    if allow_empty and val.strip() == "": return True
    if not allow_empty and val.strip() == "": return False
    if min_length and len(val.strip()) < min_length: return False
    return True


def ip_address(val, allow_empty=False):
    if allow_empty and (val is None): val = ""
    if not isinstance(val, str): return False
    if allow_empty and val.strip() == "": return True
    if val.count('.') != 3: return False

    parts = val.split('.')
    for p in parts:
        if p.isnumeric() == False: return False
        if int(p)<0: return False
        if int(p)>255: return False
    
    return True


def email_address(val, allow_empty=False):
    if allow_empty and (val is None): val = ""
    if not isinstance(val, str): return False
    if allow_empty and val.strip() == "": return True
    if val.count('@') != 1: return False
    if val.count('.') <1: return False
    if val[:1]=='@' or val[:1]=='.': return False
    if val[-1:]=='@' or val[-1:]=='.': return False
    return True


def password(val, min_length=10, req_numbers=True, req_mix_case=True, req_special_chars=True, accepted_special_chars='[@_-!£$%^&*<>?/\|}{~:]#'):
    if not isinstance(val, str):        return False
    if len(val.strip()) < min_length:   return False
    
    if req_numbers:
        nums = [x for x in val if x.isdigit()]
        if not nums:
            return False
    
    if req_mix_case:
        lcase = [x for x in val if x.islower()]
        ucase = [x for x in val if x.isupper()]
        if not all([lcase,ucase]):
            return False

    if req_special_chars:
        special_chars = re.compile(accepted_special_chars)
        if special_chars.search(val) == None:
            return False
    
    return True
