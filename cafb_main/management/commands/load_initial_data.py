from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from cafb_main.models import Product

class Command(BaseCommand):
    help = 'Provides intial data for UPC codes'

    def handle(self, *args, **options):

        path = settings.BASE_DIR

        file = path +'/cafb_main/fixtures/fixture.csv'

        self.stdout.write(file)
        with open(file, 'r+') as f:
            data = list(f)

        for product in data[1:]:
            product = unicode(product, 'utf-8').replace('\n', '').split(',')
            upc_code = int(product[1])

            obj = Product(gtin_code=upc_code, gtin_name=product[2])
            obj.save()

            self.stdout.write(self.style.SUCCESS('Product name: Added "%s"' % product[2]))
