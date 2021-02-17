from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from selenium import webdriver
import geckodriver_autoinstaller
# driver = webdriver.Chrome
import time
from .models import UfoReport
from django.db import connection

class GetUfoByDate(APIView):

    def get(self, request):
        data = request.GET.get('date')
        browser = webdriver.Chrome()
        browser.get("http://www.nuforc.org/webreports/ndxe{0}.html".format(data))
        uf_r = UfoReport()
        lst = []
        arr = []
        row_count = len(browser.find_elements_by_xpath("//table/tbody/tr"))
        print(row_count)

        x = range(row_count)
        for n in x:
            rows = browser.find_elements_by_xpath("//table/tbody/tr[{0}]/td".format(n))
            str = ''
            for row in rows:
                str = str + '&&&'+row.text
            print(str)
            query = "INSERT INTO {0} values('{1}')".format('"UFO"', str)
            cursor = connection.cursor()
            cursor.execute(query)

        html = browser.page_source
        time.sleep(2)

        # close web browser
        browser.close()
        return JsonResponse(
            {'result': html},
            status=status.HTTP_200_OK)
