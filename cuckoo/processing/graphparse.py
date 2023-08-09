# Copyright (C) 2016 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.
# Developed by Luqman Hariz

import os
import subprocess
import json
import unicodecsv as csv
import time
import pandas as pd
import codecs

from cuckoo.common.abstracts import Processing
from cuckoo.common.exceptions import CuckooProcessingError

def parser_csv(input_file, keyword, output_file):
    rows_with_keyword = []

    with open(input_file, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Read the header row

        for row in csv_reader:
            for i, value in enumerate(row):
                if keyword in value:
                    rows_with_keyword.append(row)
                    break

    # Create a DataFrame from the rows with the keyword
    df = pd.DataFrame(rows_with_keyword, columns=headers)

    # Remove quotation marks from column A1 (first column)
    df.columns = df.columns.str.strip('"').str.replace('"', '')

    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False, encoding='utf-8')
        
    file.close()

class GraphParse(Processing):
    """Generate graphs from parse.csv using visualize_logs(plotprocmoncsv)."""

    def run(self):
        self.key = "graphparse"

        procmon_csv = os.path.join(self.analysis_path, "files",  "procmon.csv")
        if not os.path.exists(procmon_csv):
            raise CuckooProcessingError("procmon.csv not found for parsing.")
        parse_csv = os.path.join(self.analysis_path, "files", "parse.csv")

        #malware_name = self.get_name()
        #malware_name = self.set_results["target"]["file"]["name"]
        #path = temppath()
        json_path = os.path.join(self.analysis_path, "task.json")
        if not os.path.exists(json_path):
            raise CuckooProcessingError("task.json not found to get info.")
        
        with codecs.open(json_path, 'r', encoding='utf-8') as f:  
            json_read = f.read()
        
        json_string = json.loads(json_read) 
        malware_path = json_string["target"] 
        print("Target:", malware_path)

        malware_name = os.path.basename(malware_path)
        print("name:" + malware_name)

        parser_csv(procmon_csv, malware_name, parse_csv)
        time.sleep(3)

        if not os.path.exists(parse_csv):
            raise CuckooProcessingError("parse.csv not found.")

        parse_graph_html = os.path.join(self.analysis_path, "files", "parse_graph.html")

        try:
            subprocess.check_call(
                [
                    "plotprocmoncsv",
                    "-pa",
                    "-sp",
                    "-t",
                    "Focused",
                    "-f",
                    parse_graph_html,
                    parse_csv,
                ]
            )
        except subprocess.CalledProcessError:
            raise CuckooProcessingError("Failed to generate html graph from parse.csv.")

        # Store the graphs in the global container
        data = parse_graph_html

        return data


