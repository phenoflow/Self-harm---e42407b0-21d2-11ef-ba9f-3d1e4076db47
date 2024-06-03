# A. John, A. Marchant, 2024.

import sys, csv, re

codes = [{"code":"ZX12.","system":"readv2"},{"code":"ZX15.","system":"readv2"},{"code":"ZX13.","system":"readv2"},{"code":"ZX1N.","system":"readv2"},{"code":"U2E..","system":"readv2"},{"code":"ZX191","system":"readv2"},{"code":"ZX1L2","system":"readv2"},{"code":"ZX1L6","system":"readv2"},{"code":"ZX131","system":"readv2"},{"code":"ZX19.","system":"readv2"},{"code":"ZX1L1","system":"readv2"},{"code":"ZX1LD","system":"readv2"},{"code":"ZX192","system":"readv2"},{"code":"ZX11.","system":"readv2"},{"code":"ZX1E.","system":"readv2"},{"code":"ZX1C.","system":"readv2"},{"code":"ZX18.","system":"readv2"},{"code":"ZX1L3","system":"readv2"},{"code":"ZX1M.","system":"readv2"},{"code":"ZX1L.","system":"readv2"},{"code":"ZX1G.","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('self-harm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["self-harm-selfmutilation---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["self-harm-selfmutilation---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["self-harm-selfmutilation---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
