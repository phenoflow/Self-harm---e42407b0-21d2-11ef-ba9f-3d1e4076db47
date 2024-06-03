# A. John, A. Marchant, 2024.

import sys, csv, re

codes = [{"code":"TK4..","system":"readv2"},{"code":"TK55.","system":"readv2"},{"code":"TKz..","system":"readv2"},{"code":"TKxy.","system":"readv2"},{"code":"TK30.","system":"readv2"},{"code":"TKx01","system":"readv2"},{"code":"TKxz.","system":"readv2"},{"code":"TK51.","system":"readv2"},{"code":"TK60.","system":"readv2"},{"code":"TK5z.","system":"readv2"},{"code":"TKx5.","system":"readv2"},{"code":"TK...","system":"readv2"},{"code":"TK50.","system":"readv2"},{"code":"TK61.","system":"readv2"},{"code":"TK54.","system":"readv2"},{"code":"TKx0z","system":"readv2"},{"code":"TKx..","system":"readv2"},{"code":"TKx0.","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('self-harm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["self-harm-injuryjump---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["self-harm-injuryjump---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["self-harm-injuryjump---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
