clc;clear

% Script to merge multiple NetCDF files into yearly files
% For TRMM 3B42 Daily data (3B42_Daily.YYYYMMDD.7.nc4)

% Directory containing all NetCDF files
inputDir = "C:\Users\lv299\OneDrive\A_Melbourne-Uni\A_Weather_for_21st_Century_RA_Internship\Local_Remote_Influences_on_Coastal_Rainfall\Data_preparation\TRMM";  % Update this path

% Directory to save yearly output files
outputDir = "C:\Users\lv299\OneDrive\A_Melbourne-Uni\A_Weather_for_21st_Century_RA_Internship\Local_Remote_Influences_on_Coastal_Rainfall\Data_preparation";  % Update this path

% Create output directory if it doesn't exist
if ~exist(outputDir, 'dir')
    mkdir(outputDir);
end

% Get list of all NetCDF files
fileList = dir(fullfile(inputDir, '3B42_Daily.*.7.nc4'));
fprintf('Found %d files to process\n', length(fileList));

% Extract dates from filenames and organize by year
filesByYear = containers.Map('KeyType', 'double', 'ValueType', 'any');

for i = 1:length(fileList)
    filename = fileList(i).name;
    
    % Extract date from filename using regular expression
    dateMatch = regexp(filename, '3B42_Daily\.(\d{8})\.7\.nc4', 'tokens');
    
    if ~isempty(dateMatch)
        dateStr = dateMatch{1}{1};
        fileDate = datetime(dateStr, 'InputFormat', 'yyyyMMdd');
        yearValue = year(fileDate);
        
        % Add file to the appropriate year's list
        if ~isKey(filesByYear, yearValue)
            filesByYear(yearValue) = {};
        end
        
        % Store both filename and date for sorting later
        fileEntry = struct('filename', fullfile(inputDir, filename), 'date', fileDate);
        yearFiles = filesByYear(yearValue);
        yearFiles{end+1} = fileEntry;
        filesByYear(yearValue) = yearFiles;
    else
        fprintf('Warning: Could not extract date from %s, skipping\n', filename);
    end
end

% Get sorted list of years
years = cell2mat(keys(filesByYear));
years = sort(years);
