from django.test import TestCase

import user.models as usermodels


def test_usermodels_insert():
    usermodels.insert('마이콜', 'michol@gmail.com', '1234', 'male')


def test_usermodels_fetchone():
    result = usermodels.fetchone('michol@gmail.com', '1234')
    print(result)


# test_usermodels_insert()
test_usermodels_fetchone()
