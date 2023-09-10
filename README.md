# pdf-tools
programs that contains basic pdf tools using PyMuPDF
## what can i do?
- [x] creating watermark
- [x] sign pdf using image file
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

to run this program, use ```python main.py -m [mode] -i [input.pdf] -o [output.pdf] -t [text, only required if you using watermark mode]```

in example, i want to make a "hello world" watermark on my doc.pdf file, and then save it on result.pdf, i just need to type ```python main.py -i doc.pdf -o result.pdf -t "hello world"```
