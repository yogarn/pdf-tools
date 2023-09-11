from fitz import fitz, Rect

def start(input, output, signature, name):
    doc = fitz.open(input) # open file
    img = open(signature, "rb").read()
    for page in doc: # loop in case document has more than one page
        text_instances = page.search_for(name) # search name or keywords
        for inst in text_instances: # loop in case found more than one to sign
            inst = Rect(inst.x0-20, inst.y0-80, inst.x1+10, inst.y1+10) # adjust this value if your signature looks awful
            if not page.is_wrapped:
                page.wrap_contents()
            page.insert_image(inst, stream=img) # insert signature
            print(inst)
    doc.save(output)
