from django.urls import path
from .views import index, dgis, aigis, aqllishahar, article, asosiytexnologiyal, \
    bimgis, bulutligis, coloudgisserver, crossplatform, detail, edgegisserver, \
    events, gis9, gis10, joinus, kattamalumot, mulkboshqarish, news, \
    onlinegisplatform, services, supermapgishaqida, suvsaqlash, tabiatresurs, \
    tabiiyofat, terminalgisforpc, terminalgisforweb, terminalgisformobile, \
    transport, xavfsizlik, yermulk

urlpatterns = [
    path('', index, name="index"),
    path('dgis/', dgis, name="dgis"),
    path('aigis/', aigis, name="aigis"),
    path('aqllishahar/', aqllishahar, name="aqllishahar"),
    path('article/', article, name="article"),
    path('services/', services, name="services"),
    path('terminalgisforweb/', terminalgisforweb, name="terminalgisforweb"),
    path('terminalgisformobile/', terminalgisformobile, name="terminalgisformobile"),
    path('transport/', transport, name="transport"),
    path('xavfsizlik/', xavfsizlik, name="xavfsizlik"),
    path('yermulk/', yermulk, name="yermulk"),
    path('supermapgishaqida/', supermapgishaqida, name="supermapgishaqida"),
    path('suvsaqlash/', suvsaqlash, name="suvsaqlash"),
    path('tabiatresurs/', tabiatresurs, name="tabiatresurs"),
    path('tabiiyofat/', tabiiyofat, name="tabiiyofat"),
    path('terminalgisforpc/', terminalgisforpc, name="terminalgisforpc"),
    path('asosiytexnologiyal/', asosiytexnologiyal, name="aqlasosiytexnologiyallishahar"),
    path('bimgis/', bimgis, name="bimgis"),
    path('bulutligis/', bulutligis, name="bulutligis"),
    path('coloudgisserver/', coloudgisserver, name="coloudgisserver"),
    path('crossplatform/', crossplatform, name="crossplatform"),
    path('detail/', detail, name="detail"),
    path('edgegisserver/', edgegisserver, name="edgegisserver"),
    path('events/', events, name="events"),
    path('gis9/', gis9, name="gis9"),
    path('gis10/', gis10, name="gis10"),
    path('joinus/', joinus, name="joinus"),
    path('kattamalumot/', kattamalumot, name="kattamalumot"),
    path('mulkboshqarish/', mulkboshqarish, name="mulkboshqarish"),
    path('news/', news, name="news"),
    path('onlinegisplatform/', onlinegisplatform, name="onlinegisplatform")
]