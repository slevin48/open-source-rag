% query.m
function query()
    % Engage in a chat with your Drive files
    disp("Ask query based on your Drive projects")
    disp("---")
    while true
        question = input("User: ", "s");
        question = string(question);
        % disp("User: " + question)
        if question == "end"
            disp("AI: Closing the chat. Have a great day!")
            break;
        end
        response = py.query.ask(question);
        response = string(py.str(response));
        disp("AI: ")
        disp(response)
        disp("---")
    end
end