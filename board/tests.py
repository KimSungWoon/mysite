from django.test import TestCase

#
# paging
#

# 페이지당 글의 갯수
SZLIST = 5

# 표시할 페이지 수
SZPAGE = 5


total_count = 74

page_count = round(74 / SZLIST)
print(page_count)

