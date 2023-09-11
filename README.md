# pdf-tools
programs that contains basic pdf tools using PyMuPDF
## what can i do?
- [x] creating watermark
- [x] sign pdf using image file
- [x] apply to multiple document
- [ ] extract sentence that contain specific word
## how does this work?
### creating watermark
```
doc = fitz.open(input) 
        x = 75
        y = 72
```
at first, the program will open the document based on user argument input. then, the program will define starting point of the watermark. after that, the program will do a loop and print more watermark by increasing it's position. i know it might look awful, but i can't achieve a diagonal watermark yet, so this is the best i could do. PyMuPDF won't let me set it's rotation angle to something like 45 degrees.
```
while (y < 1000):
            for page in doc:
                position = fitz.Point(x, y)
                ...
                y = y+40
```
i might find a way around to overcome this problem in a near future. anyway, here's how it's look with watermark.

![image](https://github.com/yogarn/pdf-tools/assets/144443155/3c3ccefa-107c-4457-bc43-57ad8214d9c6)

to run this program, use the code below on terminal or command line. please note that if you use space in your watermark text, **make sure you use double quote in -t arguments**.
```
python main.py -m [mode] -i [input.pdf] -o [output.pdf] -t [watermark_text]
```

in example, i want to make a "hello world" watermark on my doc.pdf file, and then save it on result.pdf, i just need to type 
```
python main.py -m watermark -i doc.pdf -o result.pdf -t "hello world"
```

### signing pdf using image signature
the mechanism that work behind this program is actually pretty simple. PyMuPDF will find a preferred name or keywords that you want to sign and give the coordinate. after that, the program will adjust the coordinate, so that the signature will fit perfectly to the pdf document. the code below is the most important part in doing this job.
```
text_instances = page.search_for(name)
            for inst in text_instances: # loop in case found more than one name or keywords
                inst = Rect(inst.x0-20, inst.y0-80, inst.x1, inst.y1-10)
                ...
                page.insert_image(inst, stream=img) # insert signature image
```
to run this program, open terminal or command line and paste the code below. please note that all arguments provided below is **required** for this program to run.
```
python main.py -i [input_file.pdf] -o [output_file.pdf] -s [signature_image.png] -t [name_keywords]
```
in example, i want to sign doc.pdf file with my signature on signature.png file and save it on output.pdf. I'll run the code below on my terminal.
```
python main.py -m sign -i doc.pdf -o output.pdf -s signature.png -t "Yoga Raditya"
```

### using multiple input and/or output
in order to use multiple input in a single run, you need to provide those multiple document input and/or output in argument separated by comma inside double quote. for more information, please take a look at code below.
```
python main.py -m [mode] -i "first.pdf, second.pdf" -o "out_first.pdf, out_second.pdf" -t [text] -s [signature]
```
