import pynucastro as pyna
from pynucastro.networks import StarKillerNetwork

library_file = "20180319default2"
mylibrary = pyna.rates.Library(library_file)

all_nuclei = ["p", "he4", "c12", "c13", "n13", "n14", "n15", "o14", "o15", "o16", "o17", "f17", "f18"]

nova_library = mylibrary.linking_nuclei(all_nuclei, with_reverse=False)

print(nova_library)

net = StarKillerNetwork(libraries=[nova_library])
net.write_network()
