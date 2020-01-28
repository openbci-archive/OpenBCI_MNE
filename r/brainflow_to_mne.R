library(brainflow)
library(mne)


params <- brainflow_python$BrainFlowInputParams ()
board_shim <- brainflow_python$BoardShim (brainflow_python$BoardIds$SYNTHETIC_BOARD$value, params)
board_shim$prepare_session ()
board_shim$start_stream ()
Sys.sleep (time = 5)
board_shim$stop_stream ()
data <- board_shim$get_current_board_data (as.integer (250))
board_shim$release_session ()

eeg_channels <- brainflow_python$BoardShim$get_eeg_channels (brainflow_python$BoardIds$SYNTHETIC_BOARD$value)
eeg_data <- np$array (data[eeg_channels,])

# Creating MNE objects from brainflow data arrays
ch_names = list ('T7', 'CP5', 'FC5', 'C3', 'C4', 'FC6', 'CP6', 'T8')
sfreq <- brainflow_python$BoardShim$get_sampling_rate (brainflow_python$BoardIds$SYNTHETIC_BOARD$value)
info <- mne$create_info (ch_names, sfreq)
raw <- mne$io$RawArray (eeg_data, info)
# get data from RawArray
data_raw_array <- raw$get_data()
