import fitz

def start(input, output, text):
    # check whether document path is same as output path
    if (input != output):
        # split user input using comma
        input = input.split(',')
        output = output.split(',')
        for i in range(len(input)): # loop and open each document
            # remove any whitespace
            input_path = input[i].strip()
            output_path = output[i].strip()
            # open the document
            doc = fitz.open(input_path) 
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
                                        color = (141/255,142/255,145/255), # watermark grey color, adjust if you wanted to
                                        rotate = 0,
                                        )
                    # increase the text position
                    y = y+20
            # save output
            doc.save(output_path)
            print("Succesfully add watermark in", output_path)
    else:
        print("Document path and output path must not be the same!")
