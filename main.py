import argparse
import watermark
import sign

# create argument parser
parser = argparse.ArgumentParser(description="basic pdf tools using PyMuPDF")


parser.add_argument("--mode", "-m", choices=["watermark", "sign", "extract"], help="programs mode, currently available : watermark, signature", required=True)
parser.add_argument("--input", "-i", help="input file path")
parser.add_argument("--output", "-o", help="output file path")
parser.add_argument("--text", "-t", help="used for watermark, extracting text, signature name")
parser.add_argument("--signature", "-s", help="signature png file path")

args = parser.parse_args()

# check if user choose watermark mode
if args.mode == "watermark":
    # require input, output, and text
    if args.input is None or args.output is None or args.text is None:
        parser.error("Argument '--input', '--output', and '--text' required for watermark mode")
    else:
        watermark.start(args.input, args.output, args.text)
elif args.mode == "sign":
    # require input, output, signature, and text
    if args.input is None or args.output is None or args.text is None:
        parser.error("Argument '--input', '--output', '--signature', and '--text' required for sign mode")
    else:
        sign.start(args.input, args.output, args.signature, args.text)
else:
    print(f"Mode: {args.mode}")
