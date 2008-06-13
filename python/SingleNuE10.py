import FWCore.ParameterSet.Config as cms
def customise(process):

# user schedule: 

    del process.schedule[:]

    process.schedule.append(process.generation_step)
    process.schedule.append(process.simulation_step)
    process.schedule.append(process.digitisation_step)
    process.schedule.append(process.L1_Emulation)
    process.schedule.append(process.digi2raw_step)
    process.schedule.append(process.raw2digi_step)
    process.schedule.append(process.reconstruction_step)

    process.load("Validation/Configuration/noiseSimValid_cff")
    process.local_validation = cms.Path((process.globalhitsanalyze+process.globaldigisanalyze+process.noiseSimValid)*process.MEtoEDMConverter)
    process.schedule.append(process.local_validation)

    process.schedule.append(process.outpath)

    return(process)