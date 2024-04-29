from django.contrib import admin
from drug.models import inpatient_tbl, outpatient_tbl,inproducts_tbl,outproducts_tbl,out_order_tbl
# Register your models here.
admin.site.register(inpatient_tbl)
admin.site.register(outpatient_tbl)
admin.site.register(inproducts_tbl)
admin.site.register(outproducts_tbl)
admin.site.register(out_order_tbl)