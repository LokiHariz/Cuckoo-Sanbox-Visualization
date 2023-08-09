# Cuckoo-Sanbox-Visualization

This is a final year project modified cuckoo sandbox 2.0.7 using visualization graph which is integrated with "Visualize_Logs" python library.

## What's has changed and makes it different to the original cuckoo sandbox?

* Added a new graph analysis tab for all analysis results (ransomware still in working)
* An interactive graph that can be moved, zoom in and out, and also filter processes and many more!
* Two graphs which are "Focused" (shwoing malware's processes and related to only) and "All Events"(All processes).
* Graphs can be exported as a html file and be transfered or give to anywhere for futher analysis.

## Example Usage

![graphanalysis](https://github.com/LokiHariz/Cuckoo-Sanbox-Visualization/assets/140133237/77fb6b5d-b270-4e63-ad53-0d4484c9cb88)

## Steps To Install Cuckoo with Visualization

### Requirements (This is required for the cuckoo and graph module to work with later on)

* Ubuntu 18.04
  
* Python 2.7
  * sudo apt update
  * sudo apt install python-minimal
  * python --version (to check python version)
    
* Python 3
  * sudo apt update
  * sudo apt install python3
  * python3 --version

* Windows 7 ISO

### Steps:

1. Install Cuckoo
   * https://beginninghacking.net/2022/11/16/how-to-setup-your-own-malware-analysis-box-cuckoo-sandbox/

2. Install Important Dependencies
   * sudo apt-get install graphviz (Graphviz)
   * sudo apt-get install xdotool
   * pip3 install pandas
   * pip install visualize_logs
   * pip3 install networkx==2.3
   * pip install unicodecsv

3. Replace and add files in Cuckoo
   * cuckoo: /usr/local/lib/python2.7/dist-packages/cuckoo/ (cuckoo installation path)
   * CWD: /home/[user]/.cuckoo/ (cuckoo working directory)
  
4. Symlink storage analyses in cuckoo/web/static (in order to fetch results for graph)
   * go to cuckoo/web/static and run using bash linkanalyses.sh

### To start and run the modified cuckoo sandbox

To run the cuckoo sandbox without typing the command manually, download cuckoo.sh and save it to home/[user]/ directory. Run in the terminal by using command bash cuckoo.sh (make sure to edit the file by inputting your password user). To open the cuckoo web back, run bash opencuckoo.sh.
