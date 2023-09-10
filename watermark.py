import fitz

def start(input, output, text):
    # check whether document path is same as output path
    if (input != output):
        # open the document
        doc = fitz.open(input) 
        # set starting point
        x = 75
        y = 72
        # printing watermark through loop
        while (y < 1000):
            # printing for all page
            for page in doc:
                position = fitz.Point(x, y)
                # text properties
                rc = page.insert_text(position,
                                    text,
                                    fontname = "cour",
                                    fontsize = 18,
                                    rotate = 0,
                                    )
                # increase the text position
                y = y+40
        # save output
        doc.save(output)
        print("Succesfully add watermark on " + output)
    else:
        print("Document path and output path must not be the same!")