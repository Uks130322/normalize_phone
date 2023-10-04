import re


def norm_phone(phone: str) -> str:
    """Normalize phone number to format 1-NNN-NNN-NNNN"""
    pattern = re.compile(r"""
                        (?P<plus> [+] )?                 #plus in the begining
                        (?P<country_code> 1)?            #country code
                        (?P<first_symbol> [ .(-] *)?     #some symbols
                        (?P<city_code> [2-9] [0-8] \d)   #city code
                        (?P<second_symbol> [ .)-] *)?    #some symbols
                        (?P<gateway_code> [2-9] \d{2})   #gateway code
                        (?P<third_symbol> [ .-]*)?       #some symbols
                        (?P<station_code> \d{4})         #station code
                        """, re.X)

    if not pattern.match(phone):
        raise ValueError("Bad number")

    new_phone = pattern.sub(r"1-\g<city_code>"
                            r"-\g<gateway_code>"
                            r"-\g<station_code>", phone, re.X)
    return new_phone

#print(norm_phone("+1 (423) 456 7788"))

