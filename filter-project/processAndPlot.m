% Import data from CSV and apply filter
data = readtable('signal_data.csv');
t = data.Time;
noisy_signal = data.Noisy_Signal;
clean_signal = data.Clean_Signal;

% Apply filter
window_size = 21;  % Adjust this value to change filter strength
filtered_signal = filterSignal(noisy_signal, window_size);

% Plot results
figure('Position', [100 100 1200 600]);

subplot(3,1,1)
plot(t, noisy_signal)
title('Noisy Signal')
xlabel('Time')
ylabel('Amplitude')
grid on

subplot(3,1,2)
plot(t, filtered_signal)
title('Filtered Signal')
xlabel('Time')
ylabel('Amplitude')
grid on

subplot(3,1,3)
plot(t, clean_signal)
title('Original Clean Signal')
xlabel('Time')
ylabel('Amplitude')
grid on

sgtitle('Signal Filtering Results')