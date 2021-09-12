from functions import storage
from functions import register

with open("config.toml") as file:
    config = toml.load(file)["sessions"]

api_id = config["api_id"]
api_hash = config["api_hash"]

if storage.update is True:
    register.main()

sessions = storage.sessions("sessions", api_id, api_hash)
print("total accounts> %d \n" % len(sessions))
