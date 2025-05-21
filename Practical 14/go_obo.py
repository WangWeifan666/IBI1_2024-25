import xml.dom.minidom
import xml.sax
import datetime

# File path
file_path = r"C:\Users\ASUS\Desktop\ZJE\IBI1\IBI1_2024-25\Practical14\go_obo.xml"

def remove_bom(file_path):
    """
    Remove the BOM (Byte Order Mark) from the file.
    """
    try:
        with open(file_path, "rb") as file:
            content = file.read()
        if content.startswith(b'\xef\xbb\xbf'):
            content = content[3:]
        with open(file_path, "wb") as file:
            file.write(content)
    except Exception as e:
        print(f"Error removing BOM: {e}")

# Remove BOM
remove_bom(file_path)

def parse_go_obo_dom(file_path):
    """
    Parse the GO OBO XML file using the DOM API.
    """
    start_time = datetime.datetime.now()
    ontology_results = {
        "molecular_function": {"term_id": None, "is_a_count": 0},
        "biological_process": {"term_id": None, "is_a_count": 0},
        "cellular_component": {"term_id": None, "is_a_count": 0}
    }
    try:
        doc = xml.dom.minidom.parse(file_path)
        terms = doc.getElementsByTagName("term")
        for term in terms:
            term_id = term.getElementsByTagName("id")[0].firstChild.data
            namespace = term.getElementsByTagName("namespace")[0].firstChild.data
            is_a_count = len(term.getElementsByTagName("is_a"))
            if namespace in ontology_results and is_a_count > ontology_results[namespace]["is_a_count"]:
                ontology_results[namespace]["term_id"] = term_id
                ontology_results[namespace]["is_a_count"] = is_a_count
    except Exception as e:
        print(f"Error parsing with DOM API: {e}")
    end_time = datetime.datetime.now()
    return ontology_results, end_time - start_time

class GOTermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.current_term = {}
        self.ontology_results = {
            "molecular_function": {"term_id": None, "is_a_count": 0},
            "biological_process": {"term_id": None, "is_a_count": 0},
            "cellular_component": {"term_id": None, "is_a_count": 0}
        }

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == "term":
            self.current_term = {"is_a_count": 0}

    def endElement(self, tag):
        if tag == "term":
            namespace = self.current_term.get("namespace")
            if namespace in self.ontology_results and self.current_term["is_a_count"] > self.ontology_results[namespace]["is_a_count"]:
                self.ontology_results[namespace]["term_id"] = self.current_term["id"]
                self.ontology_results[namespace]["is_a_count"] = self.current_term["is_a_count"]
            self.current_term = {}

    def characters(self, content):
        if self.current_tag == "id":
            self.current_term["id"] = content
        elif self.current_tag == "namespace":
            self.current_term["namespace"] = content
        elif self.current_tag == "is_a":
            self.current_term["is_a_count"] = self.current_term.get("is_a_count", 0) + 1

def parse_go_obo_sax(file_path):
    """
    Parse the GO OBO XML file using the SAX API.
    """
    start_time = datetime.datetime.now()
    handler = GOTermHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    try:
        parser.parse(file_path)
    except Exception as e:
        print(f"Error parsing with SAX API: {e}")
    end_time = datetime.datetime.now()
    return handler.ontology_results, end_time - start_time

def print_results(results, duration, api_name):
    """
    Print the parsing results and the time taken.
    """
    print(f"Results using {api_name}:")
    for ontology, data in results.items():
        print(f"{ontology.capitalize().replace('_', ' ')}:")
        print(f"Term ID: {data['term_id']}")
        print(f"Number of <is_a> elements: {data['is_a_count']}")
        print()
    print(f"{api_name} Time Taken: {duration.total_seconds()} seconds")
    print("-" * 40)

# Parse using DOM API
dom_results, dom_duration = parse_go_obo_dom(file_path)
print_results(dom_results, dom_duration, "DOM API")

# Parse using SAX API
sax_results, sax_duration = parse_go_obo_sax(file_path)
print_results(sax_results, sax_duration, "SAX API")

# Compare performance
if dom_duration < sax_duration:
    print("DOM API was faster.")
elif sax_duration < dom_duration:
    print("SAX API was faster.")
else:
    print("Both APIs had the same performance.")