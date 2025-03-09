function filtered_signal = filterSignal(signal, window_size)
    % Simple moving average filter
    % Parameters:
    %   signal: Input signal to be filtered
    %   window_size: Size of the moving average window
    
    if mod(window_size, 2) == 0
        window_size = window_size + 1; % Ensure odd window size
    end
    
    filtered_signal = zeros(size(signal));
    half_window = floor(window_size/2);
    
    % Pad the signal with border values
    padded_signal = [repmat(signal(1), [1, half_window]) signal repmat(signal(end), [1, half_window])];
    
    % Apply moving average filter
    for i = 1:length(signal)
        filtered_signal(i) = mean(padded_signal(i:i+window_size-1));
    end
end