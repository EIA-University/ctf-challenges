from scapy.all import *
import pickle
import base64
import zlib

original_data = "eNprYEouTk4sqNTLSaxMLSrWyzHici3JSC3iKmRIjk/OT0lNLuZKzQMxuAoZI+wZGBgO70dABjDgYHBlYNBgYGRgcGBTPNQcenjaoZbSegaggAiLAwMUBDApMBg5MTAUMkWwAbk5iSWZeYaFzG2FLEGFrK2FbEGF7BrujjftBF4Gc6X6gUBJIUeSHgB54y28"

message_decoded_b64 = base64.b64decode(original_data)

data_inflated = zlib.decompress(message_decoded_b64)

deserialized_data = pickle.loads(data_inflated)

deserialized_data.show()