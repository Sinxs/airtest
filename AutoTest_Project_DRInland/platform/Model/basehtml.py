# -*- coding: utf-8 -*-__author__ = "Lee.le"from django.shortcuts import renderfrom django.contrib.auth.decorators import login_requiredfrom django.shortcuts import render_to_responsefrom Model.tools import *@login_requireddef myview(request):    return render_to_response('index.html')def base(request):    """    base.html基础网页，用于其他页面继承    :param request:    :return:    """    return render(request, 'baseauto.html', {'addr': get_addr()})