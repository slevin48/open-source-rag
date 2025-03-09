% Generate a noisy signal and save to CSV
t = 0:0.01:10;  % Time vector
f = 1;          % Frequency of the original signal
A = 2;          % Amplitude

% Generate clean signal
clean_signal = A * sin(2*pi*f*t);

% Add noise
noise = 0.5 * randn(size(t));
noisy_signal = clean_signal + noise;

% Save to CSV
data = [t' noisy_signal' clean_signal'];
headers = {'Time', 'Noisy_Signal', 'Clean_Signal'};
T = array2table(data, 'VariableNames', headers);
writetable(T, 'signal_data.csv');