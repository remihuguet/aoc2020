import passport


filename = '4/test_input.txt'


def test_parse_batch_file_properly():
    passports = passport.read_batch(filename)
    assert 4 == len(passports)
    assert "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm" == passports[0]


def test_passport_is_valid_againt_fields():
    passports = passport.read_batch(filename)

    assert passport.is_valid(passports[0])
    assert not passport.is_valid(passports[1])
    assert passport.is_valid(passports[2])
    assert not passport.is_valid(passports[3])


def test_count_valids():
    assert 2 == passport.count_valids(filename)


def test_validate_byr():
    assert passport.is_byr_valid('byr:2002')
    assert not passport.is_byr_valid('byr:2003')
    assert not passport.is_byr_valid('byr:2dsdsdsds')
    assert passport.is_byr_valid('byr:1920')
    assert not passport.is_byr_valid('byr:1919')
    assert not passport.is_byr_valid('byr:192')
    assert not passport.is_byr_valid('byr:20022')
    assert passport.is_byr_valid('byr:2002 ')
    assert passport.is_byr_valid('dskdlms byr:2002 hgt:fdiksdlkd')


def test_validate_hgt():
    assert passport.is_hgt_valid('dsdsd hgt:60in fkmdslkfml')
    assert passport.is_hgt_valid('hgt:59in')
    assert passport.is_hgt_valid('dsdsd hgt:76in fkmdslkfml')
    assert not passport.is_hgt_valid('dsdsd hgt:77in fkmdslkfml')
    assert not passport.is_hgt_valid('hgt:190in')
    assert not passport.is_hgt_valid('hgt:58in')

    assert passport.is_hgt_valid('dfsdsd hgt:150cm ')
    assert passport.is_hgt_valid('dfsdsd hgt:190cm ')
    assert passport.is_hgt_valid('dfsdsd hgt:193cm ')
    assert not passport.is_hgt_valid('dfsdsd hgt:194cm ')
    assert not passport.is_hgt_valid('hgt:149cm')
    assert not passport.is_hgt_valid('hgt:190')
    assert not passport.is_hgt_valid('hgt:1919')


def test_validate_iyr():
    assert passport.is_iyr_valid('iyr:2010')
    assert not passport.is_iyr_valid('iyr:2008')
    assert not passport.is_iyr_valid('iyr:2dsdsdsds')
    assert passport.is_iyr_valid('iyr:2020')
    assert passport.is_iyr_valid('iyr:2012')


def test_validate_eyr():
    assert passport.is_eyr_valid('eyr:2020')
    assert not passport.is_eyr_valid('eyr:2018')
    assert not passport.is_eyr_valid('eyr:2dsdsdsds')
    assert passport.is_eyr_valid('eyr:2030')
    assert not passport.is_eyr_valid('eyr:2032')


def test_validate_hcl():
    assert passport.is_hcl_valid('hcl:#12ac45')
    assert not passport.is_hcl_valid('hcl:#12ac45dd')
    assert not passport.is_hcl_valid('hcl:12ac45')
    assert not passport.is_hcl_valid('hcl:#12ac4')
    assert not passport.is_hcl_valid('hcl:#12ac4!')


def test_validate_ecl():
    assert passport.is_ecl_valid('ecl:amb')
    assert passport.is_ecl_valid('ecl:blu')
    assert passport.is_ecl_valid('ecl:brn')
    assert passport.is_ecl_valid('ecl:gry')
    assert passport.is_ecl_valid('ecl:grn')
    assert passport.is_ecl_valid('ecl:hzl')
    assert passport.is_ecl_valid('ecl:oth')
    assert not passport.is_ecl_valid('ecl:amc')
    assert not passport.is_ecl_valid('ecl:bla')
    assert not passport.is_ecl_valid('ecl:brnaaa')
    assert not passport.is_ecl_valid('ecl:1112323')


def test_validate_pid():
    assert passport.is_pid_valid('pid:012345678')
    assert passport.is_pid_valid('pid:458289043')
    assert not passport.is_pid_valid('pid:akdfmlkf')
    assert not passport.is_pid_valid('pid:45828904312323232')
    assert not passport.is_pid_valid('pid:4232')


def test_are_fields_valid():
    p = 'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f'
    assert passport.are_fields_valid(p)


def test_are_fields_invalid():
    p = 'eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926'
    assert not passport.are_fields_valid(p)


def test_invalidate_passports():
    passports = [
        'eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
        'iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946',
        'hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
        'hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007'
    ]
    assert 0 == passport.count_valid_passports(passports)


def test_validate_passports():
    passports = [
        'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f',
        'eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
        'hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022',
        'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'
    ]
    assert 4 == passport.count_valid_passports(passports)
