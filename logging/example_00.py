import logging

loggerC = logging.getLogger("system.networking.http")
loggerA = logging.getLogger("system.networking")
loggerB = logging.getLogger("system")
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter("%(asctime)s %(levelno)d %(levelname)s %(module)s [%(name)s] %(message)s"))
loggerA.addHandler(streamHandler)
loggerA.setLevel(logging.DEBUG)
loggerB.addHandler(streamHandler)
#loggerA.propagate = False
root = logging.getLogger()

print "root logger name", root.name
print loggerA.name, loggerB.name, loggerC.name
loggerB.warning("test")
loggerA.debug("test")
loggerC.error("test")

