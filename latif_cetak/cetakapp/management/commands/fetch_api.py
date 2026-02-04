import hashlib
import requests
from datetime import datetime, timedelta, timezone
from django.core.management.base import BaseCommand
from cetakapp.models import Produk, Kategori, Status


class Command(BaseCommand):
    help = "Fetch data from Fastprint API and sync with local database"

    def handle(self, *args, **options):
        url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

        wib = timezone(timedelta(hours=7))
        now = datetime.now(wib)
        date_str = now.strftime("%d-%m-%y")
        date_str_short = now.strftime("%d%m%y")
        hour_str = now.strftime("%H")

        username = f"tesprogrammer{date_str_short}C{hour_str}"
        password_raw = f"bisacoding-{date_str}"
        password_md5 = hashlib.md5(password_raw.encode()).hexdigest()

        self.stdout.write(f"Using Username: {username}")
        self.stdout.write(f"Using Password: {password_raw} (MD5: {password_md5})")

        data = {"username": username, "password": password_md5}

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()

            result = response.json()

            if result.get("error") == 0:
                products = result.get("data", [])
                self.stdout.write(self.style.SUCCESS(f"Found {len(products)} products"))

                for item in products:
                    # Get or create Kategori
                    kategori_name = item.get("kategori", "Tanpa Kategori")
                    kategori, _ = Kategori.objects.get_or_create(
                        nama_kategori=kategori_name
                    )

                    # Get or create Status
                    status_name = item.get("status", "bisa dijual")
                    status, _ = Status.objects.get_or_create(nama_status=status_name)

                    # Create or update Produk
                    Produk.objects.update_or_create(
                        id_produk=item.get("id_produk"),
                        defaults={
                            "nama_produk": item.get("nama_produk"),
                            "harga": item.get("harga"),
                            "kategori": kategori,
                            "status": status,
                        },
                    )
                self.stdout.write(self.style.SUCCESS("Database synced successfully!"))
            else:
                self.stdout.write(self.style.ERROR(f"API Error: {result.get('ket')}"))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Request failed: {e}"))
        except ValueError as e:
            self.stdout.write(self.style.ERROR(f"Failed to parse JSON: {e}"))
            self.stdout.write(f"Response content: {response.text}")
