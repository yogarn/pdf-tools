import argparse
import watermark

# create argument parser
parser = argparse.ArgumentParser(description="basic pdf tools using PyMuPDF")


parser.add_argument("--mode", "-m", choices=["watermark", "sign", "extract"], help="programs mode, currently available : watermark", required=True)
parser.add_argument("--input", "-i", help="input file path")
parser.add_argument("--output", "-o", help="output file path")
parser.add_argument("--text", "-t", help="used for watermark, extracting text (optional)")

args = parser.parse_args()

# check if user choose watermark mode
if args.mode == "watermark":
    # require input, output, and text
    if args.input is None or args.output is None or args.text is None:
        parser.error("Argumen '--input', '--output', dan '--text' required for watermark mode")
    else:
        watermark.start(args.input, args.output, args.text)
else:
    print(f"Mode: {args.mode}")