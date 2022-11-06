#!/usr/bin/env python3
# used https://github.com/alphacep/vosk-api/blob/master/python/example/test_microphone.py as a base. it works.

voskmodel = "vosk-model-en-us-0.22"
# voskmodel = "vosk-model-en-us-0.22-lgraph"

# I just want to mention that this just came into my head while watching YouTube in VRChat.

import argparse
import queue
import sys
import time
import sounddevice as sd
import json
from pythonosc import udp_client
from vosk import Model, KaldiRecognizer

q = queue.Queue()


def int_or_str(text):
    try:
        return int(text)
    except ValueError:
        return text


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    "-l",
    "--list-devices",
    action="store_true",
    help="show list of audio devices and exit",
)
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser],
)
parser.add_argument(
    "-d", "--device", type=int_or_str, help="input device (numeric ID or substring)"
)
parser.add_argument("-r", "--samplerate", type=int, help="sampling rate")
args = parser.parse_args(remaining)

try:
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, "input")
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info["default_samplerate"])

    model = Model(voskmodel)
    with sd.RawInputStream(
        samplerate=args.samplerate,
        blocksize=8000,
        device=args.device,
        dtype="int16",
        channels=1,
        callback=callback,
    ):

        osc_client = udp_client.SimpleUDPClient("127.0.0.1", 9000) # Gotta connect it to VRChat
        osc_client.send_message("/input/Jump", 0) # Reset the /input/Jump parameter, just in case we exited mid time.sleep(1) or some weird shit like that.

        rec = KaldiRecognizer(model, args.samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                vc = json.loads(rec.Result())["text"]
                print(vc)
                if vc.lower().find("apple") != -1:
                    print("I heard apple!!!!!")
                    osc_client.send_message("/input/Jump", 1) # Say Apple.
                    time.sleep(1)
                    osc_client.send_message("/input/Jump", 0)

except KeyboardInterrupt:
    print("Finished.")
    parser.exit(0)
