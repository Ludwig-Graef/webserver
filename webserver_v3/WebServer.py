
import sys
import argparse
import www

if __name__ == "__main__":

    if sys.version_info[0] is not 3:
        print("ERROR: Please use Python version 3 !! (Your version: %s)"
              % (sys.version))
        exit(1)

    def type_port(x):
        x = int(x)
        if x < 1 or x > 65535:
            raise argparse.ArgumentTypeError(
                "Port number has to be greater than 1 and less than 65535.")
        return x

    description = ("Serves a local directory on your computer via the HTTP protocol."
                   "Use the www/serve.py file to implement your changes.")

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-a",
                        "--address",
                        help="The address to listen on. (Default: '127.0.0.1')",
                        default="127.0.0.1")
    parser.add_argument("-p",
                        "--port",
                        help="The port to listen on. (Default: 8080)",
                        type=type_port,
                        default=8080)

    args = parser.parse_args()

    www.serve(address=args.address, port=args.port)
