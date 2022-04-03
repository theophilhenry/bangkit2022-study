# Getopt and ArgParse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukan nama Anda")
parser.add_argument('-t', '--tanggallahir', required=True, help="Masukan tanggal lahir Anda (DD-MM-YYYY)")
args = parser.parse_args()

import re
date_format = "..-..-...."
check_format = re.match(date_format, args.tanggallahir)

from datetime import date
current_year = date.today().year
umur = current_year - int(args.tanggallahir[-4:])
pronouns = "kakak" if umur < 30 else "bapak"

if check_format:
    print("Terima kasih telah menggunakan arg_parser.py pada tahun {}, {} {}".format(current_year, pronouns, args.nama))


