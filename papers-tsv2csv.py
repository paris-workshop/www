import sys
import csv

# expected output format: UID,title,authors,abstract,keywords,sessions
# input format: TSV

class Paper:
    def __init__(self, input_record):
        self.record = {}
        self.record["UID"] = input_record["Paper ID"]
        self.record["title"] = input_record["Paper Title"]
        self.record["authors"] = input_record["Authors"]
        self.record["abstract"] = input_record["Abstract"]
        self.record["keywords"] = input_record["Q2 (Topics)"]
        self.record["sessions"] = "A/B" #input_record["sessions"]
    
    def print_paper(self):
        print(",".join([self.uid, self.title, self.authors, self.abstract, self.keywords, self.sessions]))

if __name__ == '__main__':
    writer = csv.DictWriter(sys.stdout, fieldnames=["UID","title","authors","abstract","keywords","sessions"], delimiter=",", quoting=csv.QUOTE_ALL)
    reader = csv.DictReader(sys.stdin, delimiter="\t")
    writer.writeheader()
    for record in reader:
        paper = Paper(record)
        writer.writerow(paper.record) 
    
