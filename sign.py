import fitz

def start(input, output, signature, name):
    # split user input using comma
    input = input.split(',')
    output = output.split(',')
    print(input[0])
    for i in range(len(input)): # loop and open each document
        # remove any whitespace
        input_path = input[i].strip()
        output_path = output[i].strip()
        doc = fitz.open(input_path) # open document
        img = open(signature, "rb").read() # load signature image
        for page in doc: # loop in case of multiple page document
            text_instances = page.search_for(name) # search name or keywords to be signed
            for inst in text_instances: # loop in case found more than one name or keywords
                # get name or keywords coordinate and adjust it
                # change this value if your signature looks awful
                inst = fitz.Rect(inst.x0-20, inst.y0-80, inst.x1, inst.y1-10)
                if not page.is_wrapped:
                    page.wrap_contents()
                page.insert_image(inst, stream=img) # insert signature image
        doc.save(output_path) # save output document
        print("Succesfully signing " + output_path)
