% index.m
function index(folder)
    % folder: folder to index
    % index("filter-project")
    if nargin < 1
        folder = 'filter-project';
    end
    py.index.index(folder);
    disp("Folder "+ folder +" indexed in .index/")
end