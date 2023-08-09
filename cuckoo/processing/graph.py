# Copyright (C) 2016 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.
# Developed by Luqman Hariz

import os
import subprocess

from cuckoo.common.abstracts import Processing
from cuckoo.common.exceptions import CuckooProcessingError


class Graph(Processing):
    """Generate a graph from procmon.csv using visualize_logs(plotprocmoncsv)."""

    def run(self):
	self.key = "graph"
        procmon_csv = os.path.join(self.analysis_path, "files",  "procmon.csv")    
        if not os.path.exists(procmon_csv):
            raise CuckooProcessingError("procmon.csv not found.")

        graph_html = os.path.join(self.analysis_path, "files", "graph.html")

        try:
	        #check_call is for python 2.7 / run is for python 3 and above
            subprocess.check_call(
                [
                    "plotprocmoncsv",
                    "-pa",
                    "-sp",
                    "-t",
                    "All Events",
                    "-f",
                    graph_html,
                    procmon_csv,
                ]
            )
        except subprocess.CalledProcessError:
            raise CuckooProcessingError("Failed to generate html graph using.")

        print(graph_html)
        # Store the graph in the global container
        data = graph_html
    
        return data
