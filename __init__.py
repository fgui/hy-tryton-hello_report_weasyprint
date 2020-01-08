import hy
from trytond.pool import Pool
from . import hello

def register():
    Pool.register(
        hello.HelloReport,
        module='hello_report_weasyprint', type_='model')
