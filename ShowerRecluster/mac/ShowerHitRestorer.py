import sys

if len(sys.argv) < 2:
    msg  = '\n'
    msg += "Usage 1: %s $INPUT_ROOT_FILE\n" % sys.argv[0]
    msg += '\n'
    sys.stderr.write(msg)
    sys.exit(1)


# Import the needed modules.  Need larlite and several of it's namespaces
from ROOT import gSystem,TMath
from larlite import larlite as fmwk
from larlite import larutil
from recotool import cmtool, showerreco
from ROOT import protoshower, calo

# Create ana_processor instance
my_proc = fmwk.ana_processor()

# Set input root file
for x in xrange(len(sys.argv)-1):
    my_proc.add_input_file(sys.argv[x+1])

# Specify IO mode
my_proc.set_io_mode(fmwk.storage_manager.kBOTH)

# Specify analysis output root file name
my_proc.set_ana_output_file("data/ShowerHitRestorer_ana.root")
# Specify data output root file name
my_proc.set_output_file("data/ShowerHitRestorer.root")

# Create instance of ShowerHitRestorer
shr = fmwk.ShowerHitRestorer()

# Set producer for input shower objects
shr.SetInputProducer("showerreco")

# Set producer for new hits & cluster => hit associations
shr.SetOutputProducer("ShowerHitRestorer")

# Name of output tree in ana file
shr.SetTreeName("ShowerHitRestorer")

# Attach ana module
my_proc.add_process(shr)

print
print  "Finished configuring ana_processor. Start event loop!"
print

my_proc.run(0)

sys.exit()

