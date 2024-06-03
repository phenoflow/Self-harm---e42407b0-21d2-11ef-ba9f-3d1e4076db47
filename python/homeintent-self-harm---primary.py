# A. John, A. Marchant, 2024.

import sys, csv, re

codes = [{"code":"U260.","system":"readv2"},{"code":"U2070","system":"readv2"},{"code":"U20A0","system":"readv2"},{"code":"U2D0.","system":"readv2"},{"code":"U2020","system":"readv2"},{"code":"U20C0","system":"readv2"},{"code":"U2A0.","system":"readv2"},{"code":"U210.","system":"readv2"},{"code":"U20B0","system":"readv2"},{"code":"U2050","system":"readv2"},{"code":"U280.","system":"readv2"},{"code":"U2000","system":"readv2"},{"code":"U20y0","system":"readv2"},{"code":"U2010","system":"readv2"},{"code":"U2060","system":"readv2"},{"code":"U220.","system":"readv2"},{"code":"U240.","system":"readv2"},{"code":"U2080","system":"readv2"},{"code":"U230.","system":"readv2"},{"code":"U2030","system":"readv2"},{"code":"U2y0.","system":"readv2"},{"code":"U2z0.","system":"readv2"},{"code":"U250.","system":"readv2"},{"code":"U2040","system":"readv2"},{"code":"U290.","system":"readv2"},{"code":"X68.0","system":"readv2"},{"code":"X79.0","system":"readv2"},{"code":"X61.0","system":"readv2"},{"code":"X63.0","system":"readv2"},{"code":"X77.0","system":"readv2"},{"code":"X75.0","system":"readv2"},{"code":"X78.0","system":"readv2"},{"code":"X69.0","system":"readv2"},{"code":"X67.0","system":"readv2"},{"code":"X70.0","system":"readv2"},{"code":"X73.0","system":"readv2"},{"code":"X64.0","system":"readv2"},{"code":"X72.0","system":"readv2"},{"code":"X66.0","system":"readv2"},{"code":"X82.0","system":"readv2"},{"code":"X71.0","system":"readv2"},{"code":"X80.0","system":"readv2"},{"code":"X83.0","system":"readv2"},{"code":"X74.0","system":"readv2"},{"code":"X60.0","system":"readv2"},{"code":"X84.0","system":"readv2"},{"code":"X62.0","system":"readv2"},{"code":"X81.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('self-harm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["homeintent-self-harm---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["homeintent-self-harm---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["homeintent-self-harm---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
