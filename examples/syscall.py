from Exrop import Exrop
import time

rop = Exrop("libc.so.6")
t = time.mktime(time.gmtime())
rop.find_gadgets(cache=True) # it's slow for first analyze keep waiting
print(f"Analyzing done in {time.mktime(time.gmtime()) - t}s")
chain = rop.syscall(1, (1,2,3))
chain.dump()
#print(chain.payload_str())
