#  The server bit that connects and reads messages
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected with result code "+str(rc))

    # Here you can subscribe to whatever topics you like
    # use '#' for a 'wildcard' - subscribe to any messages
    client.subscribe("gc/yourtopic")

def on_message(client, userdata, msg):
    print('\033[92m' + msg.topic + ":\033[0m \n" + msg.payload.decode("utf-8")  + "\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.5", 1883, 60)
client.loop_forever()
