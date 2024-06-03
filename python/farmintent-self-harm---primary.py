# A. John, A. Marchant, 2024.

import sys, csv, re

codes = [{"code":"U20A7","system":"readv2"},{"code":"U20C7","system":"readv2"},{"code":"U2A7.","system":"readv2"},{"code":"U2007","system":"readv2"},{"code":"U2z7.","system":"readv2"},{"code":"U257.","system":"readv2"},{"code":"U2037","system":"readv2"},{"code":"U237.","system":"readv2"},{"code":"U2087","system":"readv2"},{"code":"U2077","system":"readv2"},{"code":"U247.","system":"readv2"},{"code":"U20B7","system":"readv2"},{"code":"U2027","system":"readv2"},{"code":"U2067","system":"readv2"},{"code":"U2D7.","system":"readv2"},{"code":"U2057","system":"readv2"},{"code":"U2017","system":"readv2"},{"code":"U20y7","system":"readv2"},{"code":"U2y7.","system":"readv2"},{"code":"U217.","system":"readv2"},{"code":"U267.","system":"readv2"},{"code":"U227.","system":"readv2"},{"code":"U2047","system":"readv2"},{"code":"U297.","system":"readv2"},{"code":"U287.","system":"readv2"},{"code":"X79.7","system":"readv2"},{"code":"X64.7","system":"readv2"},{"code":"X83.7","system":"readv2"},{"code":"X61.7","system":"readv2"},{"code":"X81.7","system":"readv2"},{"code":"X69.7","system":"readv2"},{"code":"X77.7","system":"readv2"},{"code":"X60.7","system":"readv2"},{"code":"X80.7","system":"readv2"},{"code":"X72.7","system":"readv2"},{"code":"X82.7","system":"readv2"},{"code":"X67.7","system":"readv2"},{"code":"X71.7","system":"readv2"},{"code":"X75.7","system":"readv2"},{"code":"X66.7","system":"readv2"},{"code":"X74.7","system":"readv2"},{"code":"X73.7","system":"readv2"},{"code":"X63.7","system":"readv2"},{"code":"X84.7","system":"readv2"},{"code":"X78.7","system":"readv2"},{"code":"X70.7","system":"readv2"},{"code":"X62.7","system":"readv2"},{"code":"X68.7","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('self-harm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["farmintent-self-harm---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["farmintent-self-harm---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["farmintent-self-harm---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
